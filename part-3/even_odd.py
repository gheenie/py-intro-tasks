from test_api import test_func as test
# Create the function even_odd which accepts a list of integers and returns a new list of strings
# describing whether the number in it's postion is odd or even.
# eg. even_odd([5]) => ['odd']
#     even_odd([1,30,21,4,88]) => ['odd', 'even', 'odd', 'even', 'even']

def even_odd():
    pass

#tests
test.check(even_odd([]), [])
test.check(even_odd([1]), ['odd'])
test.check(even_odd([2]), ['even'])
test.check(even_odd([1, 2, 3, 4]), ['odd', 'even', 'odd', 'even'])
