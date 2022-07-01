import numpy as np
import random
from scipy import rand


def initialization(SearchAgents,dimension,upperbound,lowerbound):
    Boundary_no = len([upperbound])
    # Boundary_no = np.size(upperbound, 1)        # numnber  of  boundaries

#     如果所有变量的边界相等，用户为ub和lb都输入一个数字
    if Boundary_no == 1:
        X = rand(SearchAgents,dimension) * (upperbound-lowerbound)+lowerbound

#         如果每个变量有不同的lb和ub
    if Boundary_no > 1:
        for i in range(dimension):
            ub_i = upperbound[i]
            lb_i   = lowerbound[i]
            X[:,i] = rand(SearchAgents,1) * (ub_i - lb_i) + lb_i

    return X

def RSO(Search_Agents,Max_iterations,Lower_bound,Upper_bound,dimension,objective):
    Position = np.zeros([1,dimension])
    Score = np.inf
    Positions = initialization(Search_Agents,dimension,Upper_bound,Lower_bound)
    Convergence = np.zeros([1,Max_iterations])

    l = 0
    x = 1
    y = 5
    R = round((y - x) * random.random() + x)

    while l < Max_iterations:
        for i in range(np.size(Positions,0)):
            Flag4Upper_bound = Positions[i,:] > Upper_bound
            Flag4Lower_bound = Positions[i,:] < Lower_bound
            Positions[i,:]=(Positions[i,:] * (~(Flag4Upper_bound + Flag4Lower_bound)))+Upper_bound * Flag4Upper_bound + Lower_bound * Flag4Lower_bound

            fitness = objective(Positions[i,:])

            if fitness < Score:
                Score = fitness
                Position = Positions[i,:]

        A = R - l *((R) / Max_iterations)

        for i in range(np.size(Positions,0)):
            for j in range(np.size(Positions,1)):
                C = 2 * random.random()
                P_vec = A * Positions[i,j] + abs(C * (Position[j] - Positions[i,j]))
                P_final = Position[j] - P_vec
                Positions[i,j] = P_final
        print('迭代数',l,'Score:',Score)
        Convergence[:,l] = Score
        l = l + 1
    return Score,Position,Convergence

def BC(X, lb, ub):
    Flag4ub = X > ub
    Flag4lb = X < lb
    X = (X  * (~(Flag4ub + Flag4lb))) + ub  * Flag4ub + lb * Flag4lb
    return X


def BenchmarkFunctions(F):
    D = 30
    if F == 'F1':
        fobj = F1
        lb = -100
        ub = 100
        dim = D

    if F == 'F2':
        fobj =F2
        lb = -10
        ub = 10
        dim = D

    if F == 'F3':
        fobj =F3
        lb = -100
        ub = 100
        dim = D

    if F == 'F4':
        fobj =F4
        lb = -100
        ub = 100
        dim = D

    if F == 'F5':
        fobj =F5
        lb = -30
        ub = 30
        dim = D

    if F == 'F6':
        fobj =F6
        lb = -100
        ub = 100
        dim = D

    if F == 'F7':
        fobj =F7
        lb = -1.28
        ub = 1.28
        dim = D

    if F == 'F8':
        fobj =F8
        lb = -500
        ub = 500
        dim = D

    if F == 'F9':
        fobj =F9
        lb = -5.12
        ub = 5.12
        dim = D

    if F == 'F10':
        fobj =F10
        lb = [-32]
        ub =[32]
        dim = D

    if F == 'F11':
        fobj =F11
        lb = -600
        ub = 600
        dim = D

    if F == 'F12':
        fobj =F12
        lb = -50
        ub = 50
        dim = D

    if F == 'F13':
        fobj =F13
        lb = -50
        ub = 50
        dim = D

    # if F == 'F14':
    #     fobj =F14
    #     lb = -65.536
    #     ub = 65.536
    #     dim = 2

    if F == 'F15':
        fobj =F15
        lb = -5
        ub = 5
        dim = 4

    if F == 'F16':
        fobj =F16
        lb = -5
        ub = 5
        dim = 2

    if F == 'F17':
        fobj =F17
        lb = -5
        ub = 5
        dim = 2

    if F == 'F18':
        fobj =F18
        lb = -5
        ub = 5
        dim = 2

    if F == 'F19':
        fobj =F19
        lb = 0
        ub = 1
        dim = 3

    if F == 'F20':
        fobj =F20
        lb = 0
        ub = 1
        dim = 6

    if F == 'F21':
        fobj =F21
        lb = 0
        ub = 10
        dim = 4

    if F == 'F22':
        fobj =F22
        lb = 0
        ub = 10
        dim = 4

    if F == 'F23':
        fobj =F23
        lb = 0
        ub = 10
        dim = 4
    return lb,ub,dim,fobj

def F1(x):
    o = sum(list(map(np.square,x)))
    return o

def F2(x):
    o = sum(abs(x)) + np.prod(abs(x),0)
    return o

def F3(x):
    dim = np.size(x, 0)
    o = 0
    for i   in range(dim):
        o = o + sum(x[:i+1]) ** 2
    return o

def F4(x):
    o = max(abs(x))
    return o

def F5(x):
    dim = np.size(x, 0)#列数
    o = sum(100 * (x[1:dim] - (x[:dim-1]** 2))** 2 + (x[:dim-1] - 1)** 2)
    return o

def F6(x):
    o = sum(abs((x + .5))** 2)
    return o

def F7(x):
    dim = np.size(x, 0)
    new = []
    for i in range(dim):
        new.append(i+1)
    o = sum(new *(x**4))+ random.random()
    return o

def F8(x):
    o = sum(-x * np.sin(np.sqrt(abs(x))))
    return o

def F9(x):
    dim = np.size(x, 0)
    o = sum(x**2 - 10 * np.cos(2 * np.pi * x)) + 10 * dim
    return o

def F10(x):
    dim = np.size(x, 0)

    o = -20 * np.exp(-.2 * np.sqrt(sum(x** 2) / dim)) - np.exp(sum(np.cos(2 * np.pi * x)) / dim) + 20 + np.exp(1)
    return o

def F11(x):
    dim = np.size(x, 0)
    new = []
    for i in range(dim):
        new.append(i + 1)
    o = sum(x** 2) / 4000 - np.prod(np.cos(x  / np.sqrt(new)))+1
    return o
    
def F12(x):
    dim = np.size(x, 0)
    o = (np.pi / dim) * (10 * ((np.sin(np.pi * (1 + (x[0]+ 1) / 4))) ^ 2) + sum((((x[:dim-1] + 1)  / 4)** 2) *  (1 + 10. * ((np.sin(np.pi * (1 + (x[1:dim] + 1) / 4))))** 2))+((x[dim] + 1) / 4) ^ 2)+sum(Ufun(x, 10, 100, 4))
    return o

def F13(x):
    dim = np.size(x, 0)
    o = .1 * ((np.sin(3 * np.pi * x[0])) ^ 2 + sum((x[:dim-1] - 1)** 2. * (1 + (np.sin(3. * np.pi * x[1:dim]))** 2))+ ((x[dim] - 1) ** 2) * (1 + (np.sin(2 * np.pi * x[dim])) ** 2))+sum(Ufun(x, 5, 100, 4))
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
    bK = [.25, .5, 1, 2, 4, 6 ,8 ,10, 12 ,14, 16]
    bK = 1. / bK
    o = sum((aK - ((x[0] * (bK** 2 + x[1] * bK)) / (bK** 2 + x[2] * bK + x[3])))** 2)
    return o

def F16(x):
    o = 4 * (x[0] ^ 2) - 2.1 * (x[0] ^ 4) + (x[0] ^ 6) / 3 + x[0] * x[1] - 4 * (x[1] ^ 2) + 4 * (x[1] ^ 4)
    return o

def F17(x):
    o = (x[1] - (x[0] ** 2) * 5.1 / (4 * (np.pi ** 2)) + 5 / np.pi * x[0] - 6) ** 2 + 10 * (1 - 1 / (8 * np.pi)) * np.cos(x[0]) + 10
    return o

def F18(x):
    o = (1 + (x[0] + x[1] + 1) ^ 2 * (19 - 14 * x[0] + 3 * (x[0] ^ 2) - 14 * x[1] + 6 * x[0] * x[1] + 3 * x[1] ^ 2)) *  (30 + (2 * x[0] - 3 * x[1]) ^ 2 * (18 - 32 * x[0] + 12 * (x[0] ^ 2) + 48 * x[1] - 36 * x[0] * x[1] + 27 * (x[1] ^ 2)))
    return o

def F19(x):
    aH = [3,10,30,.1,10,35,3,10,30,.1,10,35]
    cH = [1,1.2, 3, 3.2]
    pH = [.3689,.117, .2673,.4699,.4387,.747,.1091,.8732,.5547,.03815,.5743,.8828]
    o = 0
    for i in range(4):
        o = o - cH[i] * np.exp(-(sum(aH[i,:] * ((x - pH[i,:])** 2))))
    return o

def F20(x):
    aH = [10,3, 17, 3.5, 1.7, 8,.05,10,17,.1,8,14,3,3.5,1.7,10,17,8,17,8,.05,10,.1,14]
    cH = [1,1.2 ,3, 3.2]
    pH = [.1312,.1696, .5569, .0124, .8283, .5886,.2329,.4135,.8307,.3736,.1004,.9991,.2348,.1415,.3522,.2883,.3047,.6650,.4047,.8828,.8732,.5743,.1091,.0381]
    o = 0
    for i in range(4):
        o = o - cH[i] * np.exp(-(sum(aH[i,:] * ((x - pH[i,:])** 2))))
    return o

def F21(x):
    aSH = [4,4,4, 4,1,1,1,1,8,8,8,8,6,6,6,6,3,7,3,7,2,9,2,9,5,5,3,3,8,1,8,1,6,2,6,2,7,3.6,7,3.6]
    cSH = [.1, .2, .2 ,.4, .4, .6,.3,.7, .5, .5]
    o = 0
    for i in range(5):
        o = o - ((x - aSH[i,:]) * (x - aSH[i,:])+cSH[i])**(-1)
    return o

def F22(x):
    aSH = [4,4,4,4,1,1,1,1,8,8,8,8,6,6,6,6,3,7,3,7,2,9,2,9,5,5,3,3,8,1,8,1,6,2,6,2,7,3.6,7,3.6]
    cSH = [.1,.2 ,.2, .4, .4, .6,.3, .7 ,.5, .5]
    o = 0
    for i in range(7):
        o = o - ((x - aSH[i,:]) * (x - aSH[i,:])+cSH[i])**(-1)
    return o

def F23(x):
    aSH = [4,4,4,4,1,1,1,1,8,8,8,8,6,6,6,6,3,7,3,7,2,9,2,9,5,5,3,3,8,1,8,1,6,2,6,2,7,3.6,7,3.6]
    cSH = [.1,.2,.2, .4,.4 ,.6 ,.3 ,.7, .5 ,.5]
    o = 0
    for i in range(10):
        o = o - ((x - aSH[i,:]) * (x - aSH[i,:])+cSH[i])**(-1)
    return o

def Ufun(x, a, k, m):
    o = k * ((x - a)** m) * (x > a) + k * ((-x - a)** m) * (x < (-a))
    return o

def fun_plot(fun_name):
    lowerbound, upperbound, dimension, fitness = BenchmarkFunctions(fun_name)
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

