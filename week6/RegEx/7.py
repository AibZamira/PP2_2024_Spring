import re

def uppercase(match):
    return match.group('X').replace('_', '').capitalize() + match.group('Y').replace('_', '').capitalize()

def test(pattern, testData, testNumber, expectedResult):
    result = re.sub(pattern, uppercase, testData)
    print(result)
    if result == expectedResult:
        print(testNumber + " is passed!")
    else: 
        print(testNumber + " is not passed!")

pattern = r"(?P<X>[a-zA-Z]*)(?P<Y>_[a-zA-Z]*)"
test(pattern, "Hello_World", "test1", "HelloWorld")
test(pattern, "hello_World_my_name_is_Zamira", "test2", "HelloWorldMyNameIsZamira")
"""result = re.search(pattern, s)
if result:
    print(result['X'].capitalize())
else:
    print('not found!')"""