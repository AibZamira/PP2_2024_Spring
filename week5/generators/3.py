def even(t):
    a = 1
    while a <= t:
        if a % 3 == 0 and a % 4 == 0:
            yield a
        a += 1

t = int(input("Enter the number: "))
for x in even(t):
    print(x)
