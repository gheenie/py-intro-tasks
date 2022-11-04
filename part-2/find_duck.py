from test_api import test_func as test
# Complete the function find_duck which takes a queue of farmyard animals.
# Return the position the duck is at in the queue assuming that the first postion is the animal at the far left of the queue.
# Farmyard animal respect each other's personal space, each animal is one white space away from the one in front.

# eg. find_duck('🦆 🐄 🐖 🐑 🦙') => 1
# eg. find_duck('🐖 🐄 🐖 🐑 🦆 🐖') => 5


def find_duck():
    pass

# tests

def test_finds_lonesome_duck():
    expected = 1
    result = find_duck('🦆')

    assert result == expected

def test_finds_duck_in_the_queue():
    expected = 3
    result = find_duck('🐄 🐖 🦆 🐑 🦙')

    assert result == expected

def test_handles_non_existant_duck():
    expected = -1
    result = find_duck('🐄 🐖 🐑 🦙')

    assert result == expected


