#lee tres números 
numero1 = int(input("Ingresa el primer número:"))
numero2 = int(input("Ingresa el segundo número:"))
numero3 = int(input("Ingresa el tercer número:"))

#asumimos temporalmente que el primer número
# Es mas grande 
# lo vamos a verificar pronto

nmasGrande = numero1

#comprobamos si el segundo número es más grande 
#que el mayor número actual
#actualiza el número más grande si es necesario

if numero2 > nmasGrande:
    nmasGrande = numero2

#comprobamos si el tercer número es más grande que 
# el mayor numero actual 
#actualiza el número más grande si es necesario

if numero3 > nmasGrande:
    nmasGrande = numero3

#imprimir el resultado
print("El número más grande es:", nmasGrande)