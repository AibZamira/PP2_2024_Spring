import re

s = input()
pattern = r"a.+b$"
x = re.findall(pattern, s)
print(x)