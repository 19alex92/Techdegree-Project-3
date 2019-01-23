import csv
import os

def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")


def add_entry():
    #clear_screen()
    print("What is the date of the task?")
    date = input("  > ")
    
    print("What is the task titel?")
    task = input("  > ")
    
    print("How much time in minutes?")
    time = input("  > ")
    
    print("Additional notes...if you dont have any notes please press enter")
    notes = input("  > ")


    with open('log.csv', 'a', newline='') as file: 
        file_is_empty = os.stat('log.csv').st_size == 0                 
        fieldnames = ['Date', 'Title Task', 'Time spent', 'Notes']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if file_is_empty: 
            writer.writeheader()
        writer.writerow({'Date': date, 'Title Task': task, 'Time spent': time, 'Notes': notes})
        

def search_entry():
    #clear_screen()
    print("How would you like to search for an entry?")
    print("a) By Date")
    print("b) By Time Spent")
    print("c) By a word")
    print("d) By regex pattern")
    print("e) Between dates")
    print("f) Back to main menue")
    input_search = input("  > ")
    if input_search == "a":
        pass
    elif input_search == "b":
        pass
    elif input_search == "c":
        pass
    elif input_search == "d":
        pass
    elif input_search == "e":
        pass
    elif input_search == "f":
        main_menue()


def main_menue():

    while True:

        #clear_screen()
        print("WORK LOG")
        print("What would you like to do?")
        print("a) Add new entry")
        print("b) Search for an existing entry")
        print("c) Quit programm")
        input_menue = input("  > ")
        input_menue = input_menue.lower()
        if input_menue == "a":
            add_entry()
            continue
        elif input_menue == "b":
            search_entry()
        elif input_menue == "c":
            break
        else:
            raise ValueError("Please type in a valid character")


main_menue()