from test_api import test_func as test
# Complete the function get_age which takes a response to the question "how old are you?" and returns the numerical value as an integer.
# You can assume the input will always be string, starting with with the age of the person.
# eg. get_age('15 years old.') => 15




def get_age():
    pass


# tests
test.check(get_age('9 years old'), 9)
test.check(get_age('27 years old'), 27)
test.check(get_age('101 years old'), 101)

