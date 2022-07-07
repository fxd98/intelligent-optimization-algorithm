import numpy as np
import random
import datetime,math
from Function import *

def HGS(N,Max_iter,lb,ub,dim,fobj):
    print('HGS is now tackling your problem')
    starttime = datetime.datetime.now()

    # initialize position
    bestPositions = np.zeros([dim,1])
    tempPosition = np.zeros([dim,N])

    Destination_fitness = np.inf # change this to - inf for maximization problems
    Worstest_fitness = -np.inf
    AllFitness = np.inf * np.ones([N, 1]) # record the fitness  of all positions
    VC1 = np.ones([N, 1]) # record the variation control of  all positions
    weight3 = np.ones([N, dim]) # hungry weight  of each position
    weight4 = np.ones([N, dim]) # hungry weight of each position

    # Initialize the set of random  solutions
    X = initialization(N, dim, ub, lb)
    Convergence_curve = np.zeros([Max_iter,1])
    it = 0 # Number of iterations

    hungry = np.zeros([1,np.size(X, 0)]) # record  the hungry of all positions
    count = 0

    # Main loop
    while it < Max_iter:
        VC2 = 0.03 # The  variable of  variation  control

        sumHungry = 0 # record the  sum of  each hungry

        # sort   the  fitness
        for i in range(np.size(X, 0)):
            # Check if solutions go  outside the  search  space and bring  them back
            Flag4ub = X[i,:] > ub
            Flag4lb = X[i,:] < lb
            X[i,:]=(X[i,:]  * (~(Flag4ub + Flag4lb)))+ub  * Flag4ub + lb  * Flag4lb
            AllFitness[i] = fobj(X[i,:])

        AllFitnessSorted    = np.sort(AllFitness)
        IndexSorted            = np.argsort(AllFitness)
        bestFitness = AllFitnessSorted[0]
        worstFitness = AllFitnessSorted[-1]

        # update the best fitness value and best position
        if bestFitness < Destination_fitness:
            bestPositions = X[IndexSorted[0],:]
            Destination_fitness = bestFitness
            count = 0

        if worstFitness > Worstest_fitness:
            Worstest_fitness = worstFitness

        for i in range(np.size(X, 0)):
            # calculate  the variation control of all positions
            VC1[i]= 1/(math.cosh(abs(AllFitness[i] - Destination_fitness)))#公式2
            # calculate  the hungry of  each position
            if Destination_fitness == AllFitness[i]:
                hungry[0, i] = 0
                count = count + 1
                tempPosition[count,:]=X[i,:]
            else:
                temprand = random.random()
                c = (AllFitness[i]- Destination_fitness) / (Worstest_fitness - Destination_fitness) * temprand * 2 * (ub[0] - lb[0])#公式8
                if c < 100:#公式8
                    b = 100 * (1 + temprand)
                else:
                    b = c

                # hungry[0, i] = hungry[0, i]+ max(b)#公式8
                hungry[0, i] = hungry[0, i] + b  # 公式8
                sumHungry = sumHungry + hungry[0, i]


        # calculate the hungry weight of each position
        for i in range(np.size(X, 0)):
            for j in range(1,np.size(X, 1)):
                weight3[i, j] = (1 - np.exp(-abs(hungry[0, i]- sumHungry))) * random.random() * 2#公式7
                if random.random() < VC2:
                    weight4[i, j] = hungry[0, i]* np.size(X, 0) / sumHungry * random.random()#公式6
                else:
                    weight4[i, j] = 1

        # Update the Position of search agents
        shrink = 2 * (1 - it / Max_iter) # a  decreases  linearly  from 2  to  0 公式5
        for i in range(np.size(X, 0)):
            if random.random() < VC2:
                X[i,:] = X[i, j] * (1 + np.random.randn(1))#公式1.1
            else:
                A = np.random.randint(count)
                for j in range(np.size(X, 1)):
                    r = np.random.rand()
                    vb = 2 * shrink * r - shrink # [-a, a] 公式4
                    # Moving based on  the bestPosition
                    # The transformation range is controlled by  weight3, bestPositions and X
                    if r > VC1[i]:
                        X[i, j] = weight4[i, j] * tempPosition[A, j] + vb * weight3[i, j] * abs(tempPosition[A, j] - X[i, j])#公式1.2
                    else:
                        X[i, j] = weight4[i, j] * tempPosition[A, j] - vb * weight3[i, j] * abs(tempPosition[A, j] - X[i, j])#公式1.3


        Convergence_curve[it] = Destination_fitness
        it = it + 1
    # long running
    # do something other
    endtime = datetime.datetime.now()
    print((endtime - starttime).seconds)

    return Destination_fitness,bestPositions,Convergence_curve