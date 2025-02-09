#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 23:50:46 2025

@author: Ersultan
"""

import numpy as np
import scienceplots
import pandas as pd
import matplotlib.pyplot as plt


plt.style.use(["science", "grid", 'ieee'])



df = pd.read_csv('datalab3.csv')
y = df['Velocity (m/s) Run #27'].values
x=df['Time (s) Auto'].values
b, m = np.polyfit(x, y, 1)
plt.figure(figsize = (13,4))
plt.plot(x, x*b+m, linestyle = 'dashed', color = 'purple', label = 'Fitted line = y = 1.8067595459236325x ± 0.03852425180598532')
plt.errorbar(x, y, fmt='rd', label = 'Experimental Data', xerr = 0, yerr = 0.3932705998, capsize = 5, capthick = 1, ecolor = 'black')
plt.ylabel('Velocity (m/s)', fontsize = 12)
plt.xlabel('Time (s)', fontsize  = 12)
plt.legend(loc = 'upper right', fontsize = 12, fancybox = False, edgecolor = 'black')
plt.grid(True)
plt.savefig('regres.png', dpi = 1500)
plt.show()
