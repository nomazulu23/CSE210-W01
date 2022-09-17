print("Welcome to the tic-tac-toe game.\n The game requires two players, Player 1 and Player 2. \n The players will take turns using X's and O's to mark the spaces in the game board with 3 by 3 grid.")
game_count = 0
turn_limit = 5
out_of_turns = False
symbol = ""


def game_board():
    board = [[1 | 2 | 3],
             [4 | 5 | 6],
             [7 | 8 | 9]]
    return (board)


def players():
    choose = input("Do you want to be player 1 or player 2")
    if choose == "player 1":  # need to made my players case sensetive
        player_1 = "X"
        player_2 = "O"
        print("Player 1 uses X and Player 2 uses O")
    else:
        player_2 = "X"
        print("Player 1 uses O and Player 2 uses X")
    return (player_1, player_2)


def playing_game(board, player_1, player_2, game_count):
    if game_count < turn_limit:
        play = player_1
        play = player_2
        print("Next players turn")
    else:
        out_of_turns = True
        print("No more turns, you lose")
