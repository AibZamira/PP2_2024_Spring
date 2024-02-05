class String:
    def __init__(self):
        self.consol = ""
    def getString(self):
        self.consol = input()
    def printString(self):
        print(self.consol.upper())

string = String()
string.getString()
string.printString()

