#Questao 1
# 1. Escreva um programa em Python que leia uma tupla contendo 3 números inteiros, (n1, n2, n3) e os imprima em ordem crescente.

print("Digite 3 números conforme exemplo: (n1, n2, n3)")
numeros = tuple(str(input("Informe os 3 numeros ")).split(","))

numeros = [int(i) for i in numeros]
numeros.sort(reverse=False)

print(f"Os numeros informados são {tuple(numeros)}")
