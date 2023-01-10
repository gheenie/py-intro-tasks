# Create the function is_uppercase which returns a boolean idicating whether each character is uppercase in the passed string
# eg. is_uppercase('BANANA') => True
#     is_uppercase('banana') => False
#     is_uppercase('banAna') => True


def is_uppercase():
    pass


#tests
def test_detects_single_char_is_lowercase():
    expected = False
    result = is_uppercase('a')

    assert result == expected

def test_detects_single_char_is_uppercase():
    expected = True
    result = is_uppercase('A')

    assert result == expected

def test_detects_multi_char_is_uppercase():
    expected = True
    result = is_uppercase('ARTICHOKE')

    assert result == expected

def test_works_with_mixed_casing():
    expected = True
    result = is_uppercase('aArdvaRk')

    assert result == expected
