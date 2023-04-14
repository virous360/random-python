from uni_20 import *
from math import sqrt
from time import perf_counter

primes = [2,3,5]
def save(list:list[int]):
    file = json_file("primes")
    file.write(list)


def isprime(num) -> bool:
    for prime in primes:
        if prime>sqrt(num):
            return True
        elif num%prime==0:
            return False

def main(maxnumber):
    #numbers = [x for x in range(3,maxnumber) if x%2!=0]
    start = perf_counter()
    # primes = [2] + [x for x in range(3,maxnumber,2) if isprime(x)]
    # for x in range(3,maxnumber,2):
    for x in [x for x in range(3,maxnumber,2) if x%3!=0 and x%5!=0]:
        if isprime(x):
            primes.append(x)
    end = perf_counter()
    print(f"time = {end - start}")
    save_list = [int(x) for x in primes]
    save(save_list)

main(10**10)