import gwosc
from pycbc import catalog
#import pandas as pd

#Criar variaveis
data = []
#Obter todos os dados do gwosc
catalogo = find_datasets(type="catalog")
for cat in catalog.Catalog():
    print(cat)

#Verificando todos os eventos
#info = [e, dados["GPS"], dados["UTC"], dados["mass_1"], dados["mass_2"], dados["final_mass"], dados["peak_frequency"]]
#data.append(info)

# Criando config do pandas
#df = pd.DataFrame(data, columns=["Nome da onda", "Data (GPS)", "Data (UTC)", "Massa 1", "Massa 2", "Massa Final", "Frequencia Peak"])
#df.to_excel("ondas gravitacionais gwosc.xlsx", index=False)
print("Arquivo criado com sucesso")