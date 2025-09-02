import numpy as np
import scipy as sy
    

class MatrizHamiltoniana:
    def __init__(self,n):
        self.n = n

    def GOE(self):
        Y = np.random.normal(0,1,(self.n,self.n))
        return 0.5 * (Y + Y.T)
    
    def GUE(self):
        Y = np.random.normal(0,1/np.sqrt(2),(self.n,self.n)) + 1j * np.random.normal(0,1/np.sqrt(2),(self.n,self.n))
        return 0.5 * (Y + Y.conj().T)
    
    def GSE(self):
        A = np.random.normal(0,1,(self.n,self.n)) + 1j * np.random.normal(0,1,(self.n,self.n))
        A = (A + A.conj().T) / 2
        B = np.random.normal(0,1,(self.n,self.n)) + 1j * np.random.normal(0,1,(self.n,self.n))
        B = (B - B.T) / 2
        H_top = np.hstack((A, B))
        H_bottom = np.hstack((-B.conj(), A.T))
        return np.vstack((H_top, H_bottom))
    

class DensidadesHam:
    def __init__(self, n:int, beta:int):
        self.n = n
        self.beta = beta

    def Ps(self,S):
        if self.beta == 1:
            return np.pi*0.5*S*np.exp(-(np.pi/4)*S**2)
        elif self.beta == 2:
            return (32/np.pi**2) * (S**2) * np.exp(-(4/np.pi)*S**2)
        elif self.beta == 4:
            return (262144/(729*np.pi**3)) * S**4 * np.exp(-(64/(9*np.pi))*S**2)
        
    def Pr(self, r):
        if self.beta == 1:
            return (27/8) * (r+r**2) / (1+r+r**2)**(5/2)
        elif self.beta == 2:
            return ((81* np.sqrt(3))/(4*np.pi)) * (r+r**2)**2 / (1+r+r**2)**4
        elif self.beta == 4:
            return ((729 * np.sqrt(3))/(4*np.pi)) * (r+r**2)**4 / (1+r+r**2)**7

    def Plam(self,x):
        if self.beta == 1:
            return np.sqrt(2*self.n - x**2)/(self.n * np.pi)
        elif self.beta == 2:
            return np.sqrt(4*self.n - x**2) / (2*self.n*np.pi)
        elif self.beta == 4:
            return np.sqrt(8*self.n - x**2) / (4*self.n*np.pi)
        
    def PlamNorm(self,x):
        c = 1/(self.beta*self.n*np.pi)
        return c* np.sqrt(2*self.beta - x**2)
    
    def lamCorre(self,x):
        return (1/np.pi)* np.sqrt(2-x**2)
    
    def SemiCicle(self,x):
        rho = np.zeros_like(x)
        mask = np.abs(x) <= np.sqrt(2)
        rho[mask] = (1/np.pi) * np.sqrt(2 - x[mask]**2)
        return rho
    
    def SemiCircleNorm(self,x):
        rho = np.zeros_like(x)
        mask = np.abs(x) <= np.sqrt(2*self.beta*self.n)
        rho[mask] = (1/(self.beta * self.n * np.pi)) * np.sqrt(2*self.beta * self.n - x[mask] ** 2)
        return rho