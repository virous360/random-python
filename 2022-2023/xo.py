#board
def print_board(board):
    print(" "+board[0]+" | "+board[1]+" | "+board[2])
    print("---+---+---")
    print(" "+board[3]+" | "+board[4]+" | "+board[5])
    print("---+---+---")
    print(" "+board[6]+" | "+board[7]+" | "+board[8])
#index
def move(board,xo):
    while True:
        x = int(input("player "+xo+" (1-9): "))
        if 1 <= x <= 9:
            if board[x-1] == " " :
                board[x-1] = xo
                break
        print("incorrect input")
    return board
#player move
def check_win(board):
    for i in range(3):
        if (board[i*3] == board[i*3+1] == board[i*3+2] and board[i*3] != " ") or \
            (board[i] == board[i+3] == board[i+6] and board[i] != " "):
            return True
    return (board[0] == board[4] == board[8] and board[0] != " ") or \
        (board[2] == board[4] == board[6] and board[2] != " ") or \
        (" " not in board)
board = [" "]*9        
print_board(board)
letter = "O"
while not check_win(board):
    #game
    if letter == "X" :
        letter = "O"
    else:
        letter = "X"
    board = move(board,letter)
    print_board(board)