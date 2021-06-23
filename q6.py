#Questao 6
# 6. Escreva uma função em Python que leia uma tupla contendo números inteiros,
# retorne uma lista contendo somente os números impares
# e uma nova tupla contendo somente os elementos nas posições pares.

numeros = (7,8,9,11,12,47,2,8,16,21,4,3)
impares = [numero for numero in numeros if numero % 2 != 0]
pares = tuple([numero for numero in numeros if numeros.index(numero) % 2 == 0])

print("numeros ímpares: ",impares,"\nelementos nas posições pares:",pares)