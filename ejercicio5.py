#Implementar una representación con tuplas de la baraja francesa

def barajaCreate():

    palos=("corazones","diamantes","tréboles","picas")
    numeros=("as",2,3,4,5,6,7,8,9,10,"Valet","Damme","Roi")

    barajafrancesa = [(i,j) for i in palos for j in numeros]
    return barajafrancesa

baraja=barajaCreate()

print(baraja)