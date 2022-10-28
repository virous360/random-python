
#perf counter
from functools import wraps
import time
import os
DEBUG = False
def set_debug(b:bool):
    global DEBUG
    DEBUG = b
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
    if DEBUG == True:
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

def timer(func):
    wraps(func)
    def wrap(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end-start} seconds to run")
    return wrap