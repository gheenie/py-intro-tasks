from test_api import test_func as test
# Complete the function get_length which returns the length of any passed string, ignoring whitespace characters.
# eg. get_length('hello there!') => 11


def get_length():
    pass


# tests
test.check(get_length('a'), 1)
test.check(get_length('tofu'), 4)
test.check(get_length('Linda McCartney sausages'), 22)

