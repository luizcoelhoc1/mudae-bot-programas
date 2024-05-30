x = input()
qntPlayers = 5
minimo = 70
vezes = 1
while x != "x":
    x = float(x)
    x = x * vezes
    minimo = minimo * vezes
    print ((x - minimo)/(1-(1/qntPlayers)) + minimo)
    x = input()

