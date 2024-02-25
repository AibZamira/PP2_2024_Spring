import re
"""
def S(match_obj):
    return match_obj.group('X') + " " + match_obj.group('Y')

def test(pattern, testData, testNumber, expectedResult):
    result = re.sub(pattern, S, testData)
    print(result)
    if result == expectedResult:
        print(testNumber + " is passed!")
    else: 
        print(testNumber + " is not passed!")"""

s = "HelloWorld"

pattern = r'(?P<X>[a-zA-Z])(?P<Y>[A-Z])'
# test(pattern, "HelloWorld", "test1", "Hello World")
result = re.search(pattern, s)
if result:
    print(result['X'])
    print(result['Y'])
else:
    print('not found!')