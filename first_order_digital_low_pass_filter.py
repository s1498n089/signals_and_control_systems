import math
import matplotlib.pyplot as plt
import scipy.signal as sig

sample_rate = 10000 # Note: Nyquist frequency is 5000Hz 
cut_off_freq = 20
cut_off_angular_freq = 2 * math.pi * cut_off_freq

dt = 1 / sample_rate
num = cut_off_angular_freq
den = [1, cut_off_angular_freq]
low_pass = sig.TransferFunction(num, den)  # get transfer function
low_pass = low_pass.to_discrete(dt, method='bilinear') # from s-domain to z-domain using bilinear method
'''
print(low_pass)
array([0.00624395, 0.00624395]),
array([ 1.        , -0.98751209]),
dt: 0.0001
'''

time_axis = [i/sample_rate for i in range(sample_rate)]

sin10 = [0.5 * math.sin(2 * math.pi * 10 * t) for t in time_axis]
sin300 = [0.2 * math.sin(2 * math.pi * 300 * t) for t in time_axis]
sin500 = [0.2 * math.sin(2 * math.pi * 500 * t + math.pi/6) for t in time_axis]
input_signal = [a + b + c for a, b, c in zip(sin10, sin300, sin500)]

# inverse Z transform to get difference equation
output_signal = []
yn, yn_1, xn, xn_1 = (0,0,0,0)
for i in range(sample_rate):
    xn_1 = xn
    xn = input_signal[i]
    yn_1 = yn
    yn = 0.00624395 * xn + 0.00624395 * xn_1 + 0.98751209 * yn_1 # difference equation
    output_signal.append(yn)

plt.plot(time_axis, input_signal)
plt.plot(time_axis, output_signal)
plt.show()
