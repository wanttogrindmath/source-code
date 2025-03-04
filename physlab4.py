#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 03:31:57 2025

@author: Ersultan
"""

import numpy as np
import scienceplots
import pandas as pd
import matplotlib.pyplot as plt


plt.style.use(["science", "grid", 'ieee'])

data=pd.read_csv('data4.csv')
green=pd.read_csv('green.csv')
red = pd.read_csv('red.csv')
gr = pd.read_csv('g-r.csv')
bp = pd.read_csv('blue-p.csv')
bbpg = pd.read_csv('bbpg.csv')

x=data['position'].values
x_green = green['position'].values
x_red = red['position'].values
x_gred = gr['position'].values
x_bluepair = bp['position'].values
x_bpairgr = bbpg['position'].values



def substract(a,b):
    return np.array([z-b for z in a])

ext = np.linspace(0, 0.1, 10)
x_1 = substract(x, 0.15)
x_g = substract(x_green, 0.15)
x_r = substract(x_red, 0.16)
x_gr = substract(x_gred, 0.32)
x_bp = substract(x_bluepair, 0.18)
x_bbpg = substract(x_bpairgr, 0.38)

y=data['force'].values
y_g=green['force'].values
y_r=red['force'].values
y_gr = gr['force'].values
y_bp=bp['force'].values
y_bbpg = bbpg['force'].values

m, b = np.polyfit(x_1, y, 1) 
m_g,b_g = np.polyfit(x_g, y_g, 1)
m_r,b_r=np.polyfit(x_r, y_r, 1)
m_gr, b_gr = np.polyfit(x_gr, y_gr, 1)
m_bp, b_bp = np.polyfit(x_bp, y_bp, 1)
m_bbpg, b_bbpg = np.polyfit(x_bbpg, y_bbpg, 1)

plt.figure(figsize = (20, 6))
plt.plot(ext, ext*m+b, linestyle = 'dashed', color = 'darkcyan', label = 'Blue: y = 19.65556291x + 0.5967211')
plt.plot(ext, ext*m_g+b_g, linestyle = 'dashed', color = 'forestgreen', label = 'Green: y = 44.999998x + 0.950001' )
plt.plot(ext, ext*m_r+b_r, linestyle = 'dashed', color = 'firebrick', label = 'Red: 15.0837988x + 0.32849162')
plt.plot(ext, ext*m_gr+b_gr, linestyle = 'dashed', color = 'darkgoldenrod', label = 'Green-Red-Series: 11.8918918x + 0.4018108')
plt.plot(ext, ext*m_bp+b_bp, linestyle = 'dashed', color = 'violet', label = 'Blue-Parallel: 32.11000917x + 1.31110917')
plt.plot(ext, ext*m_bbpg+b_bbpg, linestyle = 'dashed', color = 'dodgerblue', label = 'Blue-Paralle-Green-Series: 32.0.0071684x + 0.9125448')
plt.errorbar(x_1, y, fmt='bd', label = 'Experimental Data Blue', xerr = 0.02391588796, yerr = 0.5280036731, capsize = 1, capthick = 1, ecolor = 'steelblue')
plt.errorbar(x_g, y_g, fmt='gd', label = 'Experimental Data Green', xerr = 0.0107871978, yerr = 0.6030226892, capsize = 1, capthick = 1, ecolor = 'limegreen')
plt.errorbar(x_r, y_r, fmt = 'rd', label = 'Experimental Data Red', xerr = 0.03153481321, yerr = 0.5049752469, capsize = 1, capthick = 1, ecolor = 'lightcoral')
plt.errorbar(x_gr, y_gr, fmt = 'yd', label = 'Experimental Data Green-Blue-Series', xerr = 0.04301162634, yerr = 0.5456901848, capsize = 1, capthick = 1, ecolor = 'olive' )
plt.errorbar(x_bp, y_bp, color = 'violet', marker = 'd', label = 'Experimental Data Blue-Paralle', xerr = 0.01100504935, yerr = 0.7527726527, capsize = 1, capthick = 1, ecolor = 'blueviolet' )
plt.errorbar(x_bbpg, y_bbpg, color = 'cyan', marker = 'd', label = 'Experimental Data Blue-Paralle-Green-Seires', xerr = 0.02252271581, yerr  = 0.8112840552, capsize = 1, capthick = 1, ecolor = 'teal')
plt.ylabel('Exerted Force (m)', fontsize = 14)
plt.xlabel('Elongation (m)', fontsize = 14)
plt.legend(loc = 'upper right', fontsize = 11, fancybox = False, edgecolor = 'black')
plt.grid(True)
plt.show()