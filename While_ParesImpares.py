# programa lee una secuencia de numeros y cuenta cuantos
#números son pares y cuántos son impares, programa termina cuando ingresa cero

numerosImpares = 0
numerosPares = 0

# lee el primer número 
numero = int(input("Introduce un número o escriba 0 para detecer:"))

# 0 termina la ejecución 
while numero != 0:
    # verifica si el número impar
    if numero % 2 == 1:
        # aumentar el contador de numeros impares 
        numerosImpares += 1
    else:
        # aumentar el contador de numeros pares
        numerosPares += 1
    #lee el siguiente número
    numero = int(input("Introduce un número o escriba 0 para detener:"))

    # imprima los numeros impares y los numeros pares
    print("Números impares:", numerosImpares)
    print("Números pares:", numerosPares)

