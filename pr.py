import numpy as np
import matplotlib.pyplot as plt

# Parámetros
N = 1000       # Tamaño de la matriz
sigma = 1      # Varianza de elementos no diagonales

# Generar matriz aleatoria simétrica
A = np.random.normal(0, sigma, (N, N))
A = (A + A.T) / 2  # Hacerla simétrica

# Calcular eigenvalues
eigenvalues = np.linalg.eigvalsh(A)

# Calcular R a partir de la varianza de los eigenvalues
var_lambda = np.var(eigenvalues)
R_estimated = 2 * np.sqrt(var_lambda)

# Calcular R teórico (si se conoce sigma)
R_theoretical = 2 * sigma * np.sqrt(N)

def f(R,x):
    return (2/(np.pi*R**2)) * np.sqrt(R**2-x**2)

print(f"Radio estimado (R) desde eigenvalues: {R_estimated:.2f}")
print(f"Radio teórico (R) desde sigma y N: {R_theoretical:.2f}")

x = np.linspace(-1.5,1.5,100)

plt.figure()

plt.plot(x,f(R_estimated,x))

plt.show()