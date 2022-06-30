import numpy as np
import random,math

def Chung_Reynolds(x):
    n = np.size(x,0)
    f = 0
    for i in range(n):
        f = f + (x[i]**2)**2
    objval = f
    return objval

def SO(SearchAgents_no,Max_iteration,fitfun, dim,lb,ub):

    fitness = np.ones([SearchAgents_no,1])
    gbest_t = np.ones([Max_iteration,1])


    # 初始化参数
    vec_flag = [1,-1]
    Threshold = 0.25
    Thresold2 = 0.6
    C1 = 0.5
    C2 = 0.05
    C3 = 2

    # 初始化X
    X = lb + np.random.randn(SearchAgents_no,dim) * (ub - lb)

    # 计算适应度函数值
    for i in range(SearchAgents_no):
        fitness[i] = Chung_Reynolds(X[i,:])

    GYbest = min(fitness)[0]
    gbest    = np.where(fitness == GYbest)[0]

    # 全局最优位置
    X_food = X[gbest,:]

    # 将种群分成两个平等的群体雄性和雌性
    N_m = int(np.round(SearchAgents_no/2))
    N_f    = int(SearchAgents_no - N_m)

    X_m   = X[:N_m,:]
    X_f     = X[N_m:,:]

    fitness_m = fitness[:N_m]
    fitness_f    = fitness[N_m:]

    fitnessBest_m = min(fitness_m)
    gbest_m            = np.where(fitness_m ==  fitnessBest_m)[0]
    fitnessBest_f = min(fitness_f)
    gbest_f = np.where(fitness_f == fitnessBest_f)[0]

    X_best_m = X_f[gbest_m, :]
    X_best_f = X_f[gbest_f,:]

    X_new_m = np.ones([N_m, dim])
    X_new_f   = np.ones([N_m, dim])
    for t in range(Max_iteration):
        Temp = np.exp(-(t / Max_iteration))
        Q = C1 * np.exp((t - Max_iteration)/Max_iteration)
        if Q > 1 :
            Q = 1

        # Exploration Phase (no Food)
        if Q < Threshold:
            for i in range(N_m):
                for j in range(dim):
                    rand_leader_index =round((N_m - 1)* random.random())
                    X_rand_m = X_m[rand_leader_index,:]
                    flag_index = round(random.random())
                    Flag = vec_flag[flag_index]
                    A_m  = np.exp(-fitness_m[rand_leader_index] / (fitness_m[i] + math.e))
                    X_new_m[i,j] = X_rand_m[j] + Flag * C2 * A_m * ((ub - lb) * random.random() + lb)
            for i in range(N_f):
                for j in range(dim):
                    rand_leader_index = round((N_f - 1)* random.random())
                    X_rand_f = X_f[rand_leader_index, :]
                    flag_index = round(random.random())
                    Flag = vec_flag[flag_index]
                    A_f = np.exp(-fitness_f[rand_leader_index] / (fitness_f[i] + math.e))
                    X_new_f[i, j] = X_rand_f[j] + Flag * C2 * A_f * ((ub - lb) * random.random() + lb)
        else:
            if Temp > Thresold2:
                for i in range(N_m):
                    flag_index = round(random.random())
                    Flag            = vec_flag[flag_index]
                    for j in range(dim):
                        X_new_m[i,j] = X_food[:,j] + C3 * Flag * Temp * random.random() * (X_food[:,j] - X_m[i,j])
                for i in range(N_f):
                    flag_index = round(random.random())
                    Flag = vec_flag[flag_index]
                    for j in range(dim):
                        X_new_f[i, j] = X_food[:,j] + C3 * Flag * Temp * random.random() * (X_food[:,j] - X_f[i, j])
            else:
                if random.random() > 0.6:
                    for i in range(N_m):
                        for j in range(dim):
                            FM = np.exp(-(fitnessBest_f) / (fitness_m[i] + math.e))
                            X_new_m[i,j] = X_m[i,j] + C3 * FM * random.random() * (Q * X_best_f[:,j] - X_m[i,j])
                    for i in range(N_f):
                        for j in range(dim):
                            FF = np.exp(-(fitnessBest_m) / (fitness_f[i] + math.e))
                            X_new_f[i,j] = X_f[i,j] + C3 * FF * random.random() * (Q * X_best_m[:,j] - X_f[i,j])
                else:
                    for i in range(N_m):
                        for j in range(dim):
                            Mm = np.exp(-fitness_f[i] / (fitness_m[i] + math.e))
                            X_new_m[i,j] = X_m[i,j] + C3 * random.random() * Mm * (Q * X_f[i,j]-X_m[i,j])
                    for i in range(N_f):
                        for j in range(dim):
                            Mf = np.exp(-fitness_m[i] / (fitness_f[i] + math.e))
                            X_new_f[i,j] = X_f[i,j] + C3 * random.random() * Mf * (Q * X_m[i,j] - X_f[i,j])

                    flag_index = round(random.random())
                    egg = vec_flag[flag_index]
                    if egg == 1:
                        GYworst_m = max(fitness_m)
                        gworst_m    = np.where(fitness_m == GYworst_m)
                        X_new_m[gworst_m,:] = lb + random.random() * (ub - lb)

                        GYworst_f = max(fitness_f)
                        gworst_f = np.where(fitness_f == GYworst_f)
                        X_new_f[gworst_f, :] = lb + random.random() * (ub - lb)
        for j in range(N_m):
            Flag4ub = X_new_m[j,:] > ub
            Flag4lb   = X_new_m[j, :] < lb
            X_new_m[j,:] = (X_new_m[j,:] * (~(Flag4ub + Flag4lb))) + ub * Flag4ub + lb * Flag4lb
            y = Chung_Reynolds(X_new_m[j,:])
            if y < fitness_m[j]:
                fitness_m[j] = y
                X_m[j,:] = X_new_m[j,:]
        Ybest_m = min(fitness_m)
        gbest_m  = np.where(fitness_m == Ybest_m)[0]

        for j in range(N_f):
            Flag4ub = X_new_f[j, :] > ub
            Flag4lb = X_new_f[j, :] < lb
            X_new_f[j, :] = (X_new_f[j, :] * (~(Flag4ub + Flag4lb))) + ub * Flag4ub + lb * Flag4lb
            y = Chung_Reynolds(X_new_f[j, :])
            if y < fitness_f[j]:
                fitness_f[j] = y
                X_f[j, :] = X_new_f[j, :]
        Ybest_f = min(fitness_f)
        gbest_f = np.where(fitness_f == Ybest_f)[0]

        if Ybest_m < fitnessBest_m:
            X_best_m = X_m[gbest_m,:]
            fitnessBest_m = Ybest_m

        if Ybest_f < fitnessBest_f:
            X_best_f = X_f[gbest_f,:]
            fitnessBest_f = Ybest_f
        if Ybest_m < Ybest_f:
            gbest_t[t] = min(Ybest_m)
        else:
            gbest_t[t] = min(Ybest_f)

        if fitnessBest_m < fitnessBest_f:
            GYbest = fitnessBest_m
            X_food = X_best_m
        else:
            GYbest = fitnessBest_f
            X_food = X_best_f

    fval = GYbest
    return X_food, fval,gbest_t