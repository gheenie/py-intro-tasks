from test_api import test_func as test
# Create the function is_uppercase which returns a boolean idicating whether each character is uppercase in the passed string
# eg. is_uppercase('BANANA') => True
#     is_uppercase('banana') => False
#     is_uppercase('banAna') => True


def is_uppercase():
    pass


#tests
test.check(is_uppercase('a'), False)
test.check(is_uppercase('A'), True)
test.check(is_uppercase('aardvark'), False)
test.check(is_uppercase('ARTICHOKE'), True)
test.check(is_uppercase('aArdvaRk'), True)