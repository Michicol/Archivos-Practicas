import numpy as np
import matplotlib.pyplot as plt
from matricesAleatorias import matham as mh
plt.style.use('petroff10')

x = np.loadtxt("/home/michicol/Desktop/Practicas Profesionales/EnsambleGOE.dat")



#histEGOE, binsEGOE = np.histogram(x,bins=50)

#h = np.vstack((histEGOE,binsEGOE[:-1]))
#print(h.T.shape)

#np.savetxt('/home/michicol/Desktop/Practicas Profesionales/histEGOE.dat',h.T,delimiter=',')

plt.figure()

plt.hist(x,bins=50,density=True,linewidth=0.5, edgecolor="white")
plt.grid(True,linestyle='--')

plt.show()


