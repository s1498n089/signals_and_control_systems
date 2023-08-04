import matplotlib.pyplot as plt
import math
import cmath

bode_type = True
sample_rate = 10000 # Note: Nyquist frequency is sample_rate / 2
sample_num = 10000
dt = 1 / sample_rate
df = sample_rate / sample_num
cut_off_freq_hertz = 10
cut_off_freq_angular = 2 * math.pi * cut_off_freq_hertz

print("Please wait for a 20s...")

'''
low_pass_filter(t) = laplace_inverse(w/(s+w)) , that w = cut_off_freq_angular
'''
def low_pass_filter(t):
    global cut_off_freq_angular
    return cut_off_freq_angular * (math.e ** (-1 *  cut_off_freq_angular * t))

time_axis = [i * dt for i in range(sample_num)]
input_signal = [low_pass_filter(t) for t in time_axis]

angular_freq_axis = [2 * math.pi * df * i for i in range(sample_num)]
magnitude_spectrum = []
phase_spectrum = []
for k in range(sample_num):
    complex_num = 0
    for i in range(sample_num):
        complex_num += ( input_signal[i] * cmath.rect(1, -2 * math.pi * k * i / sample_num) ) # cmath.rect(r, phi)
    
    if bode_type == True: magnitude_spectrum.append(20 * math.log10(cmath.polar(complex_num)[0] / sample_num)) # Don't forget to divide by sample_num
    else:                 magnitude_spectrum.append(cmath.polar(complex_num)[0] / sample_num) # Don't forget to divide by sample_num
    
    real_part = round(complex_num.real, 7)
    imag_part = round(complex_num.imag, 7)
    if real_part == 0.0 and imag_part == 0.0: phase_spectrum.append(0)
    else:                                     phase_spectrum.append(cmath.polar(complex_num)[1] * 180 / math.pi)
    
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