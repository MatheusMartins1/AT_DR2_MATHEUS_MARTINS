#Questao 11
import pandas as pd
import datetime

ultimos_10_anos = datetime.datetime.now() - datetime.timedelta(days=(365.25 *10))

# 11. Obtenha, usando requests ou urllib, dentro de seu programa em Python, o csv do link:
try:
    df = pd.read_csv("https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv")
except:
    df = pd.read_csv("arquivos//Video_Games_Sales_as_at_22_Dec_2016.csv")

# Obtenha, dentre os jogos do gênero de ação (Action), tiro (Shooter) e plataforma (Platform):
jogos = df.loc[df.Genre.isin(["Action","Shooter","Platform"])]

# 11.1. Quais são as três marcas que mais publicaram jogos dos três gêneros combinados? Indique também o total de jogos de cada marca.
quantidade_jogos = jogos.groupby(jogos.Publisher).count()["Name"].sort_values(ascending=False).nlargest(3)
print("\nQuais são as três marcas que mais publicaram jogos dos três gêneros combinados? Indique também o total de jogos de cada marca.\n",quantidade_jogos)

# 11.2. Quais são as três marcas que mais venderam os três gêneros combinados? Indique também o total de vendas de cada marca.
maiores_marcas = jogos.groupby(jogos.Publisher).sum()["Global_Sales"].sort_values(ascending=False).nlargest(3)
print("\nQuais são as três marcas que mais venderam os três gêneros combinados? Indique também o total de vendas de cada marca.\n",maiores_marcas)

# 11.3. Qual é a marca com mais publicações em cada um dos gêneros nos últimos dez anos no Japão? Indique também o número total de jogos dela.
publicacoes_japao = jogos.loc[df.Year_of_Release >= 2001].groupby(jogos.Publisher).count()["Name"].sort_values(ascending=False).nlargest(3)
#NÃO É POSSÍVEL CONTAR PUBLICAÇÕES NO JAPÃO - QUESTÃO ANULADA

# 11.4. Qual foi a marca que mais vendeu em cada um desses gêneros nos últimos dez anos, no Japão? Indique também o total de vendas dela.
vendas_japao = jogos.loc[df.Year_of_Release >= ultimos_10_anos.year].groupby(jogos.Publisher).sum()["JP_Sales"].sort_values(ascending=False).nlargest(3)
print("\nQual foi a marca que mais vendeu em cada um desses gêneros nos últimos dez anos, no Japão? Indique também o total de vendas dela.\n",vendas_japao)