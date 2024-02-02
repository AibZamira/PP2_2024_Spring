def filter_prime(n):
    if n == 2 or n == 3 or n == 5:
        return True
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n == 1:
        return False
    else:
        return True

l = list(map(int, input().split()))
ls = []

for i in range(len(l)):
    if filter_prime(l[i]):
        ls.append(l[i])

print(ls)
