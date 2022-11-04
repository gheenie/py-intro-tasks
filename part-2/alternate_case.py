# Complete function alternate_case which accepts a string word (no whitespace) and alternates the casing of each character, starting with uppercase.
# eg. alternate_case('hello') => 'HeLlO'



def alternate_case(word):
    pass




# tests

def test_capitalises_first_character():
    expected = "H"
    result = alternate_case("h")

    assert result == expected

def test_lowercases_second_character():
    expected_second_char = "i"
    result = alternate_case("Hi")

    assert result[1] == expected_second_char


def test_alternates_case_of_single_word():
    expected_second_char = "i"
    result = alternate_case("Hi")

    assert result[1] == expected_second_char

def test_ignores_white_spaces():
    expected = "HeLlO wOrLd"
    result = alternate_case("Hello World")

    assert expected == result