# Create the rock_paper_scissors which takes two players' choices for the game.
# The functions should returns a string indicating which player has won.
# You can assume that player 1's choice will take the first positional argument.
# eg. rock_paper_scissors('rock', 'paper') -> 'player 2 wins!'
#     rock_paper_scissors('scissors', 'paper') -> 'player 1 wins!'

def rock_paper_scissors():
    pass


#tests
def test_draw_scenario():

    assert rock_paper_scissors('rock','rock') == 'draw'
    assert rock_paper_scissors('scissors','scissors') == 'draw'
    assert rock_paper_scissors('paper','paper') == 'draw'

def test_player1_win_scenario():

    assert rock_paper_scissors('rock','scissors') == 'player 1 wins'
    assert rock_paper_scissors('scissors','paper') == 'player 1 wins'
    assert rock_paper_scissors('paper','rock') == 'player 1 wins'

def test_player2_win_scenario():

    assert rock_paper_scissors('rock','paper') == 'player 2 wins'
    assert rock_paper_scissors('paper','scissors') == 'player 2 wins'
    assert rock_paper_scissors('scissors','rock') == 'player 2 wins'




