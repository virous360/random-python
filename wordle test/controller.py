from main import *
from wordler import *
size = 5
get_scope(size)
secret = start(size)
guess_in = give_guess(0)
while guess_in != secret:
    colors = guess(secret,guess_in)
    guess_in = list(guess_in)
    for i in colors:
        if i == "green":
            green(guess_in[colors.index(i)],colors.index(i))
        elif i == "yellow":
            yellow(guess_in[colors.index(i)],colors.index(i))
        else :
            grey(guess_in[colors.index(i)])
    print(colors,guess_in)
    guess_in = give_guess(0)