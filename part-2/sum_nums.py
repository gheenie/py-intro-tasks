from test_api import test_func as test

# Create a function which takes any number of numerical arguments and returns the total.
# eg. sum_nums(1, 2) => 3
#     sum_nums(3, 4, 5, 6) => 18


def sum_nums():
    pass


#tests
test.check(sum_nums(1), 1)
test.check(sum_nums(1, 2), 3)
test.check(sum_nums(-1, 2, 3, 4), 8)