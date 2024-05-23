from time import sleep
def S_print(s,e=""):
    for char in list(s) : 
        print(char,end="")
        sleep(0.1)
    print(e,end="")

S_print("hello world!")