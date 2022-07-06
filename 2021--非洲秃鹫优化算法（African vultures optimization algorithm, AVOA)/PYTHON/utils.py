import numpy as np
import random,math


def initialization(SearchAgents,dimension,upperbound,lowerbound):
    Boundary_no = len([upperbound])
    # Boundary_no = np.size(upperbound, 1)        # numnber  of  boundaries

#     如果所有变量的边界相等，用户为ub和lb都输入一个数字
    if Boundary_no == 1:
        X = np.random.randn(SearchAgents,dimension) * (upperbound-lowerbound)+lowerbound

#         如果每个变量有不同的lb和ub
    if Boundary_no > 1:
        for i in range(dimension):
            ub_i = upperbound[i]
            lb_i   = lowerbound[i]
            X[:,i] = np.random.randn(SearchAgents,1) * (ub_i - lb_i) + lb_i

    return X

def ObjectiveFunction(x):
    # change this file according to your objective function
    o=sum(x**2)
    return o

def BoundaryCheck(X, lb, ub):
    for i in range(np.size(X,0)):
            FU=X[i,:] > ub
            FL=X[i,:] < lb
            X[i,:]=(X[i,:] * (~(FU+FL)))+ub * FU+lb * FL
    return X

def RouletteWheelSelection(x):
    index=np.where(random.random() <= np.cumsum(x,axis=0) ,1,'first')
    return index

def random_select(Best_vulture1_X,Best_vulture2_X,alpha,betha):
    probabilities = [alpha, betha]
    if RouletteWheelSelection(probabilities) == 1:
        random_vulture_X = Best_vulture1_X
    else:
        random_vulture_X = Best_vulture2_X
    return random_vulture_X

def levyFlight(d):

    beta=3/2

    sigma=(math.gamma(1+beta) * np.sin(np.pi * beta/2)/(math.gamma((1+beta)/2) * beta*2**((beta-1)/2)))**(1/beta)
    u=np.random.randn(1,d)*sigma
    v=np.random.randn(1,d)
    step=u /abs(v)**(1/beta)

    o=step
    return o


def exploitation(current_vulture_X, Best_vulture1_X, Best_vulture2_X,
                 random_vulture_X, F, p2, p3, variables_no, upper_bound, lower_bound):

    # phase 1
        if  abs(F)<0.5:
            if random.random()<p2:
                A=Best_vulture1_X-((Best_vulture1_X * current_vulture_X) /(Best_vulture1_X-current_vulture_X**2))*F
                B=Best_vulture2_X-((Best_vulture2_X * current_vulture_X) /(Best_vulture2_X-current_vulture_X**2))*F
                current_vulture_X=(A+B)/2
            else:
                current_vulture_X=random_vulture_X-abs(random_vulture_X-current_vulture_X)*F * levyFlight(variables_no)

        # phase 2
        if  abs(F)>=0.5:
            if random.random()<p3:
                current_vulture_X=(abs((2*random.random())*random_vulture_X-current_vulture_X))*(F+random.random())-(random_vulture_X-current_vulture_X)
            else:
                s1=random_vulture_X *  (random.random()*current_vulture_X/(2*np.pi)) * np.cos(current_vulture_X)
                s2=random_vulture_X *  (random.random()*current_vulture_X/(2*np.pi)) * np.sin(current_vulture_X)
                current_vulture_X=random_vulture_X-(s1+s2)

        return current_vulture_X


def exploration(current_vulture_X, random_vulture_X, F, p1, upper_bound, lower_bound):
    if random.random() < p1:
        current_vulture_X = random_vulture_X - (abs((2 * random.random()) * random_vulture_X - current_vulture_X)) * F
    else:
        current_vulture_X = (random_vulture_X - (F) + random.random() * ((upper_bound - lower_bound) * random.random() + lower_bound))
    return current_vulture_X


def AVOA(pop_size,max_iter,lower_bound,upper_bound,variables_no):
    # initialize   Best_vulture1, Best_vulture2
    Best_vulture1_X = np.zeros([variables_no,1])
    Best_vulture1_F = np.inf
    Best_vulture2_X = np.zeros([variables_no,1])
    Best_vulture2_F = np.inf
    convergence_curve = np.zeros([max_iter,1])

    # Initialize  the  first random  population of  vultures
    X = initialization(pop_size, variables_no, upper_bound, lower_bound)

    # # Controlling  parameter
    p1 = 0.6
    p2 = 0.4
    p3 = 0.6
    alpha = 0.8
    betha = 0.2
    gamma = 2.5

    # # Main loop
    current_iter = 0 # Loop  counter

    while current_iter < max_iter:
        for i in range(np.size(X, 0)):
            # Calculate  the fitness  of the  population
            current_vulture_X = X[i,:]
            current_vulture_F = ObjectiveFunction(current_vulture_X)

            # Update the first best two   vultures if needed
            if current_vulture_F < Best_vulture1_F:
                Best_vulture1_F = current_vulture_F # Update  the first best  bulture
                Best_vulture1_X = current_vulture_X

            if current_vulture_F > Best_vulture1_F and current_vulture_F < Best_vulture2_F:
                Best_vulture2_F = current_vulture_F # Update  the second best bulture
                Best_vulture2_X = current_vulture_X

        a = random.uniform(-2, 2) * ((np.sin((np.pi / 2) * (current_iter / max_iter)) **gamma) + np.cos((np.pi / 2) * (current_iter / max_iter)) - 1) # 公式3
        P1 = (2 * random.random() + 1) * (1 - (current_iter / max_iter)) + a # 公式4

        # Update the location
        for i in range(np.size(X, 0)):
            current_vulture_X = X[i,:] # pick the current vulture  back  to  the population
            F = P1 * (2 * random.random() - 1)

            random_vulture_X = random_select(Best_vulture1_X, Best_vulture2_X, alpha, betha)

            if abs(F) >= 1: # Exploration:
                current_vulture_X = exploration(current_vulture_X, random_vulture_X, F, p1, upper_bound, lower_bound)
            elif abs(F) < 1: # Exploitation:
                current_vulture_X = exploitation(current_vulture_X, Best_vulture1_X, Best_vulture2_X, random_vulture_X, F, p2, p3,
                                                 variables_no, upper_bound, lower_bound)
            X[i,:] = current_vulture_X # place the current vulture back into the population

        convergence_curve[current_iter] = Best_vulture1_F
        current_iter = current_iter + 1
        X = BoundaryCheck(X, lower_bound, upper_bound)

        print("In Iteration{} , best estimation of the global optimum is {} ".format(current_iter,Best_vulture1_F) )

    return Best_vulture1_F,Best_vulture1_X,convergence_curve