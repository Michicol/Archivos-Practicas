#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 14:13:51 2025

@author: michicol
"""
import numpy as np
import matplotlib.pyplot as plt
from matricesAleatorias import matham as mh

n = 10
nsamp = 100

H = mh.MatrizHamiltoniana(n)
Eval = []

for isamp in range(nsamp):
    HGOE = H.GOE()
    eval = np.linalg.eigvalsh(HGOE)
    eval = eval/np.sqrt(n)
    Eval.append(eval)

#print(Eval[0].shape)
Eval = np.concatenate(Eval)

plt.figure()

for i in range(1,11):
    plt.plot(np.arange(0,10),Eval[:10*i])
#plt.ylim(-1.5,1.5)
plt.axhline(-1.5,c='r',linestyle='--')
plt.axhline(1.5,c='r',linestyle='--')

plt.show()