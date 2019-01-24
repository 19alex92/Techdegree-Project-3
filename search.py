import csv
import os


# class für with open + def für delete an item welches ich dann in die child class weiterleiten kann

class Search:
    
    def __init__(self, dict_files):
        self.dict_files = dict_files

    def open_file(self):
        with open('log.csv', newline='') as file:
            reader = csv.DictReader(file)
            data = list(reader)
            
            for row in data:
                self.dict_files.append(dict(row))
                #return self.dict_files


    def date(self, filled_file, search_file):
        print("Please enter a date")
        input_date = input("Use the format DD/MM/YYYY:  ")
        #for data in filled_file:
         #   for dict_number in range(len(filled_file)):
          #      if input_date == filled_file[dict_number]['Date']:
           #         search_file.append(dict(data))

        for data in filled_file and range(len(filled_file)):
            if input_date == filled_file[data]['Date']:
                search_file.append(dict(data))



    def menue(self, filled_file):
        for data in filled_file:
            print(data)





initial_file = []
search_file = []
search = Search(initial_file)
search.open_file()
filled_file = initial_file
search.date(filled_file, search_file)
full_file = search_file
print(full_file)


# class search date as a child from open class
# 
# class search time spent as a child from open class
# 
# class search by word as a child...
# 
# class search by regex as a child...
# 
# class search between dates as a child..

# oder alle child in eine class mit if elif abfragen und diese dann aus dem menü herausnehmen

