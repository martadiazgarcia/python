#Implementar una función que reciba una lista y devuelva la lista inversa de la lista

def inverso():
   lista=(input("introduce una lista de números por favor: "))
   
   for i in lista[::-1]:
   print(i)

inverso()
