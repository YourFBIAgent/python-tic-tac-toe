# Importing needed modules
import random as rand

# Function used for the introduction message
def introduction():
    print('Hello! Welcome to a simple tic tac toe game made with python!')
    print('The game is simple, place either X or O on a tile by entering the tile number')
    print('Tile numbers go from 1 to 9 going from the top left to the bottom right')
    print('Do you wish to play single-player, multi-player or view the scoreboard?')

# Function used to count the amount of white spaces (non filled spots) on the board
# Used to stop the game once all 9 spots are taken
def whiteSpaceCount(list):
    count = 0
    for i in range(0,9):
        if list[i] == ' ':
            count += 1
    return count

# Function used to get a players name, the name can't be 'Computer' and the same as the other player's name
def getPlayerName(playerNum, avoidName=None):
    while True:
        playerName = input(f'Player {playerNum} enter your name: ')
        if playerName != 'Computer' and playerName != avoidName:
            break
        else:
            print('Name taken! Try again!')
    return playerName

# Outputs the board
def boardOutput(board):
    for i in [0,3,6]:
        print(f' {board[i]} | {board[i+1]} | {board[i+2]}')
        if i != 6:
            print( '------------')

# Checks if the chosen spot is valid
def spotValidation(board, spot):
    try:
        spot = int(spot) - 1
    except:
        return False

    if spot < 0 or spot > 8:
        return False
    elif board[spot] != ' ':
        return False
    return True

# Gets a move from the player and updates the board with it
def getPlayerMove(board, player, sign):
    boardOutput(board)
    while True:
        spot = input(f'{player} choose a spot to place {sign}: ')
        if spotValidation(board, spot):
            spot = int(spot) - 1
            break
        else:
            print('Invalid spot taken!')
    board[spot] = sign

# Gets the index spots of all the spaces on the board with ' ' / are free
def getFreeSpaces(board):
    freeSpaces = []
    for i in range(0,9):
        if board[i] == ' ':
            freeSpaces.extend([i])
    
    return freeSpaces

# Generates a move from the computer
def getComputerMove(board):
    spot = rand.choice(getFreeSpaces(board))
    board[spot] = 'O'

# Functions that decides the winner of the game
def checkWinner(board, sign):
    for i in [0, 3, 6]:
        if sign == board[i] and sign == board[i+1] and sign == board[i+2]:
            return True
    for i in [0, 1, 2]:
        if sign == board[i] and sign == board[i+3] and sign == board[i+6]:
            return True
    if sign == board[0] and sign == board[4] and sign == board[8]:
        return True
    elif sign == board[2] and sign == board[4] and sign == board[6]:
        return True
    return False 