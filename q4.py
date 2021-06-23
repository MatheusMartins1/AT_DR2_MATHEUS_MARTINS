#Questao 4
# 4. Escreva um programa em Python que leia um vetor de 5 números inteiros e o apresente na ordem inversa. Imprima o vetor no final. Use listas.
# Exemplo: se a entrada for [4, 3, 5, 1, 2], o resultado deve ser [2, 1, 5, 3, 4].

numeros = input("Informe os numeros a serem inseridos na lista: ")

numeros = list(map(int,numeros.split(',')))

print(f"Os numeros informados são {tuple(numeros[::-1])}")
