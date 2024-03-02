import os
import sys

if not os.access("random.txt", os.F_OK):
    with open("random.txt", "x") as f:
        pass
else:
    pass

path = input()
string = ""

if os.access(path, os.F_OK):
    with open(path, "r") as ph:
        for x in ph:
            string += str(x)
else:
    print("Such file does not exist")
    sys.exit()

with open("random.txt", "w") as file:
    file.write(string)

