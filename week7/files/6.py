import os

for x in range(65, 91):
    file_name = chr(x) + ".txt"
    with open(file_name, "w") as l:
        
        l.write("This is file: " + file_name)