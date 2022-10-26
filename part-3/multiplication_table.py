from test_api import test_func as test
# Create the function multiplication_table. It should accept an integer and generate a dictionary representing it's multiplication table for up to 5.
# The key should be a tuple representing the two numbers being multiplied, the value should be product of those two numbers.
# eg. multiplication_table(5) => {(1, 5): 5, (2, 5): 10, (3, 5): 15, (4, 5):20, (5, 5): 25}




def multiplication_table():
    pass

#tests
test.check(multiplication_table(1), {(1, 1): 1, (2, 1): 2, (3, 1): 3, (4, 1): 4, (5, 1): 5})
test.check(multiplication_table(5), {(1, 5): 5, (2, 5): 10, (3, 5): 15, (4, 5):20, (5, 5): 25})