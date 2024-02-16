import datetime

x = datetime.datetime.now()
d = x.replace(microsecond=0)
print(f"The date is: {d}")