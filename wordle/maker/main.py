from random import randint, seed
from uni_20 import *

def main(length) -> str:
    f = json_file("bettercleaned").read()
    game_length = str(length)
    words = f[game_length]
    if words == []:
        print("no possible solutions...")
        exit()
    rand1 = randint(1,len(words))-1
    rand2 = randint(1,len(words))-1
    super_rand = abs( rand1 - rand2 ) 
    return words[super_rand]

def guess(secret:str ,guess : str) -> list[str]:#["green", "yellow", "gray"] of len(guess)
    secret_list = list(secret)
    guess_list = list(guess)
    the_return = []
    if len(secret) != len(guess):
        print("guess size wrong", secret,guess)
        return []
    # IS GREEN ?
    for i in range(len(guess_list)):
        if guess_list[i] == secret_list[i]:
            the_return.append("green")
        elif guess_list[i] in secret_list:
            the_return.append("yellow")
        else:
            the_return.append("grey")
    
    return the_return

def game():
    tries = 4
    size = 5 
    secret = main(size)
    while tries >= 0:
        guess_input = input("guess "+str(tries+1)+ " : ")
        if guess_input == secret:
            print("you win")
            return
        print(guess(secret,guess_input))
        tries -= 1

game()