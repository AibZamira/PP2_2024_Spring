import re

s = input()
pattern = r"[A-Z][a-z]*"
x = re.findall(pattern, s)
print(x)