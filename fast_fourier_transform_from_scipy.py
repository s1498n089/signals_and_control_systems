import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq, ifft

sample_rate = 16384
sample_num = 16384
dt = 1 / sample_rate

t = np.linspace(0, 1, sample_num, endpoint=False)

f1, f2, f3, f4 = 100, 1000, 2000, 3000
A1, A2, A3, A4 = 5, 4, 3, 2
signal = A1*np.sin(2*np.pi*f1*t) + A2*np.sin(2*np.pi*f2*t) + A3*np.sin(2*np.pi*f3*t) + A4*np.sin(2*np.pi*f4*t)

fourier = np.fft.fft(signal)
freq = np.fft.fftfreq(signal.size, d=dt)

plt.plot(freq[:signal.size // 2], np.abs(fourier[:signal.size // 2])/signal.size, linestyle='-', color='blue')
plt.grid()
plt.xlabel('frequency (Hz)', fontsize=14)
plt.ylabel('magnitude', fontsize=14)
plt.show()
