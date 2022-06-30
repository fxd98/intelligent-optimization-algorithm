import random

import matplotlib.pyplot as plt
import numpy as np

def NGO(Search_Agents,Max_iterations,Lowerbound,Upperbound,dimensions,objective):
    # 初始化
    Lowerbound = np.ones([dimensions,1]) * Lowerbound
    Upperbound = np.ones([dimensions,1]) * Upperbound
    X           = np.ones([dimensions,dimensions])
    X_new  = np.ones([Search_Agents,dimensions])
    fit           = np.ones([Search_Agents,1])
    fit_new = np.ones([Search_Agents,1])
    best_so_far= np.ones([Max_iterations,1])
    average= np.ones([Max_iterations,1])
    NGO_curve = np.zeros([ Max_iterations,1])
    fbest = 0

    for i in range(dimensions):
        m = np.random.rand(Search_Agents, 1) * (Upperbound[i] - Lowerbound[i])
        for j in range(dimensions):
            X[j, i] = Lowerbound[i] +m[j]  # Initial  population

    for i in range(Search_Agents):
        L = X[i,:]
        fit[i] = objective(L) # Fitness evaluation(Explained  at the top  of the page. )

    for t in range(Max_iterations):  # algorithm iteration
        # update: BEST proposed solution
        best = min(fit)
        blocation = np.where(fit ==best)

        if t == 0:
            xbest = X[blocation,:] # Optimal location
            fbest = best                    # The optimization objective function
        elif best < fbest:
            fbest = best
            xbest = X[blocation,:]

        # UPDATE  Northern goshawks based on PHASE1 and PHASE2
        for i in range(Search_Agents):
            # Phase      1: Exploration
            I = round(1 + random.random())
            k = random.randint(0,Search_Agents-1)
            P = X[k,:]      # Eq.(3)
            F_P = fit[k]

            if fit[i] > F_P:
                X_new[i,:]=X[i,:]+np.random.rand(1, dimensions)  * (P - I  * X[i,:])      # Eq.(4)
            else:
                X_new[i,:]=X[i,:]+np.random.rand(1, dimensions)  * (X[i,:] - P)             # Eq.(4)
            for j in range(dimensions):
                X_new[i,:] = max(X_new[i,j], Lowerbound[i])
                X_new[i,:] = min(X_new[i,j], Upperbound[i])

            # update  position based   on Eq(5)
            L = X_new[i,:]
            fit_new[i] = objective(L)
            if (fit_new[i] < fit[i]):
                X[i,:] = X_new[i,:]
                fit[i] = fit_new[i]

            # END PHASE   1

            # PHASE    2         Exploitation
            R = 0.02 * (1 - t / Max_iterations)           #Eq.(6)
            X_new[i,:]= X[i,:]+ (-R + 2 * R * np.random.rand(1, dimensions))  * X[i,:]           #Eq.(7)

            for j in range(dimensions):
                X_new[i, :] = max(X_new[i, j], Lowerbound[i])
                X_new[i, :] = min(X_new[i, j], Upperbound[i])

            # update    position    based     on     Eq(8)
            L = X_new[i,:]
            fit_new[i] = objective(L)
            if (fit_new[i] < fit[i]):
                X[i,:] = X_new[i,:]
                fit[i] = fit_new[i]
            # END    PHASE    2
        # SAVE BEST  SCORE
        best_so_far[t] = fbest           #save  best  solution  so  far
        average[t] = np.mean(fit)
        Score = fbest
        Best_pos = xbest
        print('t = ',t,'Score',Score)
        NGO_curve[t] = Score
    return Score,Best_pos,NGO_curve



def fun_plot(fun_name):
    lowerbound, upperbound, dimension, fitness = fun_info(fun_name)
    if fun_name == 'F1':
        x = np.array(range(-100,100,2))
        y = x                       #[-100, 100]

    if fun_name == 'F2':
        x = np.array(range(-100,100,2))
        y = x # [-10, 10]

    if fun_name == 'F3':
        x = np.array(range(-100,100,2))
        y = x # [-100, 100]

    if fun_name == 'F4':
        x = np.array(range(-100,100,2))
        y = x # [-100, 100]

    if fun_name == 'F5':
        x = np.array(range(-200,200,2))-200
        y = x # [-5, 5]

    if fun_name == 'F6':
        x = np.array(range(-100,100,2))
        y = x # [-100, 100]

    if fun_name == 'F7':
        x = np.array(range(-100,100,3))/100
        y = x # [-1, 1]

    if fun_name == 'F8':
        x = np.array(range(-500,500,10))
        y = x # [-500, 500]

    if fun_name == 'F9':
        x =np.array(range(-50,50,1)) /10
        y = x # [-5, 5]

    if fun_name == 'F10':
        x = np.array(range(-200,200,5)) /10
        y = x # [-500, 500]

    if fun_name == 'F11':
        x = np.array(range(-500,500,10))
        y = x # [-0.5, 0.5]

    if fun_name == 'F12':
        x = np.array(range(-100,100,1))/ 10
        y = x # [-pi, pi]

    if fun_name == 'F13':
        x = np.array(range(-500,500,8))/ 100
        y = x # [-3, 1]

    if fun_name == 'F14':
        x = np.array(range(-100,100,2))
        y = x # [-100, 100]

    if fun_name == 'F15':
        x = np.array(range(-50,50,1))/10
        y = x # [-5, 5]

    if fun_name == 'F16':
        x = np.array(range(-100,100,1))/100
        y = x # [-5, 5]

    if fun_name == 'F17':
        x = np.array(range(-50,50,1))/10
        y = x # [-5, 5]

    if fun_name == 'F18':
        x = np.array(range(-500,500,6))/100
        y = x # [-5, 5]

    if fun_name == 'F19':
        x = np.array(range(-50,50,1))/10
        y = x # [-5, 5]

    if fun_name == 'F20':
        x = np.array(range(-50,50,1))/10
        y = x # [-5, 5]

    if fun_name == 'F21':
        x =np.array(range(-50,50,1))/10
        y = x # [-5, 5]

    if fun_name == 'F22':
        x = np.array(range(-50,50,1))/10
        y = x # [-5, 5]

    if fun_name == 'F23':
        x = np.array(range(-50,50,1))/10
        y = x # [-5, 5]

    L = len(x)
    f = np.ones([L,L])

    for i in range(L):
        for j in range(L):
            if fun_name != 'F15' and  fun_name != 'F19' \
                    and fun_name != 'F20' and fun_name != 'F21' \
                    and fun_name != 'F22' and fun_name != 'F23':
                f[i, j] = fitness([x[i], y[j]])

            if fun_name == 'F15':
                f[i, j] = fitness([x[i], y[j], 0, 0])

            if fun_name == 'F19':
                f[i, j] = fitness([x[i], y[j], 0])

            if fun_name == 'F20':
                f[i, j] = fitness([x[i], y[j], 0, 0, 0, 0])

            if fun_name == 'F21' or fun_name == 'F22' or fun_name == 'F23':
                f[i, j] = fitness([x[i], y[j], 0, 0])
    return x,y,f



def fun_info(F):
    D = 30
    if F == 'F1':
        fitness = F1
        lowerbound = -100
        upperbound = 100
        dimension = D

    if F == 'F2':
        fitness = F2
        lowerbound = -10
        upperbound = 10
        dimension = D

    if F == 'F3':
        fitness = F3
        lowerbound = -100
        upperbound = 100
        dimension = D

    if F == 'F4':
        fitness = F4
        lowerbound = -100
        upperbound = 100
        dimension = D

    if F == 'F5':
        fitness = F5
        lowerbound = -30
        upperbound = 30
        dimension = D

    if F == 'F6':
        fitness = F6
        lowerbound = -100
        upperbound = 100
        dimension = D

    if F == 'F7':
        fitness = F7
        lowerbound = -1.28
        upperbound = 1.28
        dimension = D

    if F == 'F8':
        fitness = F8
        lowerbound = -500
        upperbound = 500
        dimension = D

    if F == 'F9':
        fitness = F9
        lowerbound = -5.12
        upperbound = 5.12
        dimension = D

    if F == 'F10':
        fitness = F10
        lowerbound = [-32]
        upperbound = [32]
        dimension = D

    if F == 'F11':
        fitness = F11
        lowerbound = -600
        upperbound = 600
        dimension = D

    if F == 'F12':
        fitness = F12
        lowerbound = -50
        upperbound = 50
        dimension = D

    if F == 'F13':
        fitness = F13
        lowerbound = -50
        upperbound = 50
        dimension = D

    # if F == 'F14':
    #     fitness =F14
    #     lowerbound = -65.536
    #     upperbound = 65.536
    #     dimension = 2

    if F == 'F15':
        fitness = F15
        lowerbound = -5
        upperbound = 5
        dimension = 4

    if F == 'F16':
        fitness = F16
        lowerbound = -5
        upperbound = 5
        dimension = 2

    if F == 'F17':
        fitness = F17
        lowerbound = -5
        upperbound = 5
        dimension = 2

    if F == 'F18':
        fitness = F18
        lowerbound = -5
        upperbound = 5
        dimension = 2

    if F == 'F19':
        fitness = F19
        lowerbound = 0
        upperbound = 1
        dimension = 3

    if F == 'F20':
        fitness = F20
        lowerbound = 0
        upperbound = 1
        dimension = 6

    if F == 'F21':
        fitness = F21
        lowerbound = 0
        upperbound = 10
        dimension = 4

    if F == 'F22':
        fitness = F22
        lowerbound = 0
        upperbound = 10
        dimension = 4

    if F == 'F23':
        fitness = F23
        lowerbound = 0
        upperbound = 10
        dimension = 4
    return lowerbound, upperbound, dimension, fitness


def F1(x):
    sum = 0
    for i in range(len(x)):
        sum = sum + x[i] ** 2
    o = sum
    return o


def F2(x):
    o = sum(np.abs(x)) + np.prod(np.abs(x), 0)
    return o


def F3(x):
    dim = np.size(x, 0)
    o = 0
    for i in range(dim):
        o = o + sum(x[:i + 1]) ** 2
    return o


def F4(x):
    o = max(abs(x))
    return o


def F5(x):
    dim = np.size(x, 0)  # 列数
    o = sum(100 * (x[1:dim] - (x[:dim - 1] ** 2)) ** 2 + (x[:dim - 1] - 1) ** 2)
    return o


def F6(x):
    o = sum(abs((x + .5)) ** 2)
    return o


def F7(x):
    dim = np.size(x, 0)
    new = []
    for i in range(dim):
        new.append(i + 1)
    o = sum(new * (x ** 4)) + random.random()
    return o


def F8(x):
    o = sum(-x * np.sin(np.sqrt(abs(x))))
    return o


def F9(x):
    dim = np.size(x, 0)
    o = sum(x ** 2 - 10 * np.cos(2 * np.pi * x)) + 10 * dim
    return o


def F10(x):
    dim = np.size(x, 0)

    o = -20 * np.exp(-.2 * np.sqrt(sum(x ** 2) / dim)) - np.exp(sum(np.cos(2 * np.pi * x)) / dim) + 20 + np.exp(1)
    return o


def F11(x):
    dim = np.size(x, 0)
    new = []
    for i in range(dim):
        new.append(i + 1)
    o = sum(x ** 2) / 4000 - np.prod(np.cos(x / np.sqrt(new))) + 1
    return o


def F12(x):
    dim = np.size(x, 0)
    o = (np.pi / dim) * (10 * ((np.sin(np.pi * (1 + (x[0] + 1) / 4))) ^ 2) + sum(
        (((x[:dim - 1] + 1) / 4) ** 2) * (1 + 10  * ((np.sin(np.pi * (1 + (x[1:dim] + 1) / 4)))) ** 2)) + (
                                     (x[dim] + 1) / 4) ^ 2) + sum(Ufun(x, 10, 100, 4))
    return o


def F13(x):
    dim = np.size(x, 0)
    o = .1 * ((np.sin(3 * np.pi * x[0])) ^ 2 + sum(
        (x[:dim - 1] - 1) ** 2  * (1 + (np.sin(3  * np.pi * x[1:dim])) ** 2)) + ((x[dim] - 1) ** 2) * (
                          1 + (np.sin(2 * np.pi * x[dim])) ** 2)) + sum(Ufun(x, 5, 100, 4))
    return o


# def F14(x):
#     aS = np.array([[-32,-16,0,16,32,-32,-16,0,16,32,-32,-16,0,16,32,-32,-16,0,16,32,-32,-16,0,16,32],[
#                 -32,-32,-32,-32,-32,-16,-16,-16,-16,-16,0,0,0,0,0,16,16,16,16,16,32,32,32,32,32]])
#     bS = np.ones([1,25])
#     for j in range(25):
#         bS[j] = sum((x'-aS(:,j)).^6)
#     end
#     o=(1 / 500+sum(1. / ([1:25]+bS))).^ (-1)

def F15(x):
    aK = [.1957, .1947, .1735, .16, .0844, .0627, .0456, .0342, .0323, .0235, .0246]
    bK = [.25, .5, 1, 2, 4, 6, 8, 10, 12, 14, 16]
    bK = 1. / bK
    o = sum((aK - ((x[0] * (bK ** 2 + x[1] * bK)) / (bK ** 2 + x[2] * bK + x[3]))) ** 2)
    return o


def F16(x):
    o = 4 * (x[0] ^ 2) - 2.1 * (x[0] ^ 4) + (x[0] ^ 6) / 3 + x[0] * x[1] - 4 * (x[1] ^ 2) + 4 * (x[1] ^ 4)
    return o


def F17(x):
    o = (x[1] - (x[0] ** 2) * 5.1 / (4 * (np.pi ** 2)) + 5 / np.pi * x[0] - 6) ** 2 + 10 * (
                1 - 1 / (8 * np.pi)) * np.cos(x[0]) + 10
    return o


def F18(x):
    o = (1 + (x[0] + x[1] + 1) ^ 2 * (19 - 14 * x[0] + 3 * (x[0] ^ 2) - 14 * x[1] + 6 * x[0] * x[1] + 3 * x[1] ^ 2)) * (
                30 + (2 * x[0] - 3 * x[1]) ^ 2 * (
                    18 - 32 * x[0] + 12 * (x[0] ^ 2) + 48 * x[1] - 36 * x[0] * x[1] + 27 * (x[1] ^ 2)))
    return o


def F19(x):
    aH = [3, 10, 30, .1, 10, 35, 3, 10, 30, .1, 10, 35]
    cH = [1, 1.2, 3, 3.2]
    pH = [.3689, .117, .2673, .4699, .4387, .747, .1091, .8732, .5547, .03815, .5743, .8828]
    o = 0
    for i in range(4):
        o = o - cH[i] * np.exp(-(sum(aH[i, :] * ((x - pH[i, :]) ** 2))))
    return o


def F20(x):
    aH = [10, 3, 17, 3.5, 1.7, 8, .05, 10, 17, .1, 8, 14, 3, 3.5, 1.7, 10, 17, 8, 17, 8, .05, 10, .1, 14]
    cH = [1, 1.2, 3, 3.2]
    pH = [.1312, .1696, .5569, .0124, .8283, .5886, .2329, .4135, .8307, .3736, .1004, .9991, .2348, .1415, .3522,
          .2883, .3047, .6650, .4047, .8828, .8732, .5743, .1091, .0381]
    o = 0
    for i in range(4):
        o = o - cH[i] * np.exp(-(sum(aH[i, :] * ((x - pH[i, :]) ** 2))))
    return o


def F21(x):
    aSH = [4, 4, 4, 4, 1, 1, 1, 1, 8, 8, 8, 8, 6, 6, 6, 6, 3, 7, 3, 7, 2, 9, 2, 9, 5, 5, 3, 3, 8, 1, 8, 1, 6, 2, 6, 2,
           7, 3.6, 7, 3.6]
    cSH = [.1, .2, .2, .4, .4, .6, .3, .7, .5, .5]
    o = 0
    for i in range(5):
        o = o - ((x - aSH[i, :]) * (x - aSH[i, :]) + cSH[i]) ** (-1)
    return o


def F22(x):
    aSH = [4, 4, 4, 4, 1, 1, 1, 1, 8, 8, 8, 8, 6, 6, 6, 6, 3, 7, 3, 7, 2, 9, 2, 9, 5, 5, 3, 3, 8, 1, 8, 1, 6, 2, 6, 2,
           7, 3.6, 7, 3.6]
    cSH = [.1, .2, .2, .4, .4, .6, .3, .7, .5, .5]
    o = 0
    for i in range(7):
        o = o - ((x - aSH[i, :]) * (x - aSH[i, :]) + cSH[i]) ** (-1)
    return o


def F23(x):
    aSH = [4, 4, 4, 4, 1, 1, 1, 1, 8, 8, 8, 8, 6, 6, 6, 6, 3, 7, 3, 7, 2, 9, 2, 9, 5, 5, 3, 3, 8, 1, 8, 1, 6, 2, 6, 2,
           7, 3.6, 7, 3.6]
    cSH = [.1, .2, .2, .4, .4, .6, .3, .7, .5, .5]
    o = 0
    for i in range(10):
        o = o - ((x - aSH[i, :]) * (x - aSH[i, :]) + cSH[i]) ** (-1)
    return o


def Ufun(x, a, k, m):
    o = k * ((x - a) ** m) * (x > a) + k * ((-x - a) ** m) * (x < (-a))
    return o