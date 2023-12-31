import matplotlib.pyplot as pp
import pycbc.psd
import pycbc.types


filename = 'example_psd.txt'

# The PSD will be interpolated to the requested frequency spacing
delta_f = 1.0 / 4
length = int(1024 / delta_f)
low_frequency_cutoff = 30.0
psd = pycbc.psd.from_txt(filename, length, delta_f,
                         low_frequency_cutoff, is_asd_file=False)
pp.loglog(psd.sample_frequencies, psd, label='interpolated')

# The PSD will be read in without modification
psd = pycbc.types.load_frequencyseries('./example_psd.txt')
pp.loglog(psd.sample_frequencies, psd, label='raw')

pp.xlim(xmin=30, xmax=1000)
pp.legend()
pp.xlabel('Hz')
pp.show()

# Save a psd to file, several formats are supported (.txt, .hdf, .npy)
psd.save('tmp_psd.txt')
