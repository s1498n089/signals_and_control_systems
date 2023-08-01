import matplotlib.pyplot as plt
import math

sample_rate = 10000 # Note: Nyquist frequency is 5000
cut_off_freq = 20
cut_off_angular_freq = 2 * math.pi * cut_off_freq

'''
low_pass_filter(t) = laplace_inverse(w/(s+w)) , that w = cut_off_angular_freq
'''
def low_pass_filter(t):
    global cut_off_angular_freq
    return cut_off_angular_freq * (math.e ** (-1 *  cut_off_angular_freq * t))


time_axis = [i/sample_rate for i in range(sample_rate)]

low_pass = [low_pass_filter(t) for t in time_axis]
sin10 = [0.5 * math.sin(2 * math.pi * 10 * t) for t in time_axis]
sin300 = [0.2 * math.sin(2 * math.pi * 300 * t) for t in time_axis]
sin500 = [0.2 * math.sin(2 * math.pi * 500 * t + math.pi/6) for t in time_axis]
input_signal = [a + b + c for a, b, c in zip(sin10, sin300, sin500)]

# convolution 
output_signal = []
dt = 1 / sample_rate
for i in range(sample_rate):
    sum = 0
    for j in range(i):
        sum += input_signal[i-j] * low_pass[j] # here we don't have to multiply dt, we can extract dt
    output_signal.append(sum * dt)             # Don't forget to multiply by dt
    

# plt.plot(time_axis, low_pass)
plt.plot(time_axis, input_signal)
plt.plot(time_axis, output_signal)
plt.show()