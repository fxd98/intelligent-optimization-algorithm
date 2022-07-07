from Function import Get_Functions_HGS
from utils import *
from matplotlib import pyplot as plt

N=3 # Number of search agents

Function_name='F11' # Name of the test function, range from F1-F13

FEs=10 # Maximum number of evaluation times

dimSize = 3   #dimension size

# Load details of the selected benchmark function
lb,ub,dim,fobj=Get_Functions_HGS(Function_name,dimSize)

Destination_fitness,bestPositions,Convergence_curve=HGS(N,FEs,lb,ub,dim,fobj)


#Draw objective space

plt.plot(range(len(Convergence_curve)),Convergence_curve,label='HGS')
plt.title('Convergence curve')
plt.xlabel('Iteration')
plt.ylabel('Best fitness obtained so far')
plt.grid()
plt.legend()
plt.show()

print('The best location of HGS is: ', bestPositions)
print('The best fitness of HGS is: ', Destination_fitness)