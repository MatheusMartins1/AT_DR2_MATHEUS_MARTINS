#Questao 12
import requests
from bs4 import BeautifulSoup

# 12. Obtenha, usando requests ou urllib, a página HTML
url = "https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html"
html = requests.get(url).text
soup = BeautifulSoup(html)

estrutura = {
0:"Sigla",
1:"Nome",
2:"Capital",
3:"População",
4:"Área"
}

dados = {}
for i in soup.find_all("div","linha"):
    dado = i.text.strip().split('\n')
    dados[dado[0]] = {}
    for a in dado:
        dados[dado[0]][estrutura[dado.index(a)]] = a

# 12.1. Imprima o conteúdo referente apenas à tabela apresentada na página indicada.
print(dados)

# 12.2. Escreva um programa que obtenha do usuário uma sigla do estado da região Centro-Oeste e apresenta suas informações correspondentes na tabela. O resultado deve apresentar apenas o conteúdo, sem formatação. Ou seja, as tags não devem aparecer. Não esqueça de checar se a sigla pertence à região.
uf = str(input("\nInforme a sigla da UF da região Centro-Oeste: ")).upper()

if uf in dados:
    print(dados[uf])
else:
    print("\nA sigla não pertente a região Centro-Oeste")
