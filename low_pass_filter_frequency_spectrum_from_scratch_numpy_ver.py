import matplotlib.pyplot as plt
import numpy as np

bode_type = True
sample_rate = 10000 # Note: Nyquist frequency is sample_rate / 2
sample_num = 10000
dt = 1 / sample_rate
df = sample_rate / sample_num
cut_off_freq_hertz = 10
cut_off_freq_angular = 2 * np.pi * cut_off_freq_hertz

'''
low_pass_filter(t) = laplace_inverse(w/(s+w)) , that w = cut_off_freq_angular
'''
# def low_pass_filter(t):
#     global cut_off_freq_angular
#     return cut_off_freq_angular * (np.e ** (-1 *  cut_off_freq_angular * t))

time_axis = np.arange(0, sample_num/sample_rate, dt, dtype=float)
sample_axis = np.arange(0,sample_num, 1, dtype=int)
angular_freq_axis = np.arange(0, 2 * np.pi * sample_rate, 2 * np.pi * df, dtype=float)

input_signal = cut_off_freq_angular * (np.e ** (-1 *  cut_off_freq_angular * time_axis)) # low_pass_filter

complex_freq_axis = np.exp(np.outer(sample_axis, np.array((1j) * (-2) * np.pi * sample_axis / sample_num))) # complex_freq_axis = np.array([np.exp((1j) * (-2) * np.pi * sample_axis * k / sample_num) for k in range(sample_num)]) 

complex_result = np.sum(input_signal * complex_freq_axis / sample_num, axis = 1)
result_real_part = np.round(np.real(complex_result), 7)
result_imag_part = np.round(np.imag(complex_result), 7) 


if bode_type == True: magnitude_spectrum = 20 * np.log10(np.absolute(complex_result))
else:                 magnitude_spectrum = np.absolute(complex_result) # Don't forget to divide by sample_num

phase_spectrum = np.angle(np.where( (result_real_part == 0.0) & (result_imag_part == 0.0), 0 , complex_result )) * 180 / np.pi

    
# plot    
fig, axs = plt.subplots(2)
fig.suptitle('DFT')

if bode_type == True: 
    axs[0].set_xscale('log')
    axs[0].set(xlabel='frequency(rad/sec)', ylabel='magnitude(dB)')
else:
    axs[0].set(xlabel='frequency(rad/sec)', ylabel='magnitude')
axs[0].plot(angular_freq_axis[0:sample_num // 2], magnitude_spectrum[0:sample_num // 2])

axs[1].set(xlabel='frequency(rad/sec)', ylabel='phase(deg)')
if bode_type == True: 
    axs[1].set_xscale('log')
axs[1].plot(angular_freq_axis[0:sample_num // 2], phase_spectrum[0:sample_num // 2])

plt.show()