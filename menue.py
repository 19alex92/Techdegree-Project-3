import os

def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")


def add_entry():
    input_csv = {"Date": None, "Title Task": None, "Time spent": None, "Notes": None}
    #clear_screen()
    print("What is the date of the task?")
    date = input("  > ")
    input_csv.update({"Date": date})
    
    print("What is the task titel?")
    task = input("  > ")
    input_csv.update({"Title Task": task})
    
    print("How much time in minutes?")
    time = input("  > ")
    input_csv.update({"Time spent": time})
    
    print("Additional notes...if you dont have any notes please press enter")
    notes = input("  > ")
    input_csv.update({"Notes": notes})
    
    print(input_csv)


def search_entry():
    clear_screen()
    print("How would you like to search for an entry?")

def main_menue():

    while True:

        #clear_screen()
        print("WORK LOG")
        print("What would you like to do?")
        print("a) Add new entry")
        print("b) Search in existing entries")
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