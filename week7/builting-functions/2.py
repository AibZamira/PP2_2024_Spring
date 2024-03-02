def any(x):
    cnt = 0
    for it in range(65, 91):
        if x == chr(it):
            return True
    return False

string = input()
cnt = 0
CNT = 0
for x in string:
    if not x.isalpha() or x == " ":
        continue
    else:
        if any(x):
            CNT += 1
        else:
            cnt += 1
print("Number of uppercase letter: ", CNT)
print("Number of lowercase letter: ", cnt)