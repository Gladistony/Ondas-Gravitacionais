import gwosc

import pycbc.catalog


c = pycbc.catalog.Catalog(source='gwtc-2')
print(c.names)

#data = []
#Obter todos os dados do gwosc
#for cat in catalog.Catalog():
#    print(cat)

#Verificando todos os eventos
#info = [e, dados["GPS"], dados["UTC"], dados["mass_1"], dados["mass_2"], dados["final_mass"], dados["peak_frequency"]]
#data.append(info)

# Criando config do pandas
#df = pd.DataFrame(data, columns=["Nome da onda", "Data (GPS)", "Data (UTC)", "Massa 1", "Massa 2", "Massa Final", "Frequencia Peak"])
#df.to_excel("ondas gravitacionais gwosc.xlsx", index=False)
print("Arquivo criado com sucesso")
