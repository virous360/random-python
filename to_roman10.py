from time import sleep
from uni import *
clr_logs()
log("loaded uni.py... starting script : "+str(__file__).split("\\")[-1])
dic1 = [
     1,"I",
     5,"V",
     10,"X",
     50,"L",
     100,"C",
     500,"D",
     1000,"M",
]
dic = [
     4,"IV",
     9,"IX",
     40,"XL",
     90,"XC",
     400,"CD",
     900,"CM"
]


def to_roman(int1:int):
     roman = []
     log("started function to_roman")
     if 3999 < int1 or int1 < 1:
          log("dec must be between 1 and 3999. given "+str(int1))
     l = [int(x) for x in str(int1)]
     l.reverse()
     for i in range(len(l)):
          eli = l[i]*(10**i)
          if eli in dic:
               ind = dic.index(eli)
               roman.append(dic[ind+1])
          elif eli in dic1 :
               roman.append(dic1[dic1.index(eli)+1])
          elif 10**i in dic1:
               if l[i] < 5:
                    roman.append(dic1[dic1.index((10**i))+1]*l[i])
               else :
                    l[i] = l[i]-5*(10**i)
                    roman.append(dic1[dic1.index((10**i))+1]*l[i])
                    roman.append(dic1[dic1.index((5)*(10**i))+1])
          else:
               print("ERROR",eli,l[i],(10**i))
               exit()
     roman.reverse()
     return "".join(roman)

# Main
@timer
def all_roman():
     f = open("roman_numbers", "w")
     f.write("")
     f.close()
     f = open("roman_numbers", "a")
     for i in range (1,4000):
          f.write(str(i)+" : "+to_roman(i)+"\n")
     f.close()


all_roman()
log("EOF")
log("printing file contents")
print_logs()