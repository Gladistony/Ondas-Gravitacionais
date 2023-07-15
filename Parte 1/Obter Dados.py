#import gwosc
from pycbc import catalog


c = catalog.Catalog()
#mchirp = c.median1d('mchirp')
#print(mchirp)

def dataCatalogo(nome):
	m = catalog.Merger(nome)
	return m.data

print(dataCatalogo("GW170817"))

# or from a specific merger
#m = catalog.Merger("GW170817")
#mchirp_gw170817 = m.median1d('mchirp')
#massa1 = m.median1d('mass1')
#print('GW170817: {}'.format(mchirp_gw170817))
#print(massa1)

# print parameters that can be read
#print(m.data.keys())
