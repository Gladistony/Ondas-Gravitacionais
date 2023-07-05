#Verificar Versão
import gwosc
print(gwosc.__version__)

#Buscar todos os catalogos
from gwosc.datasets import find_datasets
from gwosc import datasets

#-- List all available catalogs
print("List of available catalogs")
print(find_datasets(type="catalog"))

#mostra todos os eventos de um determinado catalogo
gwtc1 = datasets.find_datasets(type='events', catalog='GWTC-1-confident')
print('GWTC-1 events:', gwtc1)
print("")