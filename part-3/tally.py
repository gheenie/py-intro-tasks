from test_api import test_func as test
# Create the function tally which when given a list, creates at dictionary which counts the occurances of each item.

# eg. tally(['dog', 'pineapple', 'pineapple', 'furby' 'pineapple']) => {'dog: 1, 'pineapple': 3, 'furby':1}


def tally():
    pass





#tests
test.check(tally([]), {})
test.check(tally(['dog']), {'dog':1})
test.check(tally(['dog', 'cat']), {'dog': 1, 'cat':1})
test.check(tally(['dog', 'cat', 'cat', 'cat']), {'dog': 1, 'cat': 3})

