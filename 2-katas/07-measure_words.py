# Create the function measure_words which takes a string of words separated by
# commas. It should return a dictionary which records the length of each word.
# Each property should be of the form str: int, where the key is in lowercase.
# You can assume the string will not contain duplicate words.
# eg. measure_words('Ficus, Alocasia, Begonia') => {'ficus': 5, 'alocasia': 8, 'begonia':7}


def measure_words(sentence):
    words = sentence.split(', ')
    
    if words == ['']:
        return {}
    
    return {word: len(word) for word in words}


#tests
def test_returns_empty_dict_when_passed_empty_str():
    expected = {}
    result = measure_words('')

    assert result == expected

def test_assigns_property_for_single_word():
    expected = {'hello': 5}
    result = measure_words('hello')

    assert result == expected

def test_assigns_property_for_multiple_words():
    expected = {'multiple': 8, 'words': 5, 'are': 3, 'fun': 3}
    result = measure_words('multiple, words, are, fun')

    assert result == expected
