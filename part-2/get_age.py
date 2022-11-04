# Complete the function get_age which takes a response to the question "how old are you?" and returns the numerical value as an integer.
# You can assume the input will always be string, starting with with the age of the person.
# eg. get_age('15 years old.') => 15


def get_age():
    pass



# tests
def test_parses_single_char_response():
    expected = 9
    result = get_age('9 years old')

    assert result == expected

def test_parses_number_from_sentence():
    expected = 9
    result = get_age('9 years old')

    assert result == expected

def test_parses_two_digit_numbers_from_sentence():
    expected = 27
    result = get_age('27 years old')

    assert result == expected

def test_parses_longer_digit_numbers_from_sentence():
    expected = 101
    result = get_age('101 years old')

    assert result == expected


