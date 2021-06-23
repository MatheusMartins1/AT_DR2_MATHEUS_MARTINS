#Questao 13
import requests
from bs4 import BeautifulSoup
import re
from collections import Counter

# 13. Obtenha, usando requests ou urllib, o conteúdo sobre as PyLadies no link http://brasil.pyladies.com/about
html = requests.get("http://brasil.pyladies.com/about")
html.encoding = 'UTF-8'
soup = BeautifulSoup(html.text)

texto = ""
for p in soup.html.body.find_all('p'):
    texto += p.get_text().strip()

texto = ' '.join(texto.lower().split())

# 13.1. Conte todas as palavras no corpo da página, e indique quais palavras apareceram apenas uma vez.
dict_contagem = dict(Counter(texto.split(" "))).items()
contagem = {}
for key, value in dict_contagem:
    if value > 1:
        contagem[key] = value

print("\nConte todas as palavras no corpo da página, e indique quais palavras apareceram apenas uma vez.",contagem)

# 13.2. Conte quantas vezes apareceu a palavra ladies no conteúdo da página
print(f"\nA palavra ladies aparece {len(re.findall('ladies', texto))} vezes no corpo da página e {len(re.findall('ladies', soup.get_text()))} vezes em todo o html")
