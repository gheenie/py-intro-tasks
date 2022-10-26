from test_api import test_func as test
# Create the function format_date which takes a date string in the format 'DD MM YYYY'. The date could be separated by . / or whitespace.
# and returns a string in the following format: day date month year
# eg. format_date(21.03.2017) => 'Tuesday 9th February 2017'


def format_date():
    pass

# tests
test.check(format_date('21.03.2017'), 'Tuesday 21st March 2017')
test.check(format_date('02 01 1921'), 'Sunday 2nd January 1921')
test.check(format_date('28/06/1989'), 'Wednesday 28th June 1989')
