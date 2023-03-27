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
    num_X = 0
    num_O = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X":
                num_X += 1
            if board[i][j] == "O":
                num_O += 1
    if num_X == num_O:
        return "X"
    else:
        return "O"
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_move = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action_move.append((i,j))
    return action_move

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    fill = player(board)
    i,j = action
    if board[i][j] != EMPTY:
        raise Exception("infeasible move")
    new_board[i][j] = fill
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2]) and board[i][0] != EMPTY:
            return board[i][0]
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[i][0] != EMPTY:
            return board[0][j]
    if (board[0][0] == board[1][1] == board[2][2]) and board[0][0] != EMPTY:
        return board[0][0]
    if (board[0][2] == board[1][1] == board[2][0]) and board[0][2] != EMPTY:
        return board[0][2]
    
    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True 

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) == True:
        if winner(board) == "X":
            return 1
        if winner(board) == "O":
            return -1
        if winner(board) == None:
            return 0


def argmax(v):
    ix = 0
    maxV = v[0]
    for i,x in enumerate(v):
        if x > maxV:
            ix, maxV = i, x
    return ix

def argmin(v):
    ix = 0
    minV = v[0]
    for i,x in enumerate(v):
        if x < minV:
            ix, minV = i, x
    return ix
    
def min_value(board):
    if terminal(board):
        return utility(board)
    v = 10
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -10
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v
    
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    X : Max
    O : Min
    """
    if terminal(board):
        return None

    Actions = actions(board)
    turn = player(board)
    v = []
    if turn == X: # Max
        for action in Actions:
            v.append(min_value(result(board, action)))
        return Actions[argmax(v)]
    elif turn == O: # Min
        for action in Actions:
            v.append(max_value(result(board, action)))
        return Actions[argmin(v)]