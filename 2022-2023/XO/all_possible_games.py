# LETS DIEEEEEEEE
# Ali Naim 
# started 22-12-2023
from os import system
# board = ["-"]*9
PATH = "\\".join(__file__.split("\\")[:-1])+"\\"

#board for debugging 
def print_board(board):
    print(" "+board[0]+" | "+board[1]+" | "+board[2])
    print("---+---+---")
    print(" "+board[3]+" | "+board[4]+" | "+board[5])
    print("---+---+---")
    print(" "+board[6]+" | "+board[7]+" | "+board[8])
def check_win(board):
    for i in range(3):
        if (board[i*3] == board[i*3+1] == board[i*3+2] and board[i*3] != "-") :
            return (True,board[i*3]) #===
        elif (board[i] == board[i+3] == board[i+6] and board[i] != "-"):
            return (True,board[i]) #|||
    if (board[0] == board[4] == board[8] and board[0] != "-"):
        return (True,board[0]) #\\\
    elif (board[2] == board[4] == board[6] and board[2] != "-"):
        return (True,board[2]) #///
    elif ("-" not in board):
        return (False,"DRAW")
    return (False,"-")
def save(i1=9,i2=9,i3=9,i4=9,i5=9,i6=9,i7=9,i8=9,i9=9):
    return str(i1)+str(i2)+str(i3)+str(i4)+str(i5)+str(i6)+str(i7)+str(i8)+str(i9)
def add_to_file(b,s):
    with open(PATH+"GAMES.txt", "a") as f :
        f.write(s+"\n")
def P(b,s) :
    # print("="*13)
    # print_board(b)
    # print("="*13)
    # print(s)
    # print("="*13)
    add_to_file(b,s)
def PP(b,s) :
    print("="*13)
    print_board(b)
    print("="*13)
    print(s)
    print("="*13)
draws = []
computed = 0
#BOT = X (starts first)
# print_board(board)
for i1 in range(9):
    # print(computed)
    board = ["-"]*9
    board[i1]="X" #MOVE 1 
    for i2 in range(9):
        board2 = list(board)
        if board2[i2] == "-":
            board2[i2] = "O" #MOVE 2
            for i3 in range(9):
                board3 = list(board2)
                if board3[i3] == "-":
                    board3[i3] = "X" #MOVE 3
                    for i4 in range(9):
                        board4 = list(board3)
                        if board4[i4] == "-":
                            board4[i4] = "O" #MOVE 4
                            for i5 in range(9):
                                WIN = False
                                board5 = list(board4)
                                if board5[i5] == "-":
                                    board5[i5] = "X" #MOVE 5
                                    if check_win(board5)[0] :
                                        P(board5,save(i1,i2,i3,i4,i5))
                                        WIN = True
                                        computed +=1
                                    for i6 in range(9):
                                        if WIN : 
                                            WIN = False
                                            break
                                        board6 = list(board5)
                                        if board6[i6] == "-":
                                            board6[i6] = "O" #MOVE 6
                                            if check_win(board6)[0] :
                                                P(board6,save(i1,i2,i3,i4,i5,i6))
                                                WIN = True
                                                computed +=1
                                            for i7 in range(9):
                                                if WIN : 
                                                    WIN = False
                                                    break
                                                board7 = list(board6)
                                                if board7[i7] == "-":
                                                    board7[i7] = "X" #MOVE 7
                                                    if check_win(board7)[0] :
                                                        P(board7,save(i1,i2,i3,i4,i5,i6,i7))
                                                        WIN = True
                                                        computed +=1
                                                    for i8 in range(9):
                                                        if WIN : 
                                                            WIN = False
                                                            break
                                                        board8 = list(board7)
                                                        if board8[i8] == "-":
                                                            board8[i8] = "O" #MOVE 8
                                                            if check_win(board8)[0] :
                                                                P(board8,save(i1,i2,i3,i4,i5,i6,i7,i8))
                                                                WIN = True
                                                                computed +=1
                                                            else :
                                                                i9 = board8.index("-")
                                                                board8[i9] = "X" #MOVE 9
                                                                if check_win(board8)[0] :
                                                                    P(board8,save(i1,i2,i3,i4,i5,i6,i7,i8,i9))
                                                                    computed +=1
                                                                else : 
                                                                    draws.append(save(i1,i2,i3,i4,i5,i6,i7,i8,i9)) 
                                                                    PP(board8,save(i1,i2,i3,i4,i5,i6,i7,i8,i9))
                                                                    
                                                                    # PP(board9,save(i1,i2,i3,i4,i5,i6,i7,i8,i9))
                                                                    

with open(PATH+"DRAWS.txt", "w") as f :
    f.write("\n".join(draws))
    
print(computed)