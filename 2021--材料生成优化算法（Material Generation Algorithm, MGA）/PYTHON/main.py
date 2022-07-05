import numpy as np
import random
import matplotlib.pyplot as plt

# # Objective
def Sphere(x):
    z = sum(x** 2)
    return z

Var_Number = 10     # Number of variables
VarMin = -10 * np.ones([ Var_Number,1])     # Lower bound of variable
VarMax = 10 * np.ones([ Var_Number,1])     # Upper bound of variable


# # Get Required Algorithm Parameters
MaxIteration = 100    # Maximum number of Iterations
NCompan = 100     # Maximum number of initial Companent
Globalbest = 0
Fun_Eval = np.ones([NCompan,1])
Best_Fun_Eval = np.ones([MaxIteration,1])
Best_Position   = np.ones([MaxIteration,Var_Number])
C_New_Position = np.ones([2,Var_Number])
C_New_Fun_Eval = np.ones([2,1])

# # Create Initial Companant
Position = np.resize(random.uniform(np.tile(VarMin, (NCompan, 10)), np.tile(VarMax, (NCompan, 10))),(NCompan,Var_Number))

# Evaluate Initial CompnMats
for ind in range(NCompan):
    Fun_Eval[ind] = Sphere(Position[ind,:])

# Find So Far Best
value   = min(Fun_Eval)
Index1 = np.where(Fun_Eval == value)[0][0]

Best_Fun_Eval[0] = value
print('Best_Fun_Eval[0]',Best_Fun_Eval[0])
Best_Position[0,:]= Position[Index1,:]


# # Main Loop of MSS
for Iter in np.arange(1,MaxIteration-1):
    print('迭代数：',Iter)
    # New   Companent     1
    # Index = NCompan  * np.arange(0,Var_Number) + np.random.choice(np.random.permutation(NCompan), size=Var_Number, replace=False)
    Index = np.random.choice(np.random.permutation(NCompan), size=Var_Number, replace=False)
    C_New_Position[0,:]= Position[Index[0],:] + random.uniform(-1, 1)  * np.random.randn(1, Var_Number)

    # New  Companent    2
    Index = np.random.choice(np.random.permutation(NCompan), size=1, replace=False)
    Index2 = np.random.choice(np.random.permutation(NCompan), size=Index, replace=False)
    CMs = np.random.randn(Index[0], 1)
    CMs = CMs / sum(CMs)
    P = np.ones([Index2.shape[0],Var_Number])
    for i in range(Index2.shape[0]):
        P[i,:] = Position[Index2[i],:]
    C_New_Position[1,:]=sum(CMs * P)

    # Apply  Lower and Upper  Bound  Limits
    for i in range(2):
        for j in range(Var_Number):
            C_New_Position[i] = max(C_New_Position[i,j], VarMin[j])
            C_New_Position[i] = min(C_New_Position[i,j], VarMax[j])
    # C_New_Position = max(C_New_Position, VarMin[Iter,:].T)
    # C_New_Position = min(C_New_Position, VarMax)

    # Evaluation
    for ind3 in range(np.size(C_New_Position, 0)):
        C_New_Fun_Eval[ind3] = Sphere(C_New_Position[ind3,:])

    # Update Companent
    AllCompn_Position = np.vstack((Position,C_New_Position))
    AllCompn_Fun_Eval =  np.vstack((Fun_Eval,C_New_Fun_Eval))
    Index1 = np.argsort(AllCompn_Fun_Eval,axis=0)
    for i in range(NCompan):
        Position[i,:] = AllCompn_Position[Index1[i],:]
        Fun_Eval[i,:] = AllCompn_Fun_Eval[Index1[i]]

    # Update So Far Best
    print(Best_Fun_Eval)
    print(Fun_Eval[0] , Best_Fun_Eval[Iter - 1])
    To_UpdateG = Fun_Eval[0] < Best_Fun_Eval[Iter - 1]
    best = (1 - To_UpdateG)  * Best_Position[Iter - 1,:]+To_UpdateG  * Position[1,:]
    Best_Fun_Eval[Iter] = (1 - To_UpdateG)  * Best_Fun_Eval[Iter - 1] + To_UpdateG  * Fun_Eval [1]
    Best_Position[Iter,:]=best
    print('best',Best_Fun_Eval[Iter])

    # Show Iteration  Information
    # Showindex = 1
    # if Showindex

    # Checking The Termination  Criteria
    if Best_Fun_Eval[Iter] < Globalbest:
        Globalbest = Best_Fun_Eval[Iter]
        break
    print('\n')

Eval_Number = NCompan + 2 * Iter
Conv_History = Best_Fun_Eval

# # Plot Results
# plot(Conv_History, 'LineWidth', 2)
plt.plot(np.arange(len(Conv_History)),Conv_History)
plt.xlabel('Iteration')
plt.ylabel('Best Cost')
plt.grid()
plt.show()


