import math
sqrt = math.sqrt
import json
from uni_20 import *
with open("primes_init.json","r") as file:
    primes_predifined = json.load(file)

def save(list:list[int]):
    file = json_file("primes")
    file.write(list)

def isprime(num) -> bool:
    sqrnum = sqrt(num)
    for prime in primes_predifined:
        if prime > sqrnum:
            return True
        elif num%prime==0:
            return False


def main():
    maxnumber = int("9"*8)
    x = 9999991 # < 10e5
    final = []
    #limit = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 = 10e615
    range_list = range(x,maxnumber,2)
    print("range returned with list")
    range_list = [x for x in range_list if x%3!=0 and x%5!=0 and x%7!=0 and x%11!=0 and x%13!=0 and x%17!=0 and x%19!=0 and x%23!=0]
    print("created the list")
    for x in range_list:
        if isprime(x):
            primes_predifined.append(x)
            final.append(x)
            print(f"found prime : {x}")
    return final
f = main()
save_list = [int(x) for x in f]
save(save_list)
print(f)