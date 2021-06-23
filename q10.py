#Questao 10
import pandas as pd

# 10. Obtenha, usando requests ou urllib, dentro de seu programa em Python, o csv do link:
try:
    df = pd.read_csv("https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv")
except:
    df = pd.read_csv("arquivos//Winter_Olympics_Medals.csv")

# 10.1. Dentre os seguintes países nórdicos: Suécia, Dinamarca e Noruega, verifique: No século XXI (a partir de 2001), qual foi o maior medalhista de ouro, considerando apenas as seguintes modalidades:
seculo_XXI = df.loc[(df.Year >= 2001) & (df.NOC.isin(["SWE","DNK","NOR"]) & (df.Medal == "Gold"))]

# 10.1.1. Curling
Curling = seculo_XXI.loc[seculo_XXI.Sport == "Curling"].groupby(seculo_XXI.NOC).count()["Medal"]
print(f"\nNo século XXI, o maior medalista de ouro dentre os países selecionados no esporte Curling foi {Curling.idxmax()}")

# 10.1.2. Patinação no gelo (skating)
Skating = seculo_XXI.loc[seculo_XXI.Sport == "Skating"].groupby(seculo_XXI.NOC).count()["Medal"]
print(f"\nNo século XXI, o maior medalista de ouro dentre os países selecionados no esporte Skating foi {Skating.idxmax() if Skating.empty == False else 'nenhum'}")

# 10.1.3. Esqui (skiing)
Skiing = seculo_XXI.loc[seculo_XXI.Sport == "Skiing"].groupby(seculo_XXI.NOC).count()["Medal"]
print(f"\nNo século XXI, o maior medalista de ouro dentre os países selecionados no esporte Skiing foi {Skiing.idxmax()}")

# 10.1.4. Hóquei sobre o gelo (ice hockey)
Hockey = seculo_XXI.loc[seculo_XXI.Sport == "Ice Hockey"].groupby(seculo_XXI.NOC).count()["Medal"]
print(f"\nNo século XXI, o maior medalista de ouro dentre os países selecionados no esporte Ice Hockey foi {Hockey.idxmax()}")

# 10.1.5. Para cada esporte, considere todas as modalidades, tanto no masculino quanto no feminino.
# Sua resposta deve imprimir um relatório mostrando o total de medalhas de cada um dos países e em que esporte, ano, cidade e gênero (masculino ou feminino) cada medalha foi obtida.
relatorio = df.groupby(['NOC','Sport','Year','City','Event gender','Medal']).count()['Event']
print("\nRelatório mostrando o total de medalhas de cada um dos países e em que esporte, ano, cidade e gênero (masculino ou feminino) cada medalha foi obtida.\n",relatorio)
