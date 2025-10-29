import numpy as np 
import scipy as sci 
from tabulate import tabulate

class Medidas_Estadisticas:
    def __init__(self,datos,pdf=None,limite_inf=None):
        self.datos = datos
        self.pdf = pdf
        self.limite_inf = limite_inf

    def Medidas(self):
        keys = ["Media", "Varianza","Asimetria","Kurtosis"]
        momentos = dict.fromkeys(keys)
        descripcion = sci.stats.describe(self.datos)
        for i,k in enumerate(keys):
            #k = keys[i]
            momentos[k] = descripcion[i+2]
        return momentos

    def Kolmogorov_Smirnov(self):
        if self.pdf is not None and self.limite_inf is not None:
            def CDF(x):
                resultado, _ = sci.integrate.quad(self.pdf,self.limite_inf,x)
                return resultado
            CDF = np.vectorize(CDF)
            statistic, pvalue = sci.stats.kstest(datos,CDF)
            print(f"El estadistico corresponde a: {statistic:.4f}")
            print(f"El p-value es de:{pvalue:.4f}")
            return statistic, pvalue
        else:
            print("No se  proporciono la pdf o el limite inferiro")
            return None, None

    def Resumen_Resultados(self):
        dict_medidas = self.Medidas()
        datos_para_tabla = [[key, value] for key, value in dict_medidas.items()]
        headers = ["Medida", "Valor"]
        print(tabulate(datos_para_tabla, headers=headers,tablefmt="github"))



