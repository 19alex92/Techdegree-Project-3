import csv
import datetime
import os
import re


class Search:

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def open_file(self, dict_files):
        with open('log.csv', newline='') as file:
            reader = csv.DictReader(file)
            data = list(reader)
            
            for row in data:
                dict_files.append(dict(row))


    def search(self, initial_file, search_file, key1, key2, regex, date_search, date1, date2, input_user):
        iteration = 0
       
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
                    pattern = re.search(input_user, initial_file[iteration][regex[key_iter]])
                    if pattern is None:
                        key_iter += 1
                        continue
                    elif pattern.group() in initial_file[iteration][regex[key_iter]]:
                        search_file.append(dict(initial_file[iteration]))
                        key_iter += 1
                        break
                    else:
                        key_iter += 1
                iteration += 1
            elif date_search:
                if str(input_user) == initial_file[iteration][date_search]:
                    search_file.append(dict(data))
                    iteration += 1
                elif date1 and date2:
                    saved_date = datetime.datetime.strptime(initial_file[iteration][date_search], "%Y-%m-%d %X")
                    if date1 <= saved_date and date2 >= saved_date:
                        search_file.append(dict(data))
                        iteration += 1
                    else:
                        iteration += 1
            else:
                iteration += 1


    def edit_entry(self):
        pass

    def delete_entry(self, menue_file, initial_file):
        self.clear_screen()
        for key, value in menue_file.items():
            print(key,": ", value)
        print("\nAre you sure you want to delete this entry? Y/N")
        user_input = input(">  ")
        if user_input.upper() == "Y":
            initial_file