import math
casados = {}
casados = {}
nomefile = "harem.txt"
fileH = ""
while True:
    try:
        fileH = open(nomefile, encoding='utf8', errors='ignore')
        break
    except OSError:    
        print("Digite novamente o nome do arquivo...")
        nomefile = input()
lines1 = fileH.readlines()
fileH.close()

nomefile2 = "ll.txt"
fileL = ""
while True:
    try:
        fileL = open(nomefile2, encoding='utf8', errors='ignore')
        break
    except OSError:    
        print("Digite novamente o nome do arquivo...")
        nomefile = input()
lines2 = fileL.readlines()
fileL.close()


ll = []
mm = []
temp = {}

for line in lines1:
    mm.append(line.replace("\n", ""))
for line in lines2:
    ll.append(line.split(" - ")[0].split(". ")[1])


for lp in ll:
    achou = False
    for immp, mmp in enumerate(mm):
        if lp == mmp:
            temp[lp] = immp
            achou = True
    if not achou:
        temp[lp] = math.inf
print(temp)

orderedLL1 = []
orderedLL2 = []
for vez in range(0, len(ll)):
    for pp, index in temp.items():
        if vez == index:
            orderedLL1.append(pp)
    
for pp, index in temp.items():
    if index == math.inf:
        orderedLL2.append(pp)

orderedLL = orderedLL1 + orderedLL2

print(orderedLL)      


        
    
