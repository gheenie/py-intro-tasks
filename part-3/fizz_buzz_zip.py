from test_api import test_func as test
# Create the function fizz_buzz_zip which takes two lists of integers and combines them into one list element from each list between each other (like a zip!)
# If the number is divisible by three, the element should be replaced with the string 'fizz'.
# If the number is divisible by five, the element should be replaced with the string 'buzz'.
# If the number is divisible by three and five, the element should be replace with the string 'fizzbuzz'.

# eg. fizz_buzz_zip([1,3,5,1,2],[4,2,2,1,15]) => [1, 4, 'fizz', 2, 'buzz', 2, 1, 1, 2, 'fizzbuzz']


def fizz_buzz_zip():
    pass

#tests
test.check(fizz_buzz_zip([],[]), [])
test.check(fizz_buzz_zip([1],[]), [1])
test.check(fizz_buzz_zip([1],[2]), [1, 2])
test.check(fizz_buzz_zip(['3'],[]), ['fizz'])
test.check(fizz_buzz_zip(['5'],[]), ['buzz'])
test.check(fizz_buzz_zip(['15'],[]), ['fizzbuzz'])
test.check(fizz_buzz_zip([1, 3, 5, 1, 2],[4, 2, 2, 1, 15]), [1, 4, 'fizz', 2, 'buzz', 2, 1, 1, 2, 'fizzbuzz'])
