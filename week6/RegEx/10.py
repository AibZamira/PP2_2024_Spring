import re
def S(match_obj):
    return  "_" + match_obj.group('Z').casefold()

def test(pattern, testData, testNumber, expectedResult):
    result = re.sub(pattern, S, testData)
    pattern1 = r"\b^_"
    result = re.sub(pattern1, "", result)
    print(result)
    if result == expectedResult:
        print(testNumber + " is passed!")
    else: 
        print(testNumber + " is not passed!")
        
pattern = r'(?P<Z>[A-Z][a-z]*)'
test(pattern, "HelloWorld", "test1", "hello_world")
test(pattern, "MySuperTestForYou", "test1", "my_super_test_for_you")
test(pattern, "HowToFindTheBasisOfPolynomialsInLinearAlgebra", "test3", "how_to_find_the_basis_of_polynomials_in_linear_algebra")