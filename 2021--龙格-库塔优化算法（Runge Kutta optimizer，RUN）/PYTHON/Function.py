import numpy as np
import random

def initialization(SearchAgents,dimension,upperbound,lowerbound):
    Boundary_no = len([upperbound])
    # Boundary_no = np.size(upperbound, 1)        # numnber  of  boundaries

#     如果所有变量的边界相等，用户为ub和lb都输入一个数字
    if Boundary_no == 1:
        X = np.random.randn(SearchAgents,dimension) * (upperbound[0]-lowerbound[0])+lowerbound[0]

#         如果每个变量有不同的lb和ub
    if Boundary_no > 1:
        for i in range(dimension):
            ub_i = upperbound[i]
            lb_i   = lowerbound[i]
            X[:,i] = np.random.randn(SearchAgents,1) * (ub_i - lb_i) + lb_i

    return X

def RungeKutta(XB,XW,DelX,dim):

    C=round(1 + random.random())*(1-random.random())
    r1=np.random.rand(1,dim)
    r2=np.random.rand(1,dim)
    
    K1 = 0.5*(random.random()*XW-C *XB)
    K2 = 0.5*(random.random()*(XW+r2 *K1 *DelX/2)-(C*XB+r1 *K1 *DelX/2))
    K3 = 0.5*(random.random()*(XW+r2 *K2 *DelX/2)-(C*XB+r1 *K2 *DelX/2))
    K4 = 0.5*(random.random()*(XW+r2 *K3 *DelX)-(C*XB+r1 *K3 *DelX))
    
    XRK = (K1+2 *K2+2 *K3+K4)
    SM=1/6*XRK
    return SM


def BC(X, lb, ub):
    Flag4ub = X > ub
    Flag4lb = X < lb
    X = (X * (~(Flag4ub + Flag4lb))) + ub * Flag4ub + lb * Flag4lb
    return X


def Get_Functions_details(F):
    D = 30
    if F == 'F1':
        fobj = F1
        lb = -100
        ub = 100
        dim = D

    if F == 'F2':
        fobj = F2
        lb = -10
        ub = 10
        dim = D

    if F == 'F3':
        fobj = F3
        lb = -100
        ub = 100
        dim = D

    if F == 'F4':
        fobj = F4
        lb = -100
        ub = 100
        dim = D

    if F == 'F5':
        fobj = F5
        lb = -30
        ub = 30
        dim = D

    if F == 'F6':
        fobj = F6
        lb = -100
        ub = 100
        dim = D

    if F == 'F7':
        fobj = F7
        lb = -1.28
        ub = 1.28
        dim = D

    if F == 'F8':
        fobj = F8
        lb = -500
        ub = 500
        dim = D

    if F == 'F9':
        fobj = F9
        lb = -5.12
        ub = 5.12
        dim = D

    if F == 'F10':
        fobj = F10
        lb = [-32]
        ub = [32]
        dim = D

    if F == 'F11':
        fobj = F11
        lb = -600
        ub = 600
        dim = D

    if F == 'F12':
        fobj = F12
        lb = -50
        ub = 50
        dim = D

    if F == 'F13':
        fobj = F13
        lb = -50
        ub = 50
        dim = D

    # if F == 'F14':
    #     fobj =F14
    #     lb = -65.536
    #     ub = 65.536
    #     dim = 2

    if F == 'F15':
        fobj = F15
        lb = -5
        ub = 5
        dim = 4

    if F == 'F16':
        fobj = F16
        lb = -5
        ub = 5
        dim = 2

    if F == 'F17':
        fobj = F17
        lb = -5
        ub = 5
        dim = 2

    if F == 'F18':
        fobj = F18
        lb = -5
        ub = 5
        dim = 2

    if F == 'F19':
        fobj = F19
        lb = 0
        ub = 1
        dim = 3

    if F == 'F20':
        fobj = F20
        lb = 0
        ub = 1
        dim = 6

    if F == 'F21':
        fobj = F21
        lb = 0
        ub = 10
        dim = 4

    if F == 'F22':
        fobj = F22
        lb = 0
        ub = 10
        dim = 4

    if F == 'F23':
        fobj = F23
        lb = 0
        ub = 10
        dim = 4
    return [lb], [ub], dim, fobj


def F1(x):
    o = sum(list(map(np.square, x)))
    return o


def F2(x):
    o = sum(abs(x)) + np.prod(abs(x), 0)
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
        (((x[:dim - 1] + 1) / 4) ** 2) * (1 + 10 * ((np.sin(np.pi * (1 + (x[1:dim] + 1) / 4)))) ** 2)) + (
                                     (x[dim] + 1) / 4) ^ 2) + sum(Ufun(x, 10, 100, 4))
    return o


def F13(x):
    dim = np.size(x, 0)

    o = .1 * ((np.sin(3 * np.pi * x[0])) ** 2 + np.sum(
        (x[:dim - 1] - 1) ** 2 * (1 + (np.sin(3 * np.pi * x[1:dim])) ** 2)) + ((x[dim - 1] - 1) ** 2) * (
                          1 + (np.sin(2 * np.pi * x[dim - 1])) ** 2)) + np.sum(Ufun(x, 5, 100, 4))

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
