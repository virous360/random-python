# for the TI-83 premium python ce

cache = {0:0,1:1}
def fibonacci(n):
    if n in cache :
        return cache[n]
    else :
        return fibonacci(n-1) + fibonacci(n-2)

a = int(input("int : "))
print("fibonacci : "+str(fibonacci(a)))