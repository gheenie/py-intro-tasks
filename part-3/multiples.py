from test_api import test_func as test
# Create the function multiples which accepts an integer. It should return a list of all numbers between 1-100 which are divisible by that number.
# eg. multiples(20) => [20, 40, 60, 80, 100]
# eg. multiples(75) => [75]

def multiples():
    pass

#tests
test.check(multiples(100), [100])
test.check(multiples(99), [99])
test.check(multiples(20), [20, 40, 60, 80, 100])

