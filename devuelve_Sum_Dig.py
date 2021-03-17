#escriba una funcion que suma(n) que entregue la suma de las cifras de un
# número dado n. Con esta funcion escriba un programa que genere 10 números
#aleatorios entre 1 y 100 y encuentre cual de ellos tiene la mayor suma de 
#sus cifras.

from random import randint

#Devuelve la suma de los digitos 

def suma(n):
    digitos = [int (d) for d in str(n)]
    suma = sum(digitos)
    return suma

# Genera una lista de longitud n con números alatorios entre 1 y 100

def generarNumeros(n):
    numeros = []
    for i in range(n):
        numeros.append(randint(1,100))
    return numeros

# Crea una lista con 10 números aleatorios 

lista = generarNumeros(10)
print("Lista generada: \n", lista)

# Hace la funcion 'suma' para cada elemento de la lista 

sumas = [suma(n) for n in lista]
print("lista de la suma de los digitos: \n", sumas)

# Obtiene el número mayor de la lista 

maximo = max(sumas)
print("Número mayor: \n", maximo)

