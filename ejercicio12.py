#· Implementar un generador que reciba un número y devuelva los múltiplos de 3 de ese número
def multiplos(limite):
    num=1
    while num<limite/3:
        yield num*3
        num=num+1
multiplos=multiplos(10)
print(next(multiplos))
print("Aquí podría ir más código...")
print(next(multiplos))
print("Aquí podría ir más código...")
print(next(multiplos))
print(next(multiplos))
print("Aquí podría ir más código...")
print(next(multiplos))
print("Aquí podría ir más código...")
print(next(multiplos))
print(next(multiplos))
print("Aquí podría ir más código...")
print(next(multiplos))
print("Aquí podría ir más código...")
print(next(multiplos))
print(next(multiplos))
print("Aquí podría ir más código...")
print(next(multiplos))
print("Aquí podría ir más código...")
print(next(multiplos))