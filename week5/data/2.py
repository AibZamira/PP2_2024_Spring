import datetime

x = datetime.datetime.now()
y = x.day - 1
t = x.day + 1
print(f"Yeasterday: {y}")
print(f"Today: {x.day}")
print(f"Tomorrow: {t}")