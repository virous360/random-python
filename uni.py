
#perf counter
from functools import wraps
import time
import os
import json

#LOGS
DEBUG = False
def set_debug(b:bool):
    global DEBUG
    DEBUG = b
    clr_logs()
def get_debug():
    return DEBUG
def print_logs():
    if DEBUG == True:
        try:
            f = open("logs", "r")
            print(f.read())
            f.close()
        except:
            print("no log file!")
def clr_logs():
    f = open("logs", "w")
    f.write("")
    f.close()
def del_logs(b:bool):
    if DEBUG == True:
        if b:
            os.system("del logs")
def log(s):
    if DEBUG==True:
        t = time.gmtime()
        f = open("logs", "a")
        f.write(f'log {t[3]}:{t[4]}:{t[5]} : {s} \n')
        f.close()

#wrappers
def timer(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        start = time.perf_counter()
        ret = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end-start} seconds to run")
        return ret
    return wrap
def cache_me(func):
    cache = {}
    @wraps(func)
    def wrap(*args,**kwargs):
        if args not in cache:
            cache[args] = func(*args,**kwargs)
        return cache[args]
    return wrap

#classes
class raw_file():
    def __init__(self,name:str) -> None:
        self.__name__ = name
        self.f = open(name,"w")
        self.f.write("")
        self.close()
        log("created file object of name "+self.__name__)
    def read(self) -> str:
        self.__open("r")
        a = str(self.f.read())
        self.close()
        log("read all of file : "+self.__name__)
        return a
    def append(self,string:str) -> None:
        self.__open("a")
        self.f.write(string)
        self.close()
        log("appended string to file : "+self.__name__)
    def raw_open(self,mode:str) -> None:
        self.f = open(self.__name__, mode)
        log("WARING : opening files in raw mode can be dangerous... plz make sure to close the file after finishing")
    def raw_append(self,string: str) -> None:
        self.f.write(string)
    def close(self) -> None:
        self.f.close()
        log("closed file : "+self.__name__)
    def __open(self,mode:str) -> None:
        self.f = open(self.__name__,mode)
        log("opened file : "+self.__name__)
    def write(self, string : str) -> None:
        self.__open("w")
        a = self.f.write(string)
        self.close()
    def __enter__(self):
        log(f"opening file... {self.name}")
        return self
    def __exit__(self, type_error,value_error,exception_traceback):
        log(f"exiting .... {self.name}")
        if type_error is not None :
            log(f"type error : {type_error}")
        elif value_error is not None :
            log(f"value error : {value_error}")
        elif exception_traceback is not None :
            log(f"exception traceback error : {exception_traceback}")

class json_file():
    def __init__(self,name) -> None:
        self.name = name+".json"
    def read(self):
        x = json.
        return x
    



#https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json