def even(t):
    a = 0
    while a <= t:
        if a % 2 == 0:
            yield a
        a += 1

t = int(input("Enter the number: "))
s = ""
for x in even(t):
    s += str(x) + ", "
print(s[:-2])