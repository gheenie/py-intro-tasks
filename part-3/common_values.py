from test_api import test_func as test
# Create the function common_values which returns a set of values present in the two passed lists.
# eg.  common_values([1, 4, 'dog'],['dog', False, 2, 1]) => {1, 'dog'}


def common_values():
    pass


#tests
test.check(common_values([],[]), set())
test.check(common_values(['a']['a']), {'a'})
test.check(common_values(['a']['a','b']), {'a'})
test.check(common_values([1, 4, 'dog'],['dog', False, 2, 1]), {1, 'dog'})