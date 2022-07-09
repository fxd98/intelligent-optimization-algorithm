from matplotlib import pyplot as plt
from utils import HBA

dim = 30
T = 15
Lb = -10
Ub = 10
N = 30
[xmin, fmin, CNVG] = HBA(dim, Lb, Ub, T, N)

plt.plot(range(len(CNVG)),CNVG,label = 'HBA')
plt.xlim([0,T])
plt.title('Convergence curve')
plt.xlabel('Iteration')
plt.ylabel('Best fitness obtained so far')
plt.legend()
plt.show()

print('The best location= ', xmin)
print('The best fitness score = ', fmin)



