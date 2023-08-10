import matplotlib.pyplot as plt
import numpy as np
import time

sample_rate = 10000 # Note: Nyquist frequency is sample_rate / 2
sample_num = 1000
dt = 1 / sample_rate
df = sample_rate / sample_num

time_axis = np.arange(0, sample_num/sample_rate, dt, dtype=float)
sample_axis = np.arange(0,sample_num, 1, dtype=int)
angular_freq_axis = np.arange(0, 2 * np.pi * sample_rate, 2 * np.pi * df, dtype=float)

sin100 = 5 * np.sin(2 * np.pi * 100 * time_axis)
sin1000 = 4 * np.sin(2 * np.pi * 1000 * time_axis)
sin2000 = 3 * np.sin(2 * np.pi * 2000 * time_axis + np.pi/6)
sin3000 = 2 * np.sin(2 * np.pi * 3000 * time_axis + np.pi/3)
input_signal = sin100 + sin1000 + sin2000 + sin3000

complex_freq_axis = np.exp(np.outer(sample_axis, np.array((1j) * (-2) * np.pi * sample_axis / sample_num))) # complex_freq_axis = np.array([np.exp((1j) * (-2) * np.pi * sample_axis * k / sample_num) for k in range(sample_num)]) 

complex_result = np.sum(input_signal * complex_freq_axis / sample_num, axis = 1)
result_real_part = np.round(np.real(complex_result), 7)
result_imag_part = np.round(np.imag(complex_result), 7) 

magnitude_spectrum = np.absolute(complex_result)
phase_spectrum = np.angle(np.where( (result_real_part == 0.0) & (result_imag_part == 0.0), 0 , complex_result )) * 180 / np.pi

# plot    
fig, axs = plt.subplots(2)
fig.suptitle('DFT')
axs[0].set(xlabel='frequency(rad/sec)', ylabel='magnitude')
axs[0].plot(angular_freq_axis[0:sample_num // 2], magnitude_spectrum[0:sample_num // 2])

axs[1].set(xlabel='frequency(rad/sec)', ylabel='phase')
axs[1].plot(angular_freq_axis[0:sample_num // 2], phase_spectrum[0:sample_num // 2])

plt.show()
