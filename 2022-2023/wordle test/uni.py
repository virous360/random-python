from functools import wraps
import time
import os
import json

#LOGS
DEBUG : bool = False
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
        start :float = time.perf_counter()
        ret = func(*args, **kwargs)
        end : float = time.perf_counter()
        print(f"{func.__name__} took {end-start} seconds to run")
        return ret
    return wrap
def cache_me(func):
    cache : dict = {}
    @wraps(func)
    def wrap(*args,**kwargs):
        if args not in cache:
            cache[args] = func(*args,**kwargs)
        return cache[args]
    return wrap

#classes
no_clear_extensions :list = ["json"]
class raw_file():
    def __init__(self,name:str) -> None:
        self.__name__ :str = name
        extension : str=  name.split(".")[-1]
        try:
            log("testing for file presence")
            self.read()
        except:
            log(f"no file with name {self.__name__}... creating a new one")
            self.__create()
        if extension in no_clear_extensions:
            log(f"skipping clear file : {extension} detected")
            return 
        else :
            self.__create()
    def __create(self) -> None:
        self.f = open(self.__name__,"w")
        self.f.write("")
        self.close()
        log("created file object of name "+self.__name__)
    def read(self) -> str:
        self.__open("r")
        a = str(self.f.read())
        log("read all of file : "+self.__name__)
        self.close()
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
        log("closed file      : "+self.__name__)
    def __open(self,mode:str) -> None:
        self.f = open(self.__name__,mode)
        log("opened file      : "+self.__name__)
    def write(self, string : str) -> None:
        self.__open("w")
        a = self.f.write(string)
        self.close()
    def __enter__(self):
        log(f"opening file... {self.__name__}")
        return self
    def __exit__(self, type_error,value_error,exception_traceback):
        log(f"exiting .... {self.__name__}")
        if type_error is not None :
            log(f"type error : {type_error}")
        elif value_error is not None :
            log(f"value error : {value_error}")
        elif exception_traceback is not None :
            log(f"exception traceback error : {exception_traceback}")

class json_file():
    def __init__(self,name:str) -> None:
        self.name = name+".json"
        self.__file = raw_file(self.name)
    def read(self) -> dict[str,list]:
        y = {}
        x : list = json.loads(self.__file.read())
        var_names : list = x.pop(0)
        for i in var_names:
            y[i] = x[0][var_names.index(i)]
        return y
    def write(self,x,varname:str):
        a = json.dumps(([varname],x))
        self.__file.write(a)
    def append(self,x,varname:str):
        r: list = self.raw_read()
        var_names : list = r.pop(0)
        var_names.append(varname)
        r.append(x)
        self.raw_write((var_names,r))
    def raw_append(self,*dic) -> None:
        y = self.read()
        x = json.dumps((y,dic))
        self.__file.write(x)
    def raw_read(self):
        x = json.loads(self.__file.read())
        return x
    def raw_write(self,dic) -> None:
        x = json.dumps(dic)
        self.__file.write(x)


