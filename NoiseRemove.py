import numpy as np
from IPython.display import Audio
import scipy.io.wavfile
from numpy.fft import fft, ifft, fft2, ifft2, fftshift, ifftshift
from scipy import ndimage, misc
from scipy.signal import gaussian

print('Enter File Name without the extension')
name = input()
name_with_extension = name + '.wav'
Omega, f = scipy.io.wavfile.read(name_with_extension)
F = fft(f.T)

# Some useful values
N = len(f)    # total number of samples
L = N / Omega # length of sound clip (in seconds)
t = np.arange(0,N) * L/N  # array of time stamps for samples

omega = np.fft.fftshift(np.arange(-N/2, N/2)) / L

tau = 1550
mask = abs(omega) < tau
Fe = F * mask

inverted_Fe = ifft(Fe)

output_name = name + '_fixed.wav'
scipy.io.wavfile.write(output_name, Omega, (inverted_Fe.astype(f.dtype).T))
Audio(inverted_Fe, rate=Omega)