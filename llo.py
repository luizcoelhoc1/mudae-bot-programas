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
    if ":revolving_hearts:" in line:
        splitPrincipal = line.split(" => ")
        nomeDonoEDoAnime = splitPrincipal[1].split(" - ")
        dono = nomeDonoEDoAnime[0]
        anime = nomeDonoEDoAnime[1].replace("\n", "")
        if dono not in casados.keys():
            casados[dono] = {}
        if anime not in casados[dono].keys():
            casados[dono][anime] = []

        splitPersonagemRanking = splitPrincipal[0].split(" :revolving_hearts:")
        splitPersonagemRanking = splitPersonagemRanking[0].split(". ")
        ranking = splitPersonagemRanking[0]
        personagem = splitPersonagemRanking[1].replace("\n", "")
        casados[dono][anime].append(personagem)

while True:
    print("digite o nome exato do dono que você quer ver o que ele tem seu")
    for dono in casados:
        print(dono)
    dono = input()
    for anime in casados[dono]:
        print(anime + ":")
        for personagem in casados[dono][anime]:
            print("\t" + personagem.replace("\n", ""))
    
print ()
file1.close() 
