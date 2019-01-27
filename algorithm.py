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

    def add_to_file(self, date, task, time, notes):
        with open('log.csv', 'a', newline='') as file: 
            file_is_empty = os.stat('log.csv').st_size == 0                 
            fieldnames = ['Date', 'Task name', 'Time spent', 'Notes']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if file_is_empty: 
                writer.writeheader()
            writer.writerow({'Date': date, 'Task name': task, 'Time spent': time, 'Notes': notes})


    def backup_file(self, initial_file):
        for data in initial_file:
            with open('log_backup.csv', 'a', newline='') as file:
                file_is_empty = os.stat('log_backup.csv').st_size == 0
                write = csv.DictWriter(file, data.keys())
                if file_is_empty:
                    write.writeheader()
                write.writerow(data)


    def update_file(self, initial_file):
        os.remove('log.csv')
        for data in initial_file:
            with open('log.csv', 'a', newline='') as file:
                file_is_empty = os.stat('log.csv').st_size == 0
                write = csv.DictWriter(file, data.keys())
                if file_is_empty:
                    write.writeheader()
                write.writerow(data)
        os.remove('log_backup.csv')


    def search(self, initial_file, search_file, key1, key2, regex, date_search, date1, date2, input_user, index_track):
        iteration = 0
       
        for data in initial_file:
            key_iter = 0
            if key1 and input_user in initial_file[iteration][key1]:
                index_track.append(iteration)
                search_file.append(dict(data))
                iteration += 1
            elif key2 and input_user in initial_file[iteration][key2]:
                index_track.append(iteration)
                search_file.append(dict(data))
                iteration += 1
            elif regex:
                for _ in regex:
                    pattern = re.search(input_user, initial_file[iteration][regex[key_iter]])
                    if pattern is None:
                        key_iter += 1
                        continue
                    elif pattern.group() in initial_file[iteration][regex[key_iter]]:
                        index_track.append(iteration)
                        search_file.append(dict(initial_file[iteration]))
                        key_iter += 1
                        break
                    else:
                        key_iter += 1
                iteration += 1
            elif date_search:
                if str(input_user) == initial_file[iteration][date_search]:
                    index_track.append(iteration)
                    search_file.append(dict(data))
                    iteration += 1
                elif date1 and date2:
                    saved_date = datetime.datetime.strptime(initial_file[iteration][date_search], "%Y-%m-%d %X")
                    if date1 <= saved_date and date2 >= saved_date:
                        index_track.append(iteration)
                        search_file.append(dict(data))
                        iteration += 1
                    else:
                        iteration += 1
            else:
                iteration += 1


    def edit_entry(self):
        pass

    def delete_entry(self, initial_file, delete_index):
            del initial_file[delete_index]
            return initial_file
            