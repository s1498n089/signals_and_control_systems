import matplotlib.pyplot as plt
import math
import cmath

bode_type = True
sample_rate = 100000 # Note: Nyquist frequency is sample_rate / 2
sample_num = 10000
dt = 1 / sample_rate
df = sample_rate / sample_num
cut_off_freq = 100
cut_off_angular_freq = 2 * math.pi * cut_off_freq

print("Please wait for a 20s...")

'''
low_pass_filter(t) = laplace_inverse(w/(s+w)) , that w = cut_off_angular_freq
'''
def low_pass_filter(t):
    global cut_off_angular_freq
    return cut_off_angular_freq * (math.e ** (-1 *  cut_off_angular_freq * t))

time_axis = [i * dt for i in range(sample_num)]
input_signal = [low_pass_filter(t) for t in time_axis]

angular_freq_axis = [2 * math.pi * df * i for i in range(sample_num)]
magnitude_spectrum = []
phase_spectrum = []
for k in range(sample_num):
    complex_num = 0
    for i in range(sample_num):
        complex_num += ( input_signal[i] * cmath.rect(1, -2 * math.pi * k * i / sample_num) ) # cmath.rect(r, phi)
    
    if bode_type == True: magnitude_spectrum.append(20 * math.log10(cmath.polar(complex_num)[0] * dt)) # Don't forget to multiply by dt
    else:                 magnitude_spectrum.append(cmath.polar(complex_num)[0] * dt) # Don't forget to multiply by dt
    
    real_part = round(complex_num.real, 7)
    imag_part = round(complex_num.imag, 7)
    if real_part == 0.0 and imag_part == 0.0: phase_spectrum.append(0)
    else:                                     phase_spectrum.append(cmath.polar(complex_num)[1] * 180 / math.pi)
    
# plot    
plt.title('DFT')
if bode_type == True: 
    plt.xscale("log")
    plt.xlabel('frequency(rad/sec)')
    plt.ylabel('magnitude(dB)')
else:        
    plt.xlabel('frequency(rad/sec)')         
    plt.ylabel('magnitude')
plt.plot(angular_freq_axis[0:sample_num // 2], magnitude_spectrum[0:sample_num // 2]) # Note: Nyquist frequency is sample_rate / 2
plt.show()