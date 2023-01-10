# Create the function extract_vowels which accepts and string returns a string of the vowels present in the passed string.
# The returned vowels should be sorted alphabetically.
# eg. extract_vowels('hello') => 'eo'
#     extract_vowels('greetings everyone') => 'eeeeeio'


def extract_vowels(string):
    extracted_vowels = ''
    VOWELS = {'a','e','i','o','u'}
    for char in string:
        if char in VOWELS:
            extracted_vowels += char
    return extracted_vowels


# tests
def test_returns_empty_string_whn_no_vowels_found():
    expected = ''
    result = extract_vowels('rhythm')

    assert result == expected


def test_returns_single_voweled_str():
    expected = 'a'
    result = extract_vowels('a')

    assert result == expected


def test_returns_muliple_vowels_in_string():
    expected = 'ae'
    result = extract_vowels('apple')

    assert result == expected


def test_antelopes_are_fun():
    expected = 'aeoe'
    result = extract_vowels('antelope')

    assert result == expected
