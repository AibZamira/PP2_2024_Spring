import re


def test(pattern, testData, testNumber, expectedResult):
    result = re.sub(pattern, ":", testData)
    print(result)
    if result == expectedResult:
        print(testNumber + " is passed!")
    else: 
        print(testNumber + " is not passed!")



pattern = r"[ ,.]"
test(pattern, "Hello, world", "test1", "Hello::world")
test(pattern, "Hello, world.My name  is,Zamir a.", "test2", "Hello::world:My:name::is:Zamir:a:")
