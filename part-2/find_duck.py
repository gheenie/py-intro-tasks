from test_api import test_func as test
# Complete the function find_duck which takes a queue of farmyard animals.
# Return the position the duck is at in the queue assuming that the first postion is the animal at the far left of the queue.
# Farmyard animal respect each other's personal space, each animal is one white space away from the one in front.

# eg. find_duck('🦆 🐄 🐖 🐑 🦙') => 1
# eg. find_duck('🐖 🐄 🐖 🐑 🦆 🐖') => 5


def find_duck():
    pass

# tests
test.check(find_duck('🦆'), 1)
test.check(find_duck('🐄 🐖 🦆 🐑 🦙'), 3)
test.check(find_duck('🐄 🐖 🐑 🦙'), -1)

