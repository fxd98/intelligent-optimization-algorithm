import random
import numpy as np
from Fuction import BenchmarkFunctions,initialization,BC

def INFO(nP,MaxIt,lb,ub,dim,fobj):

    #初始化————————————————————————
    Cost =np.zeros([nP,1])
    M = np.zeros([nP, 1])

    X = initialization(nP,dim,ub,lb)

    # 计算适应度值
    for i in range(nP):
        Cost[i] = fobj(X[i,:])
        M[i]       = Cost[i]

    ind = np.argsort(-Cost,0)
    Best_X          = X[ind[0],:]
    Best_Cost   = Cost[ind[0]]

    Worst_X = X[ind[-1], :]
    Worst_Cost = Cost[ind[-1]]

    I = random.randint(1,4)

    Better_X = X[ind[I],:]
    Better_Cost = Cost[ind[I]]
    Convergence_curve =np.zeros([MaxIt,1])

    # 开始了
    for it in range(MaxIt):
        alpha = 2 * np.exp(-4 * (it / MaxIt))        # Eqs.(5.1) & # Eq.(9.1)

        M_Best = Best_Cost
        M_Better = Better_Cost
        M_Worst = Worst_Cost
        for i in range(nP):
            #更新规则阶段
            delt =2 * np.random.rand() * alpha - alpha # Eq.(5)
            sigm = 2 * np.random.rand() * alpha - alpha # Eq.(9)

            # Select three random solution  选择三个随机解
            A_c = np.random.permutation(np.array(range(nP) ))
            A1  = np.delete(A_c, np.where(A_c == i))
            a = A1[0]
            b = A1[1]
            c = A1[2]

            e = 1e-25
            epsi = e * np.random.rand()
            omg = max([M[a], M[b], M[c]])
            MM = [(M[a] - M[b]),(M[a] - M[c]),(M[b] - M[c])]

            W1 = np.cos(MM[0] + np.pi) * np.exp(-abs(MM[0] / omg)) # Eq.(4.2)
            W2= np.cos(MM[1] + np.pi) * np.exp(-abs(MM[1] / omg)) # Eq.(4.3)
            W3= np.cos(MM[2] + np.pi) * np.exp(-abs(MM[2] / omg)) # Eq.(4.4)
            Wt = sum([W1,W2,W3])

            WM1 = delt *(W1 * (X[a,:] - X[b,:])+W2* (X[a,:] - X[c,:])+ W3* (X[b,:] - X[c,:])) / (Wt + 1) + epsi # Eq.(4.1)


            omg = max([M_Best,M_Better,M_Worst])
            MM = [(M_Best - M_Better),(M_Best - M_Better),(M_Better - M_Worst)]

            W1_2 = np.cos(MM[0] + np.pi) * np.exp(-abs(MM[0] / omg)) # Eq.(4.7)
            W2_2= np.cos(MM[1] + np.pi) * np.exp(-abs(MM[1] / omg)) # Eq.(4.8)
            W3_2= np.cos(MM[2] + np.pi) * np.exp(-abs(MM[2] / omg)) # Eq.(4.9)
            Wt_2 = sum([W1_2,W2_2,W3_2])

            WM2 = delt *(W1_2 * (Best_X - Better_X) + W2_2* (Best_X - Worst_X) + W3_2* (Better_X - Worst_X)) / (Wt_2 + 1) + epsi # Eq.(4.6)


            # Determine  MeanRule
            r = random.random()/2
            MeanRule = r * WM1 + (1 - r) * WM2 # Eq.(4)

            if np.random.rand() < 0.5:
                z1 = X[i,:]+sigm * (np.random.rand() * MeanRule) + np.random.randn() * (Best_X - X[a,:]) / (M_Best - M[a] + 1)
                z2 = Best_X + sigm * (np.random.rand() * MeanRule) + np.random.randn() * (X[a,:] - X[b,:]) / (M[a] - M[b] + 1)
            else: # Eq.(8)
                z1 = X[a,:]+sigm * (np.random.rand() * MeanRule) + np.random.randn() * (X[b,:] - X[c,:]) / (M[b] - M[c] + 1)
                z2 = Better_X + sigm * (np.random.rand() * MeanRule) + np.random.randn() * (X[a,:] - X[b,:]) / (M[a] - M[b] + 1)

            # Vector combining stage 向量结合阶段
            u = np.zeros([1, dim])
            for j in range(dim):
                mu = 0.05 * np.random.randn()
                if np.random.rand() < 0.5:
                    if np.random.rand() < 0.5:
                        u[:,j] = z1[:,j] + mu * abs(z1[:,j] - z2[:,j]) # Eq.(10.1)
                    else:
                        u[:,j] = z2[:,j] + mu * abs(z1[:,j] - z2[:,j]) # Eq.(10.2)
                else:
                    u[:,j] = X[i, j] # Eq.(10.3)

            # Local search stage
            if np.random.rand() < 0.5:
                L = np.random.rand() < 0.5
                v1 = (1 - L) * 2 * (np.random.rand()) + L
                v2 = np.random.rand() * L + (1 - L)                 # Eqs.(11.5) & # Eq.(11.6)
                Xavg = (X[a,:] + X[b,:]+X[c,:]) / 3                     # Eq.(11.4)
                phi = np.random.rand()
                Xrnd = phi * (Xavg) + (1 - phi) * (phi * Better_X + (1 - phi) * Best_X) # Eq.(11.3)
                Randn = L * np.random.randn(1, dim) + (1 - L) * np.random.randn()
                if np.random.rand() < 0.5:
                    u = Best_X + Randn * (MeanRule + np.random.randn() * (Best_X - X[a,:])) # Eq.(11.1)
                else:
                    u = Xrnd + Randn * (MeanRule + np.random.randn() * (v1 * Best_X - v2 * Xrnd)) # Eq.(11.2)

            # Check if new solution go outside the search space and bring them back
            New_X = BC(u, lb, ub)
            New_Cost = fobj(New_X.T)
            if New_Cost < Cost[i]:
                X[i,:]=New_X
                Cost[i] = New_Cost
                M[i] = Cost[i]
                if Cost[i] < Best_Cost:

                    Best_X = X[i,:]
                    Best_Cost = Cost[i]

        # Determine the worst solution
        ind = np.argsort(Cost,0)
        Worst_X = X[ind[-1],:]
        Worst_Cost = Cost[ind[-1]]

        # Determine the better solution
        I = random.randint(2,5)
        Better_X = X[ind[I],:]
        Better_Cost = Cost[ind[I]]


        # Update Convergence_curve
        Convergence_curve[it] = Best_Cost

        # Show Iteration Information
        print(['Iteration ', it, ',: Best Cost = ' ,Best_Cost])

    return Best_Cost,Best_X,Convergence_curve