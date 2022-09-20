import os

print("Welcome to the tic-tac-toe game.\n The game requires two players, Player 1 and Player 2. \n The players will take turns using X's and O's to mark the spaces in the game board with 3 by 3 grid.")

# Accessing the board, i will use a dictionary to identify position.
position = {1: '1', 2: '2', 3: '3', 4: '4',
            5: '5', 6: '6', 7: '7', 8: '8', 9: '9', }
playing = True
turn = 0
prev_turn = -1
completed = False

# The game board


def game_board(position):

    board = (f"|{position[1]}|{position[2]}|{position[3]}|\n"
             f"|{position[4]}|{position[5]}|{position[6]}|\n"
             f"|{position[7]}|{position[8]}|{position[9]}|")
    print(board)


# game_board(position)

# Alternating numbers with symbols example
#position[1] = "X"
#print("Second Draw:")
# game_board(position)

# Keeping track on whose turn it is when players rotate to play and take turns.
def rotate_turn(turn):
    # used a module operator
    if turn % 2 == 0:
        return "O"
    else:
        return "X"
# Checking who wins vertically, horizontally and diagonally


def winner(positin):
    # Winning horizontally
    if (position[1] == position[2] == position[3])\
            or (position[4] == position[5] == position[6])\
            or (position[7] == position[8] == position[9]):
        return True
    # Winning vertically
    elif (position[1] == position[4] == position[7])\
            or (position[2] == position[5] == position[8])\
            or (position[3] == position[6] == position[9]):
        return True
    # Winning diagonally
    elif (position[1] == position[5] == position[9])\
            or (position[3] == position[5] == position[7]):
        return True

    else:
        False


# Playing the game
while playing:
    # Reset the screen to avoid having multiple boards
    os.system("cls" if os.name == "nt" else "clear")
    game_board(position)
    # if an invalid turn occured, let the player know
    if prev_turn == turn:
        print("Invalid position picked, please select another position.")
    prev_turn = turn
    print("Player" + str((turn % 2) + 1) +
          "'s turn: Pick your position or press q to quit")
    # allow Input from the players
    pick = input()
    if pick == "q":
        playing = False
    # checking if the players picked numbers 1 to 9
    elif str.isdigit(pick) and int(pick) in position:
        # checking if the position picked has been taken
        if not position[int(pick)] in {"X", "O"}:
            # update the game_board
            turn += 1
            position[int(pick)] = rotate_turn(turn)
    # Game end and the winner
    if winner(position):
        playing, completed = False, True
    if turn > 8:
        playing = False

# Printing results
if completed:
    if winner(turn) == "X":
        print("Player 1, Won!")
    else:
        print("Player 2, Won!")
else:
    # Tie
    print("No Winner")

print("Game Over!!!")
