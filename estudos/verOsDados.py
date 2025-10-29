import pandas as pd
# leitura do cvs
df = pd.read_csv("visualizacaodadosavancada/ecommerce_estatistica (2).csv")

# ver os dados

#print(df.head()) #primeiras linhas 
#print(df.tail()) #últimas linhas "vemos se tem diferneças" 
#print(df.info()) #tipos de dados e colunas
print(df.describe())

