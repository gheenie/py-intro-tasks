from test_api import test_func as test
# Create the function contains_digit which takes an integer. It should return a List of all the numbers which contain that numeral between 1-100.
# eg. contains_digit(9) = >[9, 19, 29, 39, 49, 59, 69, 79, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99]
#     contains_digit(50) = >[50]

def contains_digit():
    pass


#tests
test.check(contains_digit(0), [10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
test.check(contains_digit(9), [9, 19, 29, 39, 49, 59, 69, 79, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99])