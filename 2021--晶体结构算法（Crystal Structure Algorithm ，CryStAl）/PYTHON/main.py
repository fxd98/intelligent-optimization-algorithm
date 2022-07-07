from matplotlib import pyplot as plt
import numpy as np
from utils import CryStAI

## Get Required Problem Information
Var_Number = 100   # Number of variables

## Get Required Algorithm Parameters
MaxIteation = 10   # Maximum number of Iterations
Cr_Number = 10   # Maximum number of initial Crystals
LB = -10 *np.ones([Var_Number,1])    # Lower bound of variable
UB = 10 *np.ones([Var_Number,1])    # Upper bound of variable

Conv_History = CryStAI(Var_Number,MaxIteation,Cr_Number,LB,UB)

print(len(Conv_History))
plt.plot(range(len(Conv_History)),Conv_History)
plt.show()


