from uni import *
import sys
sys.setrecursionlimit(1000)
@cache_me
def fibonacci(n):
    if n == 0 or n == 1 :
        return n
    return fibonacci(n-1) + fibonacci(n-2)

@timer
def doom():
    f = create_file("fibonacci")
    f.raw_open("a")
    for i in range(10001):
        f.raw_append(str(i)+" : "+str(fibonacci(i))+"\n")
    f.close()

doom()