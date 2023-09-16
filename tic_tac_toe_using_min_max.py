# Tic-Tac-Toe board represented as a list
# Indices 1-9 represent the positions on the board
# 'X' for the player, 'O' for the computer, and ' ' for empty cells
board = [' ' for _ in range(10)]

# Function to draw the board
def draw_board(board):
    print(f"{board[1]} | {board[2]} | {board[3]}")
    print("--|---|--")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print("--|---|--")
    print(f"{board[7]} | {board[8]} | {board[9]}")

# Function to check if the board is full
def is_board_full(board):
    return ' ' not in board[1:]

# Function to check if the current player has won
def check_win(board, player):
    win_conditions = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to evaluate the board for minimax algorithm
def evaluate_board(board):
    if check_win(board, 'O'):
        return 1
    elif check_win(board, 'X'):
        return -1
    elif is_board_full(board):
        return 0
    else:
        return None

# Minimax algorithm implementation
def minimax(board, depth, maximizing_player):
    if depth == 0 or is_board_full(board):
        return evaluate_board(board)

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(1, 10):
            if board[i] == ' ':
                board[i] = 'O'
                eval = minimax(board, depth - 1, False)
                board[i] = ' '
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(1, 10):
            if board[i] == ' ':
                board[i] = 'X'
                eval = minimax(board, depth - 1, True)
                board[i] = ' '
                min_eval = min(min_eval, eval)
        return min_eval

# Function to find the best move for the computer player
def find_best_move(board):
    best_move = None
    best_eval = float('-inf')
    for i in range(1, 10):
        if board[i] == ' ':
            board[i] = 'O'
            eval = minimax(board, 9, False)
            board[i] = ' '
            if eval > best_eval:
                best_eval = eval
                best_move = i
    return best_move

# Main game loop
while True:
    draw_board(board)
    
    print("If u need to start enter 0 otherwise 1: ")
    int c = int(input())
    
    if(c == 0):
      # Player's turn
      move = int(input("Enter your move (1-9): "))
      if board[move] == ' ':
        board[move] = 'X'
      else:
        print("Invalid move! Try again.")
        continue

      if check_win(board, 'X'):
        draw_board(board)
        print("Congratulations! You win!")
        break

      if is_board_full(board):
        draw_board(board)
        print("It's a draw!")
        break

      # Computer's turn
      best_move = find_best_move(board)
      board[best_move] = 'O'

      if check_win(board, 'O'):
        draw_board(board)
        print("Sorry, you lose!")
        break
    else:
      # Computer's turn
      best_move = find_best_move(board)
      board[best_move] = 'O'

      if check_win(board, 'O'):
        draw_board(board)
        print("you Win!")
        break

      if check_win(board, 'X'):
        draw_board(board)
        print("You Lose!")
        break

      if is_board_full(board):
        draw_board(board)
        print("It's a draw!")
        break

      # Player's turn
      move = int(input("Enter your move (1-9): "))
      if board[move] == ' ':
        board[move] = 'X'
      else:
        print("Invalid move! Try again.")
        continue  
