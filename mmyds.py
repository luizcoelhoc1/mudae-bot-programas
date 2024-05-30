casados = {}
casados = {}
nomefile = "harem.txt"
file1 = ""
while True:
    try:
        file1 = open(nomefile, encoding='utf8', errors='ignore')
        break
    except OSError:    
        print("Digite novamente o nome do arquivo...")
        nomefile = input()

lines = file1.readlines()
for line in lines:
    if "#" not in line:
        
        print(line.split(" · ")[0])


file1.close() 
input()
