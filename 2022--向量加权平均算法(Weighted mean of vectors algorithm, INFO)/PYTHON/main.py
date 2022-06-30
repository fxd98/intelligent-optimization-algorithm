import numpy as np
import random
from Fuction import BenchmarkFunctions
from INFO import INFO
from matplotlib import pylab as plt

nP=10                         # Number of Population

Func_name='F10'# Name of the test function, range from F1-F23

MaxIt=10               # Maximum number of iterations


lb,ub,dim,fobj=BenchmarkFunctions(Func_name)
Best_fitness,BestPositions,Convergence_curve = INFO(nP,MaxIt,lb,ub,dim,fobj)

# 成图

plt.figure(figsize=(8,8))
plt.plot(range(MaxIt),Convergence_curve, 'ro-', color='#4169E1', alpha=0.8, linewidth=1,label = 'INFO')
plt.title('Convergence curve')
plt.xlabel('Iteration')
plt.ylabel('Best fitness obtained so far')
plt.grid()
plt.legend()
plt.show()

