#Questao 3
# 3. Escreva uma função em Python chamada potencia. Esta função deve obter como argumentos dois números inteiros, A e B, e calcular AB usando multiplicações sucessivas (não use a função de python math.pow) e retornar o resultado da operação. Depois, crie um programa em Python que obtenha dois números inteiros do usuário e indique o resultado de AB usando a função.

def potencia(a,b):
    return a**b

numeros = []
for i in range(1,3):
    numeros.append(int(input(f"Informe o {i}° numero: ")))

print("Resultado da potência:",potencia(numeros[0],numeros[1]))

