def square(n):
    a = 1
    while a <= t:
        x = a ** 2
        yield x
        a += 1
  

t = int(input("Enter the number: "))

for x in square(t):
  print(x)
