#Questao 2
# 2. Escreva um programa em Python que some todos os números pares de 1 até um dado n, inclusive. O dado n deve ser obtido do usuário. No final, escreva o valor do resultado desta soma.

numero = int(input("Informe o numero: "))
soma_pares = sum([i for i in range(1,numero+1) if i % 2 == 0])

print(f'A soma de número pares entre 1 e {numero} é: {soma_pares}')