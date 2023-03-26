def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("-"*9)
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("-"*9)
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_win(board):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] and board[i] != " ":
            return True
   
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] != " ":
            return True
   
    # Check diagonals
    if board[0] == board[4] == board[8] and board[0] != " ":
        return True
    if board[2] == board[4] == board[6] and board[2] != " ":
        return True
   
    return False

def tic_tac_toe():
    board = [" "]*9
    player = "X"
   
    while True:
        print_board(board)
        print(f"Player {player}'s turn")
        move = int(input("Enter a position (1-9): ")) - 1
       
        if board[move] == " ":
            board[move] = player
        else:
            print("That position is already occupied.")
            continue
       
        if check_win(board):
            print_board(board)
            print(f"Player {player} wins!")
            break
       
        if " " not in board:
            print_board(board)
            print("It's a tie!")
            break
       
        player = "O" if player == "X" else "X"

tic_tac_toe()