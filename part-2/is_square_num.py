from test_api import test_func as test
# Write the function is_square_num which returns True if the passed number is considered square, and False if it is not.
# A square number is a number which is the result of a number multiplied by itself.
# eg. is_square_num(9) => True
#     is_square_num(7) => False


def is_square_num():
    pass


#tests
test.check(is_square_num(2), False)
test.check(is_square_num(5), False)
test.check(is_square_num(4), True)
test.check(is_square_num(25), True)