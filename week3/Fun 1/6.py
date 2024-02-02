st = input().split()
i = len(st)
stg = ""
while i > 0:
    i = i - 1
    stg = stg + st[i] + " "
stg.strip()
print(stg)
