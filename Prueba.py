#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 13:50:24 2025

@author: michicol
"""

import numpy as np
import matplotlib.pyplot as plt
from matricesAleatorias import matham as mh

Ps = lambda S: np.pi*0.5*S*np.exp(-(np.pi/4)*S**2)
Pr = lambda r: (27/8) * (r+r**2) / (1+r+r**2)**(5/2)
densidad = mh.DensidadesHam(100, 1)

S = np.linspace(0, 3,100)
ps = Ps(S)
psPOO = densidad.Ps(S)

r = np.linspace(0,6,100)
pr = Pr(r)
prPOO = densidad.Pr(r)

plt.figure()

plt.plot(r,pr,label='lambda')
plt.plot(r,prPOO,c='r',alpha=0.5,label='POO')
#plt.ylim(0,0.8)
plt.grid(True,)
plt.legend()

plt.show()