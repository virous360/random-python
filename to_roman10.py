from uni import *
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
dic2 = ["I","V","X","L","C","D","M"]

def __int_to_roman(int1:int):
     roman = []
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
                    m5 = (l[i]-5)*(10**i)
                    roman.append(__int_to_roman(m5))
                    roman.append(dic1[dic1.index(5*(10**i))+1])
                    # roman.append(dic1[dic1.index(m5*(10**i))+1])
          else:
               print("ERROR",eli,l[i],(10**i))
               exit()
     roman.reverse()
     return "".join(roman)

# Main
def all_romans() -> list:
     a = []
     for i in range (1,4000):
          a.append([i,__int_to_roman(i)])
     return a 

def __get_value(string:str) -> int:
     return dic1[dic1.index(string)-1]

def __roman_to_int(roman:str) -> int:
     final = 0
     roman_l = list(roman.upper())
     index = list(range(len(roman_l)))
     for i in roman_l:
          if i not in dic2:
               return
     while len(index)>0:
          current = roman_l[index.pop(0)]
          try:
               next = __get_value(roman_l[roman_l.index(current)+1])
          except:
               next = 0
          current = __get_value(current)
          if current >= next :
               final += current
          else :
               final += next-current
               index.pop(0)
     return final

def roman_converter(arg) -> str|int:
     type_arg = str(type(arg))[:-2][8:]
     if type_arg == "int" : 
          return __int_to_roman(arg)
     elif type_arg == "str":
          return __roman_to_int(arg)
     elif type_arg == "list":
          a = []
          for i in arg:
               a.append(roman_converter(i))
          return a
     else :
          log("error in data type")
