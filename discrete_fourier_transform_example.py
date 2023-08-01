import matplotlib.pyplot as plt
import math
import cmath
sample_rate = 1000 # Note: Nyquist frequency is 500Hz

time_axis = [i/sample_rate for i in range(sample_rate)]
sin10 = [5 * math.sin(2 * math.pi * 10 * t) for t in time_axis]
sin300 = [3 * math.sin(2 * math.pi * 100 * t) for t in time_axis]
sin500 = [2 * math.sin(2 * math.pi * 200 * t + math.pi/6) for t in time_axis]
input_signal = [a + b + c for a, b, c in zip(sin10, sin300, sin500)]

angular_freq_axis = [ 2 * math.pi * f for f in range(sample_rate)]
output_signal = []
dt = 1 / sample_rate
for k in range(sample_rate):
    magnitude = 0
    for i in range(sample_rate):
        # magnitude += ( input_signal[i] * cmath.rect(1, -1 * angular_freq_axis[k] * time_axis[i]) ) # cmath.rect(magnitude , phi)
        magnitude += ( input_signal[i] * cmath.rect(1, -2 * math.pi * k * i / sample_rate) ) # cmath.rect(magnitude , phi)
    output_signal.append(cmath.polar(magnitude)[0] * dt) # Don't forget to multiply by dt
    
# plt.plot(angular_freq_axis, input_signal)
plt.plot(angular_freq_axis[0:sample_rate // 2], output_signal[0:sample_rate // 2]) # Note: Nyquist frequency is 500Hz
plt.show()