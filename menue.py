from data_handling import input_user

input_menue = input_user(None)
# def menue 
print("WORK LOG")
print("What would you like to do?")
input_menue.input_def("test")
if input_menue.user_input == "a":
    print("Yeah!!")
else:
    print("Oh no")
    input_menue.input_def("textetet")