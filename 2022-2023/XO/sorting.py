PATH = "\\".join(__file__.split("\\")[:-1])+"\\"
with open(PATH+"GAMES.txt", "r") as f :
    data = f.read().split("\n")
    data = [x.replace("9","") for x in data]
    data.sort()
    sorted = []
    for i in range(5):
        sorted.append([x for x in data if len(x)==i+5 ])
    print(len(sorted[0]))