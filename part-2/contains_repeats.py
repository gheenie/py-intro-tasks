from test_api import test_func as test
# Create the function contains_repeats and returns true if the passed string contains repeat characters, otherwise it returns false.
# eg. contains_repeats('apple') => True
#     contains_repeats('pear') => False


def contains_repeats():
    pass


# tests
test.check(contains_repeats('a'), False)
test.check(contains_repeats('abcde'), False)
test.check(contains_repeats('aaaa'), True)