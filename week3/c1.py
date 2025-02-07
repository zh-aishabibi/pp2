class stringClass:
    def __init__(self):
        self.input_string = ""  # Initialize an empty string to store input

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print(self.input_string.upper())

# Creating an instance of the class
string_class = stringClass()

string_class.getString()
string_class.printString()

