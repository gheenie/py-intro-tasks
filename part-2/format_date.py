# Create the function format_date which takes a date string in the format 'DD MM YYYY'. The date could be separated by . / or whitespace.
# and returns a string in the following format: day date month year
# eg. format_date(21.03.2017) => 'Tuesday 9th February 2017'


def format_date():
    pass

# tests

def test_converts_tiktoks():
    expected = 'Tuesday 21st March 2017'
    result = format_date('21.03.2017')

    assert result == expected

def test_converts_gatsbys():
    expected = 'Sunday 2nd January 1921'
    result = format_date('02 01 1921')

    assert result == expected

def test_converts_millenials():
    expected = 'Wednesday 28th June 1989'
    result = format_date('28/06/1989')

    assert result == expected

def test_outliers():
    expected = 'Tuesday 11th January 2022'
    result = format_date('11/01/2022')
    assert result == expected

    expected = 'Wednesday 12th January 2022'
    result = format_date('12/01/2022')
    assert result == expected
    
    expected = 'Thursday 13th January 2022'
    result = format_date('13.01.22')
    assert result == expected
