import csv


# class für with open + def für delete an item welches ich dann in die child class weiterleiten kann

class Reader:
    
    
    #@classmethod
    def open_file(self, dict_files):
        with open('log.csv', newline='') as file:
            reader = csv.DictReader(file)
            data = list(reader)
            
            for row in data:
                dict_files.append(dict(row))
            print(dict_files)
file = []
hello = Reader()
hello.open_file(file)



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

