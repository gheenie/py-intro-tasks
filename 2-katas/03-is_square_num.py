import math
# Write the function is_square_num which returns True if the passed number is considered square, and False if it is not.
# A square number is a number which is the result of a number multiplied by itself.
# eg. is_square_num(9) => True
#     is_square_num(7) => False


def is_square_num(num):
    return str( math.sqrt(num) ).endswith('.0')


#tests
def test_reports_when_not_square_number():

    assert is_square_num(2) == False
    assert is_square_num(5) == False
    assert is_square_num(12) == False

def test_reports_when_square_number():

    assert is_square_num(1) == True
    assert is_square_num(9) == True
    assert is_square_num(25) == True   
