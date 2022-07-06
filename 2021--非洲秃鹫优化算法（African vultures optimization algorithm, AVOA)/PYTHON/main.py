from utils import *
from matplotlib import pyplot as plt

# Population size and stoppoing condition
pop_size = 3
max_iter = 10

variables_no = 10
lower_bound = -100 # can be a vector too
upper_bound = 100 # can be a vector too
Best_vulture1_F, Best_vulture1_X, convergence_curve = AVOA(pop_size, max_iter, lower_bound, upper_bound, variables_no)


plt.subplot(1,2,1)
plt.plot(range(len(Best_vulture1_X)),Best_vulture1_X)
plt.xlabel('Decision variables')
plt.ylabel('Best estimated values ')

# Best convergence curve
plt.subplot(1,2,2)
plt.plot(range(len(convergence_curve)),convergence_curve);
plt.title('Convergence curve of AVOA')
plt.xlabel('Current_iteration');
plt.ylabel('Objective value');
plt.show()