from test_api import test_func as test
# Create the function extract_vowels which accepts and string returns a string of the vowels present in the passed string.
# The returned vowels should be sorted alphabetically.
# eg. extract_vowels('hello') => 'eo'
#     extract_vowels('greetings everyone') => 'eeeeeio'



def extract_vowels():
    pass


# tests
test.check(extract_vowels('rhythm'), '')
test.check(extract_vowels('a'), 'a')
test.check(extract_vowels('apple'), 'ae')
test.check(extract_vowels('antelope'), 'aeeo')