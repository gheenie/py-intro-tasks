from test_api import test_func as test
# Complete function alternate_case which accepts a string word (no whitespace) and alternates the casing of each character, starting with uppercase.
# eg. alternate_case('hello') => 'HeLlO'



def alternate_case(word):
    pass




# tests
test.check(alternate_case('A'), 'A')
test.check(alternate_case('a'), 'A')
test.check(alternate_case('AA'), 'Aa')
test.check(alternate_case('apple'), 'ApPlE')