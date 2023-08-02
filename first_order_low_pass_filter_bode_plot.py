import matplotlib.pyplot as plt
import math
import control
import numpy as np

sample_num = 10000
cut_off_freq = 10
cut_off_angular_freq = 2 * math.pi * cut_off_freq

num = [cut_off_angular_freq]
den = [1, cut_off_angular_freq]
low_pass_tf = control.tf(num, den)
angular_freq_axis = np.logspace(0, 5, sample_num)
control.bode(low_pass_tf, angular_freq_axis, Hz=False, dB=True, deg=True)

# plot
plt.show()