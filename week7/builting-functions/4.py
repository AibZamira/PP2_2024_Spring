from threading import Timer

def sqrt(x, m):
    print(f"Square root of {x} after {m} miliseconds is {x**0.5}")

x = int(input())
m = int(input())
ml = m/1000
t = Timer(ml, sqrt, args=(x, m))
t.start() 
