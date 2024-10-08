import math


def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)


def check_winner(board):
  
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None


def is_board_full(board):
    return all(cell != " " for row in board for cell in row)


def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    
    if winner == "X":  
        return -1
    elif winner == "O": 
        return 1
    elif is_board_full(board):  
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score


def find_best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player_turn = True

    while True:
        print_board(board)
        winner = check_winner(board)
        if winner:
            print(f"{winner} wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        if player_turn:
           
            while True:
                try:
                    row = int(input("Enter the row (0-2): "))
                    col = int(input("Enter the column (0-2): "))
                    if row < 0 or row > 2 or col < 0 or col > 2:
                        print("Invalid input. Please enter values between 0 and 2.")
                        continue
                    if board[row][col] != " ":
                        print("Cell already taken. Try a different one.")
                        continue
                    board[row][col] = "X"
                    player_turn = False
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")
        else:
            # AI's turn
            print("AI's turn...")
            move = find_best_move(board)
            if move:
                board[move[0]][move[1]] = "O"
            else:
                print("Error: No valid moves available for AI.")
            player_turn = True

# Start the game
play_game()
