import matplotlib.pyplot as plt
import math
import cmath

sample_rate = 10000 # Note: Nyquist frequency is sample_rate / 2
sample_num = 1000
dt = 1 / sample_rate
df = sample_rate / sample_num

time_axis = [i * dt for i in range(sample_num)]

sin100 = [5 * math.sin(2 * math.pi * 100 * t) for t in time_axis]
sin1000 = [4 * math.sin(2 * math.pi * 1000 * t) for t in time_axis]
sin2000 = [3 * math.sin(2 * math.pi * 2000 * t + math.pi/6) for t in time_axis]
sin3000 = [2 * math.sin(2 * math.pi * 3000 * t + math.pi/3) for t in time_axis]
input_signal = [a + b + c + d for a, b, c, d in zip(sin100, sin1000, sin2000, sin3000)]

angular_freq_axis = [2 * math.pi * df * i for i in range(sample_num)]
magnitude_spectrum = []
phase_spectrum = []
for k in range(sample_num):
    complex_num = 0
    for i in range(sample_num):
        complex_num += ( input_signal[i] * cmath.rect(1, -2 * math.pi * k * i / sample_num) ) # cmath.rect(r, phi)
    magnitude_spectrum.append(cmath.polar(complex_num)[0] * dt) # Don't forget to multiply by dt
    real_part = round(complex_num.real, 7)
    imag_part = round(complex_num.imag, 7)
    if real_part == 0.0 and imag_part == 0.0: phase_spectrum.append(0)
    else:                                     phase_spectrum.append(cmath.polar(complex_num)[1] * 180 / math.pi)

# plot    
fig, axs = plt.subplots(2)
fig.suptitle('DFT')
axs[0].set(xlabel='frequency(rad/sec)', ylabel='magnitude')
axs[0].plot(angular_freq_axis[0:sample_num // 2], magnitude_spectrum[0:sample_num // 2])

axs[1].set(xlabel='frequency(rad/sec)', ylabel='phase')
axs[1].plot(angular_freq_axis[0:sample_num // 2], phase_spectrum[0:sample_num // 2])

plt.show()