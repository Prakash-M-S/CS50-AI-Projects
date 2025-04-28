import math
import copy
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
    o_count=0
    x_count=0
    for i in board:
        for j in i:
            if j=="X":
                x_count+=1
            elif j=="O":
                o_count+=1 
    if x_count>o_count:
        return O
    return X

def actions(board):
    action=set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] is EMPTY:
                action.add((i,j))
    return action
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    who = player(board)
    new_board= copy.deepcopy(board)
    new_board[action[0]][action[1]]= who
    return new_board
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    if(board[0][0]==board[1][1]==board[2][2] and board[0][0]!=EMPTY):
        return board[1][1]

    if(board[2][0]==board[1][1]==board[0][2] and board[2][0]!=EMPTY):
        return board[1][1]
    
    return None
    
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    
    # Check if board is full
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True
  
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    
    """
    win=winner(board)
    if(win==X):
        return 1
    elif(win==O):
        return -1
    else:
        return 0
    
    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    current_player = player(board)
    
    if current_player == X:
        # Maximizing player
        best_score = float('-inf')
        best_action = None
        for action in actions(board):
            score = manimizing(result(board, action))
            if score > best_score:
                best_score = score
                best_action = action
    else:
        # Minimizing player
        best_score = float('inf')
        best_action = None
        for action in actions(board):
            score = maximizing(result(board, action))
            if score < best_score:
                best_score = score
                best_action = action
    
    return best_action

def maximizing(board):
    """
    Calculates the score for the maximizing player (X).
    """
    if terminal(board):
        return utility(board)
    
    best_score = float('-inf')
    for action in actions(board):
        best_score = max(best_score, manimizing(result(board, action)))
    return best_score

def manimizing(board):
    """
    Calculates the score for the minimizing player (O).
    """
    if terminal(board):
        return utility(board)
    
    best_score = float('inf')
    for action in actions(board):
        best_score = min(best_score, maximizing(result(board, action)))
    return best_score               
        
    
    
      
    