# Implementar una función que reciba circo cartas de la baraja francesa y devuelva si tiene un poker o no (4 cartas con el mismo número)
def barajaCreate():

    carta1=(input("introduce el número de la carta1 por favor: "))
    carta2=(input("introduce el número de la carta2 por favor: "))
    carta3=(input("introduce el número de la carta3 por favor: "))
    carta4=(input("introduce el número de la carta4 por favor: "))
    carta5=(input("introduce el número de la carta5 por favor: "))

    cartas=(carta1,carta2,carta3,carta4,carta5)

    for carta in cartas:
        if cartas.count(carta)==4:
            return True
        
    return False


baraja=barajaCreate()

print(baraja)