import os

for x in range(65, 91):
    file_name = chr(x) + ".txt"
    os.remove(file_name)
