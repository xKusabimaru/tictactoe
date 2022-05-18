"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    v = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                v+=1

    if v % 2 == 0:
        return "O"
    else:
        return "X"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    actionSet = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                actionSet.add((i,j))

    return actionSet


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    newBoard = copy.deepcopy(board)
    newBoard[action[0]][action[1]] = player(newBoard)
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    if board[0][0] == board[0][1] == board[0][2]:
        return board[0][0]

    elif board[1][0] == board[1][1] == board[1][2]:
        return board[1][0]

    elif board[2][0] == board[2][1] == board[2][2]:
        return board[2][0]

    elif board[0][0] == board[1][0] == board[2][0]:
        return board[0][0]

    elif board[0][2] == board[1][2] == board[2][2]:
        return board[0][2]

    elif board[0][1] == board[1][1] == board[2][1]:
        return board[0][1]

    # elif board[0][2] == board[1][2] == board[2][2]:
    #     return board[0][2]

    elif board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    elif board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) == None:
        for i in range(3):
            for j in range(3):
                if board[i][j] == None:
                    return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == "X":
        return 1

    elif winner(board) == "O":
        return -1

    else:
        return 0


def maxValue(board):

    if terminal(board):
        return utility(board)

    v = float("-inf")

    for action in actions(board):
        v = max(v, minValue(result(board, action)))

    return v


def minValue(board):

    if terminal(board):
        return utility(board)

    v = float("inf")

    for action in actions(board):
        v = min(v, maxValue(result(board, action)))

    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    if player(board) == "X":
        v = float("-inf")
        for action in actions(board):
            tmp = minValue(result(board, action))
            if v < tmp:
                v = tmp
                move = action

    else:
        v = float("inf")
        for action in actions(board):
            tmp = maxValue(result(board, action))
            if v > tmp:
                v = tmp
                move = action

    return move