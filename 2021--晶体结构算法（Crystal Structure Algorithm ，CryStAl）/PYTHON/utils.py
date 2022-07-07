import random

import numpy as np

## Boundary Handling
def bound(x,UB,LB):
    for i in range(len(x)):
        if x[i] >UB[i]:
            x[i]=UB[i]
        elif x[i] < LB[i]:
            x[i] = LB[i]
    return x
## Objective Function
def Sphere(x):
    z=sum(x**2)
    return z

def CryStAI(Var_Number,MaxIteation,Cr_Number,LB,UB):
    Crystal = np.ones([Cr_Number,Var_Number])
    Fun_eval = np.ones([Cr_Number,1])
    NewCrystal = np.ones([4,Var_Number])
    Fun_evalNew = np.ones([4,1])
    Conv_History = np.ones([MaxIteation,1])

    ## Outputs:
    # BestCr        (Best solution)
    # BestFitness     (final Best fitness)
    # Conv_History    (Convergence History Curve)
    ## Updating the Size of ProblemParameters
    if len(LB)==1:
        LB=np.tile(LB,1,Var_Number)

    if len(UB)==1:
        UB=np.tile(UB,1,Var_Number)

    ## Initialization
    # Initializing the Position of first probs
    for i in range(Cr_Number):
        Crystal[i,:]=np.random.uniform(LB,UB,[1,Var_Number])
        # Evaluating the initial probs
        Fun_eval[i]=Sphere(Crystal[i,:])

    # The best Crystal
    BestFitness =min(Fun_eval)
    idbest = np.where(Fun_eval==BestFitness)[1]
    Crb=Crystal[idbest,:]
    # Number of Function Evaluations
    Eval_Number=Cr_Number

    ## Search Process
    Iter=0
    while Iter<MaxIteation:
        for i in range(Cr_Number):
            ## Generate New Crystals
            # Main Crystal
            Crmain=Crystal[random.randint(0,Cr_Number-1),:]

            # Random-selected Crystals
            RandNumber=random.randint(1,Cr_Number)
            RandSelectCrystal=np.random.randint(Cr_Number,size = RandNumber)

            # Mean of randomly-selected Crystals
            Fc=np.mean(Crystal[RandSelectCrystal,:]) * (len(RandSelectCrystal) !=1)+Crystal[RandSelectCrystal[0],:]*(len(RandSelectCrystal)==1)
            # Random numbers (-1,1)
            r=2*random.random()-1
            r1=2*random.random()-1
            r2=2*random.random()-1
            r3=2*random.random()-1

            # New Crystals
            NewCrystal[0,:]=Crystal[i,:]+r*Crmain                                    #公式3
            NewCrystal[1,:]=Crystal[i,:]+r1*Crmain+r2*Crb                  #公式4
            NewCrystal[2,:]=Crystal[i,:]+r1*Crmain+r2*Fc                    #公式5
            NewCrystal[3,:]=Crystal[i,:]+r1*Crmain+r2*Crb+r3*Fc     #公式6
            for i2 in range(4):
                # Checking/Updating the boundary limits for Crystals
                NewCrystal[i2,:]=bound(NewCrystal[i2,:],UB,LB)

                # Evaluating New Crystals
                Fun_evalNew[i2]=Sphere(NewCrystal[i2,:])

                # Updating the Crystals
                if Fun_evalNew[i2]<Fun_eval[i]:
                    Fun_eval[i]=Fun_evalNew[i2]
                    Crystal[i,:]=NewCrystal[i2,:]

                # Updation the Number of Function Evalutions
                Eval_Number=Eval_Number+1
            # End of One Iteration


        # The best Crystal
        BestFitness = min(Fun_eval)
        idbest = np.where(Fun_eval == BestFitness)[1]
        Crb=Crystal[idbest,:]
        BestCr=Crb
        Conv_History[Iter]=BestFitness
        # Show Iteration Information
        print(['Iteration ' ,Iter, ': Best Cost = ' ,Conv_History[Iter]])
        Iter = Iter + 1
        # End of Main Looping
    return Conv_History


