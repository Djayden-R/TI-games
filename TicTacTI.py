"""
Tic-Tac-TI

Version: 1.3

Made by:
    DjaydenR
    
Description:
    You know what Tic-Tac-Toe is, if not, you place 3 x's or o's in a diagnal, horizontal, or vertical line, first to do so wins.
    
How to share this game: 
    1. Connect two calculator with a cable.
    2. On both calculators, press [2nd] + [x,t,0,n].
    3. On the sending calculator, choose 2: All-... 
    4. On the receiving calculator, press RECEIVE 
    5. Find the game in the file list.
"""

moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
current_player = "x"
moves_made = 0

winning_moves = [
    [0, 1, 2],  # Row 1
    [3, 4, 5],  # Row 2
    [6, 7, 8],  # Row 3
    [0, 3, 6],  # Column 1
    [1, 4, 7],  # Column 2
    [2, 5, 8],  # Column 3
    [0, 4, 8],  # Diagonal 1
    [2, 4, 6]   # Diagonal 2
]


def ShowBoard():
    print("""{} | {} | {}\n---------\n{} | {} | {}\n---------\n{} | {} | {}""".format(
        moves[0], moves[1], moves[2],
        moves[3], moves[4], moves[5],
        moves[6], moves[7], moves[8]
    ))
    

def UpdateBoard(move, player):
    place = int(move) -1
    if moves[place].isdigit():
        global moves_made
        moves[place] = str(player)
        moves_made += 1
        UpdateCurrentPlayer()
        return True
    else:
        print("Move is not possible")
        return False


def UpdateCurrentPlayer():
    global current_player
    current_player = "x" if current_player == "o" else "x"



def ProcessInput(move):
    try: 
        move = int(move)
        if move < 10 and move > 0:
            Clear()
            return True
        else:
            Clear()
            print("Enter a number between 1 and 9")
            return False
    except ValueError:
        Clear()
        print("Enter a number")
        return False


def CheckWinCondition():
    for combination in winning_moves:
        if moves[combination[0]] == moves[combination[1]] == moves[combination[2]]:
            ShowBoard()
            print("Player", moves[combination[0]],"has won!")
            return True
    if moves_made == 9:
        ShowBoard()
        print("Game has ended in a draw")
        return True


def PlayAgain():
    while True:
        again = input("Would you like to play again?   (0/1): ")
        if again == "1":
            Clear()
            return True
        elif again == "0":
            return False
        else:
            print("Invalid")
    

def ResetGame():
    global moves, current_player, moves_made
    moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    current_player = "x" 
    moves_made = 0


def Clear():
    print("\n" * 3)


def Game():
    while True:
        global current_player
        ShowBoard()
        print("Player {}'s turn:".format(current_player))
        move = input("Give your move: ")
        if ProcessInput(move):
            if UpdateBoard(move, current_player):
                if CheckWinCondition():
                    if PlayAgain():
                        ResetGame()
                    else:
                        break


Clear()
Game()