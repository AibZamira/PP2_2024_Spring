import re

def test(pattern1, testData, testNumber, expectedResult):
    x = re.findall(pattern1, testData)
    y = "".join(x)

    pattern2 = r"[a-z]*"
    result = re.sub(pattern2, "", y).strip()
    print(result)

    if result == expectedResult:
        print(testNumber + " is passed")
    else:
        print(testNumber + " is not passed")

pattern1 = r"\S[a-zA-z][^\W]*"

test(pattern1, "StudentsOf Kbtu", "test1", "SOK")
test(pattern1, "WhatI s YournAme ?", "test1", "WIYA")
