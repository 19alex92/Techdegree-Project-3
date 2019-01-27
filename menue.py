import csv
import datetime
import os
import re

from algorithm import Search

start = Search()


def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")


def add_entry():
    #clear_screen()
    print("What is the date of the task?")
    raw_date = input("Use the format DD/MM/YYYY  > ")
    date = datetime.datetime.strptime(raw_date, "%d/%m/%Y")
    
    print("What is the task titel?")
    task = input("  > ")
    
    print("How much time in minutes?")
    time = input("  > ")
    
    print("Additional notes...if you dont have any notes please press enter")
    notes = input("  > ")


    with open('log.csv', 'a', newline='') as file: 
        file_is_empty = os.stat('log.csv').st_size == 0                 
        fieldnames = ['Date', 'Title', 'Time spent', 'Notes']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if file_is_empty: 
            writer.writeheader()
        writer.writerow({'Date': date, 'Title': task, 'Time spent': time, 'Notes': notes})
        

def search_entry():
    #clear_screen()
    input_user = None
    key1 = None
    key2 = None
    regex = None
    date_search = None
    date1 = None
    date2 = None
    initial_file = []
    search_file = []
    start.open_file(initial_file)
    print("How would you like to search for an entry?")
    print("a) By Date")
    print("b) Between dates")
    print("c) By Time Spent")
    print("d) By a word")
    print("e) By regex pattern")
    print("f) Back to main menue")
    input_search = input("  > ")

    if input_search == "a":
        # search by a date
        date_search = 'Date'
        print("Please enter a date")
        raw_date_input = input("Use the format DD/MM/YYYY:  ")
        input_user = datetime.datetime.strptime(raw_date_input, "%d/%m/%Y")
        start.search(initial_file, search_file, key1, key2, regex, date_search, date1, date2, input_user)
        print(search_file)
        
    elif input_search == "b":
        # search between two dates
        # IDEE suche zwischen der Unix Timestamp
        date_search = 'Date'
        print("Please enter the first date")
        try:
            raw_date1_input = input("Use the format DD/MM/YYYY:  ")
            date1 = datetime.datetime.strptime(raw_date1_input, "%d/%m/%Y")
        except ValueError:
            print("Ups seems like there is something wrong with your date, please try again!")
            raw_date1_input = input("Use the format DD/MM/YYYY:  ")
            date1 = datetime.datetime.strptime(raw_date1_input, "%d/%m/%Y")
        print("Please enter the second date")
        try:
            raw_date2_input = input("Use the format DD/MM/YYYY:  ")
            date2 = datetime.datetime.strptime(raw_date2_input, "%d/%m/%Y")
        except ValueError:
            print("Ups seems like there is something wrong with your date, please try again!")
            raw_date2_input = input("Use the format DD/MM/YYYY:  ")
            date2 = datetime.datetime.strptime(raw_date2_input, "%d/%m/%Y")
        start.search(initial_file, search_file, key1, key2, regex, date_search, date1, date2, input_user)
        print(search_file)
        pass

    elif input_search == "c":
        # search for time spent
        key1 = 'Time spent'
        print("Please enter how much time the task took in minutes")
        input_user = input("EXAMPLE: Use the format 45 for 45 minutes:  ")
        start.search(initial_file, search_file, key1, key2, regex, date_search, date1, date2, input_user)
        print(search_file)
        
    elif input_search == "d":
        # search for string title or notes
        key1 = 'Title'
        key2 = 'Notes'
        print("Please enter a word")
        input_user = input("It can be in the Title or Notes:  ")
        start.search(initial_file, search_file, key1, key2, regex, date_search, date1, date2, input_user)
        start.menue(search_file)
        
    elif input_search == "e":
        # search for regex pattern
        regex = ['Date', 'Title', 'Time spent', 'Notes']
        print("Please enter a regex pattern")
        input_user = input(":  ")
        start.search(initial_file, search_file, key1, key2, regex, date_search, date1, date2, input_user)
        print(search_file)
    elif input_search == "f":
        main_menue()


def main_menue():

    while True:
        #clear_screen()
        print("WORK LOG")
        print("What would you like to do?")
        print("a) Add new entry")
        print("b) Search for an existing entry")
        print("c) Quit program")
        input_menue = input("  > ")
        input_menue = input_menue.lower()
        if input_menue == "a":
            add_entry()
            continue
        elif input_menue == "b":
            search_entry()
            continue
        elif input_menue == "c":
            break
        else:
            raise ValueError("Please type in a valid character")


main_menue()