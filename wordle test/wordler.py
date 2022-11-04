from random import randint
from uni_20 import *
set_debug(True)
all_words : list[list[str]] = json_file("cleaned").raw_read() # [ [1], [2], ...]
spec_words : list[list[str]] = json_file("wordle_specials").raw_read() # [ [1], [2], ...]
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'y', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'z']

def test_chr(char : str):
    char = char.lower()
    if char not in alpha :
        print("char not valid")
        exit()
def get_scope_words(wordle_length):
    if 31 < wordle_length or wordle_length <= 0:
        log("wordle length error")
        exit()
    scope_words : list [str]= all_words[wordle_length - 1]
    scope_special_words : list[str] = spec_words[wordle_length -1]
    return [scope_words,scope_special_words]
def remove_letter(w : list[str], char : str):
    test_chr(char)
    return [word for word in w if char not in list(word)]
def green_letter(w : list[str], char : str, index: int):
    test_chr(char)
    # new_w = [word for word in w if char in list(word)[index]]
    # for word in w : 
    #     if char in list(word)[index] :
    #         new_w.append(word)
    return [word for word in w if char in list(word)[index]]
def yellow_letter(w : list[str], char : str, index: int):
    test_chr(char)
    new_w = []
    for word in w : 
        if char in list(word):
            if char not in list(word)[index] :
                new_w.append(word)
    return new_w
    


def solve_manual():
    size = int(input("size :"))
    a = get_scope_words(size)
    w = a[0]
    s = a[1]
    is_exit = False
    while not is_exit:
        inp = int(input("1.remove\n2.yellow\n3.green\n4.show list\n5.exit\n:"))
        if inp == 1 : 
            char = input("chr to remove :")
            w = remove_letter(w,char)
            s = remove_letter(s,char)
        elif inp == 2 : 
            char = input("yellow chr to remove :")
            index = int(input("yellow index (start:0):"))
            w = yellow_letter(w,char,index)
            s = yellow_letter(s,char,index)
        elif inp == 3 : 
            char = input("green chr :")
            index = int(input("green index (start:0):"))
            w = green_letter(w,char,index)
            s = green_letter(s,char,index)
        elif inp == 5 :
            is_exit = True
        elif inp == 4 : 
            inp = int(input("1.all words\n2.specials\n:"))
            if inp == 1:
                print(w)
                print(len(w))
            elif inp == 2:
                print(s)
                print(len(s))

def get_scope(size):
    global w,s
    a = get_scope_words(size)
    w = a[0]
    s = a[1]
def give_guess(overrid):
    if len(s) != 0 and overrid != 1:
        return s[randint(0,len(s)-1)]
    else:
        return w[randint(0,len(w)-1)]
def grey(chr):
    global w,s
    w = remove_letter(w,chr)
    s = remove_letter(s,chr)
def green(chr,index):
    global w,s
    w = green_letter(w,chr,index)
    s = green_letter(s,chr,index)
def yellow(chr,index):
    global w,s
    w = yellow_letter(w,chr,index)
    s = yellow_letter(s,chr,index)