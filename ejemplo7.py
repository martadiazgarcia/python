#Implementar una función que reciba una lista de tuplas y devuelva un diccionario donde las claves son los primeros elementos de las tuplas y los valores una lista con los segundos elementos

def diccionario():
    tupla1=("Juan",13,1,1995,13)
    tupla2=("Maria",14,1,1995,13)
    tupla3=("Pedro",15,1,1995,13)
   

    midiccionario={tupla1[0]:tupla1[1],tupla2[0]:tupla2[1],tupla3[0]:tupla3[1]}
    print(midiccionario)


diccionario()

