import math
import matplotlib.pyplot as plt
import scipy.signal as sig

sample_rate = 10000 # Note: Nyquist frequency is sample_rate / 2 
sample_num = 1000
dt = 1 / sample_rate
cut_off_freq_hertz = 20
cut_off_freq_angular = 2 * math.pi * cut_off_freq_hertz

num = cut_off_freq_angular # w
den = [1, cut_off_freq_angular] # s^1 + w
low_pass = sig.TransferFunction(num, den)  # get transfer function
low_pass = low_pass.to_discrete(dt, method='bilinear') # from s-domain to z-domain using bilinear method
'''
print(low_pass)
array([0.00624395, 0.00624395]),
array([ 1.        , -0.98751209]),
dt: 0.0001
'''

time_axis = [i * dt for i in range(sample_num)]

sin10 = [0.5 * math.sin(2 * math.pi * 10 * t) for t in time_axis]
sin300 = [0.2 * math.sin(2 * math.pi * 300 * t) for t in time_axis]
sin500 = [0.2 * math.sin(2 * math.pi * 500 * t + math.pi/6) for t in time_axis]
input_signal = [a + b + c for a, b, c in zip(sin10, sin300, sin500)]

# inverse Z transform to get difference equation
output_signal = []
yn, yn_1, xn, xn_1 = (0,0,0,0)
for i in range(sample_num):
    xn_1 = xn
    xn = input_signal[i]
    yn_1 = yn
    yn = 0.00624395 * xn + 0.00624395 * xn_1 + 0.98751209 * yn_1 # difference equation
    output_signal.append(yn)

# plot
plt.title('low-pass filter')
plt.plot(time_axis, input_signal, label='input')
plt.plot(time_axis, output_signal, label='output')
plt.legend(
    loc='best',
    shadow=True,
    facecolor='#ccc',
    edgecolor='#000')
plt.xlabel('time(s)')
plt.ylabel('amplitude')
plt.show()
