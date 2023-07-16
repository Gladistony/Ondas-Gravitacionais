#importações
from pycbc import catalog
import pandas as pd

#Carregar Catalogo
c = catalog.Catalog()
#Função de reporta data
def dataCatalogo(nome):
	m = catalog.Merger(nome)
	return m.data
def addLinha(data):
    lista = []
    lista.append(data)
    m = catalog.Merger(data)
    #print(m.data.keys())
    lista.append(m.median1d('GPS'))
    lista.append(m.median1d('mass_1_source'))
    lista.append(m.median1d('mass_2_source'))
    lista.append(m.median1d('final_mass_source'))
    lista.append(m.median1d('luminosity_distance'))
    lista.append(m.median1d('strain'))
    return lista
#Carregar lista da Catalogo
LEvento = []
#LData = []
Excel = []
for merger_name in catalog.Catalog():
    LEvento.append(merger_name)
#for str in LEvento:
#    LData.append([str, dataCatalogo(str)])
for dados in LEvento:
    Excel.append(addLinha(dados))
#Adicionar arquivos ao Pandas
df = pd.DataFrame(Excel, columns=["GW Nome", "GPS Time", "Massa 1", "Massa 2", "Massa Final", "Distancia", "Variedade"])
df.to_excel("ondas_gravitacionais_gwosc.xlsx", index=False)
print("O arquivo excel foi criado com sucesso!")

# or from a specific merger
#m = catalog.Merger("GW170817")
#mchirp_gw170817 = m.median1d('mchirp')
#massa1 = m.median1d('mass1')
#print('GW170817: {}'.format(mchirp_gw170817))
#print(massa1)

# print parameters that can be read
#print(m.data.keys())

#'commonName', 'version', 'catalog.shortName', 'GPS', 'reference', 'jsonurl', 'strain', 'mass_1_source', 
# 'mass_1_source_lower', 'mass_1_source_upper', 'mass_1_source_unit', 'mass_2_source', 'mass_2_source_lower', 
# 'mass_2_source_upper', 'mass_2_source_unit', 'network_matched_filter_snr', 'network_matched_filter_snr_lower', 'network_matched_filter_snr_upper', 
# 'network_matched_filter_snr_unit', 'luminosity_distance', 'luminosity_distance_lower', 'luminosity_distance_upper', 
# 'luminosity_distance_unit', 'chi_eff', 'chi_eff_lower', 'chi_eff_upper', 'chi_eff_unit', 'total_mass_source', 'total_mass_source_lower', 
# 'total_mass_source_upper', 'total_mass_source_unit', 'chirp_mass_source', 'chirp_mass_source_lower', 'chirp_mass_source_upper', 
# 'chirp_mass_source_unit', 'chirp_mass', 'chirp_mass_lower', 'chirp_mass_upper', 'chirp_mass_unit', 'redshift', 'redshift_lower', 
# 'redshift_upper', 'redshift_unit', 'far', 'far_lower', 'far_upper', 'far_unit', 'p_astro', 'p_astro_lower', 'p_astro_upper', 
# 'p_astro_unit', 'final_mass_source', 'final_mass_source_lower', 'final_mass_source_upper', 'final_mass_source_unit'