from time import sleep
from sys import exit
def S_print(s,e="\n"):
    for char in list(s) : 
        print(char,end="")
        sleep(0.04)
    print(e,end="")
global BOARD 
BOARD = [" "]*9  
def print_board():
    S_print("="*32+"\n"+" "+BOARD[0]+" | "+BOARD[1]+" | "+BOARD[2]+"\n"+"---+---+---"+"\n"+" "+BOARD[3]+" | "+BOARD[4]+" | "+BOARD[5]+"\n"+"---+---+---"+"\n"+" "+BOARD[6]+" | "+BOARD[7]+" | "+BOARD[8]+"\n"+"="*32)
def check_win():
    for i in range(3):
        if (BOARD[i*3] == BOARD[i*3+1] == BOARD[i*3+2] and BOARD[i*3] != " ") or \
            (BOARD[i] == BOARD[i+3] == BOARD[i+6] and BOARD[i] != " "):
            return True
    return (BOARD[0] == BOARD[4] == BOARD[8] and BOARD[0] != " ") or \
        (BOARD[2] == BOARD[4] == BOARD[6] and BOARD[2] != " ") or \
        (" " not in BOARD)
def move():
    while True:
        S_print("player O : ","")
        x = int(input())
        if 1 <= x <= 9:
            x = {7:0,8:1,9:2,4:3,5:4,6:5,1:6,2:7,3:8}[x]
            if BOARD[x] == " ":
                BOARD[x] = "O"
                return x 
        S_print("incorrect input")
def bot_move(to): 
    if BOARD[to] != " ":
        S_print("failed trying to set index "+str(to)+ ": ")
        print_board()
        exit()
    BOARD[to] = "X"
    print_board()
    return to
bot_move(4)    
m2 = move() 
bot_move({0:8,6:2,8:0}.get(m2,6))
m4 = move()
bot_move({0:{1:2,2:1,6:3,7:2}.get(m4,6),1:{2:0}.get(m4,2),2:{0:1,1:0,7:0,8:5}.get(m4,8),3:{2:8}.get(m4,2),5:{2:8}.get(m4,2),6:{0:3,1:8,7:8,8:7}.get(m4,0),7:{2:0}.get(m4,2),8:{1:6,2:5,6:7,7:6}.get(m4,2)}[m2])
if check_win():
    S_print("I won again ;)")
    exit()
m6 = move()
bot_move({0:{1:{5:6}.get(m6,5),2:{7:3}.get(m6,7),6:{5:1}.get(m6,5),7:{6:5}.get(m6,6)}.get(m4,{2:7}.get(m6,2)),1:{3:8}.get(m6,3),2:{0:{7:3}.get(m6,7),3:{7:0}.get(m6,7),5:{0:7}.get(m6,0),8:{3:7}.get(m6,3)}.get(m4,{8:3}.get(m6,8)),6:{0:{5:7}.get(m6,5),1:{5:0}.get(m6,5),7:{0:5}.get(m6,0),8:{1:3}.get(m6,1)}.get(m4,{8:1}.get(m6,8)),7:{3:8}.get(m6,3),8:{1:{2:3}.get(m6,2),2:{3:1}.get(m6,3),6:{1:3}.get(m6,1),7:{2:3}.get(m6,2)}.get(m4,{1:6}.get(m6,1))}.get(m2,{7:0}.get(m6,7)))
if check_win():
    S_print("I won again ;)")
    exit()
move()
BOARD = ["X" if x == " " else x for x in BOARD ]
print_board()
if check_win():
    S_print("I won again ;)")
    exit()
S_print("Draw :(")