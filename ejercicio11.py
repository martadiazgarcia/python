#· Implementar un generador que devuelva los números pares
def generaPares(limite):
    num=1
    while num<limite:
        yield num*2
        num=num+1
devuelvePares=generaPares(10)
print(next(devuelvePares))
print("Aquí podría ir más código...")
print(next(devuelvePares))
print("Aquí podría ir más código...")
print(next(devuelvePares))