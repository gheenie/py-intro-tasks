# Create the function fizz_buzz_zip which takes two lists of integers and combines them into one list element from each list between each other (like a zip!)
# If the number is divisible by three, the element should be replaced with the string 'fizz'.
# If the number is divisible by five, the element should be replaced with the string 'buzz'.
# If the number is divisible by three and five, the element should be replace with the string 'fizzbuzz'.

# eg. fizz_buzz_zip([1,3,5,1,2],[4,2,2,1,15]) => [1, 4, 'fizz', 2, 'buzz', 2, 1, 1, 2, 'fizzbuzz']


def fizz_buzz_zip(list_a, list_b):
    long_list, short_list = (list_a, list_b) if len(list_a) >= len(list_b) else (list_b, list_a)
    zipped = []
    for i, item in enumerate(long_list):
        zipped.append(translate_num(item))
        try:
            zipped.append(translate_num(short_list[i]))
        except IndexError:
            pass
    return zipped

def translate_num(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'fizzbuzz'
    if num % 3 == 0:
        return 'fizz'
    if num % 5 == 0:
        return 'buzz'
    return num



#tests
def test_returns_empty_list_when_past_two_empty_lists():
    expected = []
    result = fizz_buzz_zip([],[])

    assert result == expected

def test_inserts_item_from_first_list_into_final_list():
    expected = [1]
    result = fizz_buzz_zip([1],[])

    assert result == expected

def test_inserts_item_from_second_list_only_into_final_list():
    expected = [1]
    result = fizz_buzz_zip([],[1])

    assert result == expected

def test_inserts_item_from_second_list_into_final_list():
    expected = [1, 2]
    result = fizz_buzz_zip([1],[2])

    assert result == expected

def test_lists_are_zipped():
    expected = [1, 2, 1, 2, 1, 2]
    result = fizz_buzz_zip([1, 1, 1],[2, 2, 2])

    assert result == expected

def test_multiples_of_three_are_replaced_by_fizz():
    expected = ['fizz']
    result = fizz_buzz_zip([3],[])

    assert result == expected

def test_multiples_of_five_are_replaced_by_buzz():
    expected = ['buzz']
    result = fizz_buzz_zip([5],[])

    assert result == expected

def test_multiples_of_three_are_replaced_by_fizzbuzz():
    expected = ['fizzbuzz']
    result = fizz_buzz_zip([15],[])

    assert result == expected