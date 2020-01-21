import numpy as np
from IPython.display import Audio
import scipy.io.wavfile
from numpy.fft import fft, ifft, fft2, ifft2, fftshift, ifftshift
from scipy import ndimage, misc
from scipy.signal import gaussian

print('Enter File Name')
name = input()
Omega, f = scipy.io.wavfile.read(name)
Audio(f, rate=Omega)

# Some useful values
N = len(f)    # total number of samples
L = N / Omega # length of sound clip (in seconds)
t = np.arange(0,N) * L/N  # array of time stamps for samples

omega = np.fft.fftshift(np.arange(-N/2, N/2)) / L

tau = 2000
mask = abs(omega) < tau
Fe = F * mask
Audio(ifft(Fe), rate=Omega)