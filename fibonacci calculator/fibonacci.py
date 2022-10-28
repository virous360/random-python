#from uni import *
from functools import wraps
def cache_me(func):
    cache = {}
    @wraps(func)
    def wrap(*args,**kwargs):
        if args not in cache:
            cache[args] = func(*args,**kwargs)
        return cache[args]
    return wrap
class create_file():
    def __init__(self,name:str) -> None:
        self.__name__ = name
        self.f = open(name,"w")
        self.f.write("")
        self.close()
    def read(self) -> list:
        self.__open("r")
        a = self.f.read()
        self.close()
        return a
    def append(self,string:str) -> None:
        self.__open("a")
        self.f.write(string)
        self.close()
    def raw_open(self,mode:str) -> None:
        self.f = open(self.__name__, mode)
    def raw_append(self,string: str) -> None:
        self.f.write(string)
    def close(self) -> None:
        self.f.close()
    def __open(self,mode:str) -> None:
        self.f = open(self.__name__,mode)
    def write(self, string : str) -> None:
        self.__open("w")
        a = self.f.write(string)
        self.close()
import sys
sys.setrecursionlimit(1000)
@cache_me
def fibonacci(n):
    if n == 0 or n == 1 :
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def doom():
    f = create_file("fibonacci")
    f.raw_open("a")
    for i in range(10001):
        f.raw_append(str(i)+" : "+str(fibonacci(i))+"\n")
    f.close()

doom()