from test_api import test_func as test
# Create the rock_paper_scissors which takes two players' choices for the game.
# The functions should returns a string indicating which player has won.
# You can assume that player 1's choice will take the first positional argument.
# eg. rock_paper_scissors('rock', 'paper') -> 'player 2 wins!'
#     rock_paper_scissors('scissors', 'paper') -> 'player 1 wins!'

def rock_paper_scissors():
    pass


#tests
test.check(rock_paper_scissors('rock','rock'), 'draw')
test.check(rock_paper_scissors('scissors','scissors'), 'draw')
test.check(rock_paper_scissors('paper','paper'), 'draw')

test.check(rock_paper_scissors('rock','scissors'), 'player 1 wins')
test.check(rock_paper_scissors('scissors','paper'), 'player 1 wins')
test.check(rock_paper_scissors('paper','rock'), 'player 1 wins')

test.check(rock_paper_scissors('rock','paper'), 'player 2 wins')
test.check(rock_paper_scissors('paper','scissors'), 'player 2 wins')
test.check(rock_paper_scissors('scissors','rock'), 'player 2 wins')

