import numpy as np

class MatrizWishart:
    def __init__(self,dim:tuple):
        self.dim = dim

    def WOE(self):
        X = np.random.normal(0,1,self.dim)
        return np.matmul(X,X.T.conj()) / self.dim[0]
    
    def WUE(self):
        X = np.random.normal(0,1,self.dim) + 1j * np.random.normal(0,1,self.dim)
        return np.matmul(X,X.T.conj()) / self.dim[0]
    
    def WSE(self):
        a = np.random.normal(0,1,self.dim) + 1j * np.random.normal(0, 1, self.dim)
        b = np.random.normal(0, 1, self.dim) + 1j * np.random.normal(0, 1, self.dim)

        X = np.zeros((2*self.dim[0],2*self.dim[1]), dtype=complex)

        #Asignacion vectorizada
        X[0::2, 0::2] = a
        X[0::2, 1::2] = b
        X[1::2, 0::2] = -np.conj(b)
        X[1::2, 1::2] = np.conj(a)

        return np.matmul(X,X.T.conj()) #Resutado una matriz de 2N*2N
    

class Densidades(MatrizWishart):
    def __init__(self, dim: tuple, puntos:int, beta:int):
        super().__init__(dim)
        self.puntos = puntos
        self.beta = beta

    def MarchenkoPastur(self):
        q = self.dim[1] / self.dim[0]
        def m0(a):
            return np.maximum(a,np.zeros_like(a))
        
        Qplus = (1 + q**0.5) ** 2
        Qminus = (1 - q**0.5) ** 2

        x = np.linspace(Qminus,Qplus,self.puntos)
        y = np.sqrt(m0(Qplus - x) * m0(x - Qminus)) / (2 * np.pi * x)

        return x, y
    
    def Pr(self, r):
        if self.beta == 1:
            return (27/8) * (r+r**2) / (1+r+r**2)**(5/2)
        elif self.beta == 2:
            return ((81* np.sqrt(3))/(4*np.pi)) * (r+r**2)**2 / (1+r+r**2)**4
        elif self.beta == 4:
            return ((729 * np.sqrt(3))/(4*np.pi)) * (r+r**2)**4 / (1+r+r**2)**7