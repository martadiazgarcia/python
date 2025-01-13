#mplementar una función que reciba un numero y devuelva su descomposición en números primos

def descomponer_en_primos(n):
    factores = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factores.append(divisor)
            n //= divisor
        divisor += 1
    return factores
n =int(input("introduce una lista de números por favor: "))
factores_primos = descomponer_en_primos(n)
print(f"Los números primos de {n} son: {factores_primos}")