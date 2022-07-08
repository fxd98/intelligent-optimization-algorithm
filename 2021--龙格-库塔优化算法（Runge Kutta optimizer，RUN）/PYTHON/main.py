from Function import Get_Functions_details
from utils import RUN
from matplotlib import pyplot as plt

nP=50          # Number of Population

Func_name='F1' # Name of the test function, range from F1-F14

MaxIt=10      # Maximum number of iterations

# Load details of the selected benchmark function
[lb,ub,dim,fobj]=Get_Functions_details(Func_name)

[Best_fitness,BestPositions,Convergence_curve] = RUN(nP,MaxIt,lb,ub,dim,fobj)

## Draw objective space


plt.plot(range(len(Convergence_curve)),Convergence_curve,label ='RUN')
plt.title('Convergence curve')
plt.xlabel('Iteration')
plt.ylabel('Best fitness obtained so far')
plt.grid()
plt.legend()
plt.show()
