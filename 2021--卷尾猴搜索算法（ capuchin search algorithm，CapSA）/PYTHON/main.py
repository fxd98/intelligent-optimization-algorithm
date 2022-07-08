import numpy as np
from utils import CapSA
from matplotlib import pyplot as plt

#Prepare the problem
dim = 2
ub = 50 * np.ones([1, 2])
lb = -50 * np.ones([1, 2])

# CSA parameters
noP = 2
maxIter = 1000

bestFitness, bestPosition, CSAConvCurve = CapSA(noP, maxIter, lb, ub, dim)

print('===> The optimal fitness value found by Standard CapSA is ', bestFitness)

plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.plot(range(len(CSAConvCurve)),CSAConvCurve)
plt.xlabel('迭代数')
plt.ylabel('适应度值')
plt.show()

