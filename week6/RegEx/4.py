import re

s = input()
pattern = r"[A-Z][a-z]"
x = re.findall(pattern, s)
y = "".join(x)
print(y)