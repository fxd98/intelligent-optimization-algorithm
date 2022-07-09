import numpy as np
import random,math

def sumsqu(xx):
    d = len(xx)
    sum = 0
    for ii in range(d):
        xi = xx[ii]
        sum = sum + ii * xi**2
        y = sum
    return y

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


def fun_calcobjfunc(func, X):
    if  len(X.shape) == 2:
        N = np.size(X, 1)
        Y = np.zeros([N, 1])
        for i in range(N):
            Y[i] = func(X[i, :])
    else:
        N =1
        # Y = np.zeros([N, 1])
        Y = func(X)
    return Y


def Intensity(N, Xprey, X):

    di = np.zeros([N, 1])
    S = np.zeros([N, 1])
    I = np.zeros([N, 1])
    for i in range(N - 1):
        di[i] = (np.linalg.norm((X[i, :] - Xprey + np.finfo(np.float64).eps))) ** 2
        S[i] = (np.linalg.norm((X[i, :] - X[i + 1, :] + np.finfo(np.float64).eps))) ** 2

    di[N-1] = (np.linalg.norm((X[N-1, :] - Xprey + np.finfo(np.float64).eps))) ** 2
    S[N-1] = (np.linalg.norm((X[N-1, :] - X[0, :] + np.finfo(np.float64).eps))) ** 2
    for i in range(N):
        r2 = random.random()
        I[i] = r2 * S[i] / (4 * np.pi * di[i])
    return I

def HBA(dim, lb, ub, tmax, N):
    beta = 6 # the ability of HB to get the food Eq.(4)
    C = 2 # constant in Eq.(3)
    vec_flag = [1, -1]
    # initialization
    X = initialization(N, dim, ub, lb)

    Xnew = np.zeros([N,dim])
    CNVG  = np.zeros([tmax,1])
    # Evaluation
    fitness = fun_calcobjfunc(sumsqu, X)

    GYbest = min(fitness)
    gbest   = np.where(fitness == GYbest)[1]

    Xprey = X[gbest,:]
    for t in range(tmax):
        alpha = C * np.exp(-t / tmax) # density factor in Eq.(3)
        I = Intensity(N, Xprey, X) # intensity in Eq.(2)
        for i in range(N):
            r = random.random()
            F = vec_flag[int(np.floor(2 * random.random()))]
            for j in range(dim):
                di = (Xprey[0,j] - X[i, j])
                if r < .5:
                    r3 = random.random()
                    r4 = random.random()
                    r5 = random.random()

                    Xnew[i, j] = Xprey[0,j] + F * beta * I[i] * Xprey[0,j] + F * r3 * alpha * (di) * abs(np.cos(2 * np.pi * r4) * (1 - np.cos(2 * np.pi * r5)))
                else:
                    r7 = random.random()
                    Xnew[i, j] = Xprey[0,j] + F * r7 * alpha * di
                

            FU = Xnew[i,:] > ub
            FL = Xnew[i,:] < lb
            Xnew[i,:]=(Xnew[i,:]  * (~(FU + FL)))+ub  * FU + lb  * FL

            tempFitness = fun_calcobjfunc(sumsqu, Xnew[i,:])
            if tempFitness < fitness[i]:
                fitness[i] = tempFitness
                X[i,:]= Xnew[i,:]

        FU = X > ub
        FL = X < lb
        X = (X  * (~(FU + FL))) + ub  * FU + lb  * FL

        Ybest  = min(fitness)
        index = np.where(fitness == Ybest)[1]

        CNVG[t] = min(Ybest)
        if Ybest <= GYbest:
            GYbest = Ybest
            Xprey = X[index,:]
        print('第{}次迭代'.format(t), '最佳适应度值：', GYbest)
        print('\n')
    Food_Score = GYbest


    return Xprey, Food_Score, CNVG


