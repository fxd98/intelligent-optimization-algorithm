import random
import numpy as np

#  initialization
def Initialize(nPop,d,lb,ub):
    """
    d  变量维度
    lb 变量的上界
    ub 变量的下界
    """
    rand = np.random.rand(nPop,d)
    for i in range(nPop):
        rand[i,:] = rand[i,:] * (np.array(ub) - np.array(lb)) + np.array(lb)
    return rand

def cal_Tpos(x,d,nPop):
    fit = []
    f= 0
    for i in range(nPop):
        for j in range(d):
            f = f + x[i,j] * x[i,j]
        fit.append(f)
    fit_min = min(fit)
    id = fit.index(fit_min)
    return x[id,:],fit_min

# updating of the hunter
# 公式5
def cal_C(it,MaxIt):
        # C : 探索和开发之间的平衡参数，其值在迭代过程中从1减小到0.02，计算方法如下：
        C = 1 - it * (0.98/MaxIt)
        return C

# 公式 4
def cal_Z(R1,R2,R3,d,C):
    #     Z : 自适应参数
    if R1 < C:
        P =1
        IDX= 0
        IDX_ = 1
    else:
        P=0
        IDX = 1
        IDX_ = 0
    Z = R2 * IDX + R3 * IDX_
    return Z

#公式6
def cal_miu(i,x):
    # 计算每一列的平均值
    i = int(i)
    mean_u = np.average(x[:i, :], 0)
    return mean_u

# 公式7
"""理解应该有错误"""
def cal_Deuc(x,d,nPop,kbest,miu):
    # 计算欧氏距离
    Deuc_all = []
    distance = 0
    global deuc
    for i in range(nPop):
        for j in range(d):
            distance1 = np.power((x[i,j] - miu[j]), 2)
            distance = distance + distance1
        deuc = np.sqrt(distance)
        Deuc_all.append(deuc)
        if i == int(kbest)-1:
            d_kb = deuc
    num = sorted(Deuc_all).index(d_kb)
    return num

# 公式9
def cal_kbest(C  , nPop):
        # 计算Kbest
        kbest = int(C  * nPop)
        return kbest

def HPO(nPop,d,lb,ub,MaxIt,R1,R2,R3):
    # initialization
    X =  Initialize(nPop,d,lb,ub)
    fit = []
    # updating of the hunter and prey
    for iter in range(MaxIt):
        # fitness evaluation
        Tpos,fit_min = cal_Tpos(x=X, d=d, nPop=nPop)
        fit.append(fit_min)

        #公式5
        C = cal_C(iter,MaxIt)
        #公式4
        Z = cal_Z(R1,R2,R3,d,C)
        # R2 = Z

        R5 = random.random()
        beta = 0.5
        for i in range(nPop):
            if R5  < beta:#猎人
                print('定义猎人')
                kbest = round(C * nPop)                               # 公式9
                miu = cal_miu(kbest - 1, x=X)                   # 公式6
                num = cal_Deuc(X,d,nPop,kbest,miu)     # 公式7、10  ####理解应该有错误
                X[i,:] = X[i,:] + 0.5 * ((2 * int(C) * Z * X[num,:]) - X[i,:]) + (2 * (1 - int(C)) * Z * miu - X[i,:])
            else:#猎物
                pass
                R4 = random.uniform(-1,1)
                X[i,:] = Tpos + C * Z  * np.cos(2 * np.pi * R4) * (Tpos - X[i,:])
                print('定义猎物')
    return fit_min

nPop = 30
d          = 30
lb         = np.ones([1,d])  * -100
ub         = np.ones([1,d])  * 100
MaxIt   = 50
R1          = np.random.randn(1)
R2          = np.random.rand()
R3          = np.random.randn(1)

# self.R1     = np.random.random(1)#随机向量
# self.R2     = np.random.random(1)
# self.R3     = random.random()        #随机数

print(HPO(nPop,d,lb,ub,MaxIt,R1,R2,R3))