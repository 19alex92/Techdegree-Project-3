class input_user:
    
    def __init__(self, text):
        self.text = text

    def input_def(self, text):
        
        self.user_input = input(text, ">  ")
        return self.user_input
# has to get input from the user 


#class WriteToCsv:
# write input to a csv file
# change and delete items from that csv file
# display items from that csv file