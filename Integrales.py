from matricesAleatorias import matham as mh
import numpy as np
from scipy import integrate

densidad = mh.DensidadesHam(1000000,1)
inte = integrate.quad(densidad.Ps,0,np.inf)

print(r'densidad $P(S)$, la integral es:{}'.format(inte))

inte = integrate.quad(densidad.Pr,0,np.inf)

print(r'densidad $P(r)$, la integral es:{}'.format(inte))

inte = integrate.quad(densidad.lamCorre,-1.5,1.5)

print(r'densidad $P(\lambda)$, la integral es:{}'.format(inte))