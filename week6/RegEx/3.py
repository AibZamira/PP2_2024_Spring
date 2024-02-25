import re

s = input()
pattern = r"[a-z]+(?:_[a-z]+)+"
x = re.findall(pattern, s)
print(x)
