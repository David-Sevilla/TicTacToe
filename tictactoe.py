"""
@author: David Sevilla
"""

import random


def print_board(board):
    #Function that draws the board
    print("")
    for i in board:
        print("".join(i))
        

def did_win(win,score):
    ''' Function that valuates winning conditions
    if there is a winner returns game over is True '''
    game_over = False
    for line in win:
        evaluate = set(score) & set(line)
        if len(evaluate) == 3:
            return True # Game Over
    return game_over #keep playing
    


# Defines winning conditions    
win = []
for i in range(3):
    win += [[x for x in range(1+i,8+i,3)]]
win += [[1,2,3],[4,5,6],[6,7,8],[1,5,9],[7,5,3]]
    

# sets coordinates with numpad
coordinates = {"7": [0,0], "8": [0,2], "9": [0,4], 
               "4": [1,0], "5": [1,2], "6": [1,4], 
               "1": [2,0], "2": [2,2], "3": [2,4]}


    
# Draw a an empty tic tac toe
board = [["___","|","___","|","___"],["___","|","___","|","___"],["   ","|","   ","|", "   "]]
    


# Welcome Message, Who is playing, print empty board
print("Welcome to the game of Tic-Tac-Toe")
p1 = input("Who is player 1?: ")
p2 = input("who is player 2?: ") 

print("\nUse your numpad to play: \nEach number in your numpad corresponds to a coordinate on the TicTacToe board")
print_board(board)


# initialize variables
end = 0
p1_turn = bool(random.getrandbits(1)) # Starting player is randomly chosen
score_p1 = []
score_p2 = []
game_over = False


#Main game, the board only has 9 options (maximum of 9 turns)
while end < 9:
    #assing marks to players
    if p1_turn:
        x = "_X_"
        player = p1
    else: 
        x = "_O_"
        player = p2
    
    # Prompt who's turn it is and ask to make a move
    user_mark = input("It is %s's turn \n%s, where do you want to put your mark?: " % (player,player))
    
    #Compare user input with playable positions
    if user_mark not in coordinates.keys():
        print("It seems like you want to write your mark outside the board \n Try again")
        continue
    else: 
        mark = coordinates[user_mark]
        # Check that the user input has not been played before
        if mark == "_O_" or mark == "_X_":
            print("There is already a mark in this position \n Try another position")
            continue
        else:
            #Mark the board with player's move
            board[mark[0]][mark[1]] = x
            coordinates[user_mark]= x
            
            # keep track of the score and evaluate when the game is over
            if p1_turn:
                score_p1.append(int(user_mark))
                game_over = did_win(win, score_p1)
            else:
                score_p2.append(int(user_mark))
                game_over = did_win(win, score_p2)
                
            print_board(board)
            
            p1_turn = 0b1^p1_turn  #xor is used to toggle turns
    
    # If there is a winner. Display who won
    if game_over:
        print("Game Over:\n%s is the winner!" % player)
        break
    end += 1
    
    # If it is a tie, Display game over message
else:
    print("Game Over:\nThere is no winner")
    
    
    




     