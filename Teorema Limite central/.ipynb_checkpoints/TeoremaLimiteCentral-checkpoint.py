import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

n = 1000000
X = np.random.poisson(lam=0.3,size=n)/n
X = np.cumsum(X)

# X[0] = np.random.poisson(0.3)

# for i in range(n-1):
#     y = np.random.poisson(0.3)
#     X[i+1] = (X[i] + y) / (i+1)
    
sns.barplot(data=X)
