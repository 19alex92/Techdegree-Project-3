import csv
import re


class Search:

    def open_file(self, dict_files):
        with open('log.csv', newline='') as file:
            reader = csv.DictReader(file)
            data = list(reader)
            
            for row in data:
                dict_files.append(dict(row))


    def search(self, initial_file, search_file, key1, key2, regex, input_user):
        iteration = 0
        
        #pattern = re.search(r'[\w*\d*]', initial_file[0]['Title'])
        #print(pattern)
       
        for data in initial_file:
            key_iter = 0
            if key1 and input_user in initial_file[iteration][key1]:
                search_file.append(dict(data))
                iteration += 1
            elif key2 and input_user in initial_file[iteration][key2]:
                search_file.append(dict(data))
                iteration += 1
            elif regex:

                for _ in regex:
                    pattern = re.search(r'[test]', initial_file[iteration][regex[key_iter]])
                    if pattern.group() in initial_file[iteration][regex[key_iter]]:
                        search_file.append(dict(initial_file[iteration]))
                        key_iter += 1
                        break
                    else:
                        key_iter += 1
                
                iteration += 1
            else:
                iteration += 1



# Diese Menü wird nachher dafür sein um das ergebnis auf die Ergebnisseite zu drucken
    #def menue(self, filled_file):
        #for data in filled_file:
            #print(data)
