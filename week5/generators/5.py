def gen(n):
    while n != 0:
        yield n
        n -= 1

n = int(input("Enter the number: "))
s = ""
for x in gen(n):
    print(x)