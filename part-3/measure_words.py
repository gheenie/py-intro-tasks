from test_api import test_func as test
# Create the function measure_words which takes a string of words separated by
# commas. It should return a dictionary which records the length of each word.
# Each property should be of the form str: int, where the key is in lowercase.
# You can assume the string will not contain duplicate words.
# eg. measure_words('Ficus, Alocasia, Begonia') => {'ficus': 5, 'alocasia': 8, 'begonia':7}


def measure_words():
    pass


#tests
test.check(measure_words(''), {})
test.check(measure_words('hello'), {'hello': 1})
test.check(measure_words('multiple, words, are, fun'), {'multiple': 8, 'words': 5, 'are': 3, 'fun': 3})