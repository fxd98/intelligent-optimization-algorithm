import numpy as np
import random,math
from Function import initialization,RungeKutta

def RUN(nP, MaxIt, lb, ub, dim, fobj):
    Cost = np.zeros([nP, 1]) # Record the Fitness of all Solutions
    X = initialization(nP, dim, ub, lb) # Initialize the set of random solutions
    Xnew2 = np.zeros([1,dim])
    Convergence_curve = np.zeros([MaxIt,1])

    for i in range(nP):
        Cost[i] = fobj(X[i,:]) # Calculate the Value of Objective Function

    Best_Cost = min(Cost) # Determine the Best Solution
    ind   = np.where(Cost == Best_Cost)[1]
    Best_X = X[ind,:]

    Convergence_curve[0] = Best_Cost

    # # Main Loop of RUN
    it = 1 # Number of iterations
    while it < MaxIt:

        f = 20  * np.exp(-(12  * (it / MaxIt))) # (Eq.17.6)
        Xavg = np.mean(X) # Determine    the    Average    of    Solutions

        SF = 2  * (0.5 - np.random.rand(nP,1))  * f # Determine    the    Adaptive    Factor(Eq.17.5)

        for i in range(nP):
            ind_l  = np.where(Cost == min(Cost))[1]
            lBest = X[ind_l,:]

            A, B, C = RndX(nP, i) # Determine    Three    Random    Indices    of    Solutions
            ind1 = np.where([Cost[A][0],Cost[B][0],Cost[C][0]] ==min([Cost[A][0],Cost[B][0],Cost[C][0]]))[0]

            # Determine    Delta    X(Eqs.    11.1    to    11.3)
            gama = random.random()  * (X[i,:] - np.random.rand(1, dim)  * (np.array(ub) - np.array(lb))) * np.exp((-4 * it) / MaxIt)
            Stp = np.random.rand(1, dim)  * ((Best_X - random.random()  * Xavg) + gama)
            DelX = 2 * np.random.rand(1, dim)  * (abs(Stp))

            # Determine    Xb and Xw    for using in Runge Kutta method
            if Cost[i] < Cost[ind1,0]:
                Xb = X[i,:]
                Xw = X[ind1,:]
            else:
                Xb = X[ind1,:]
                Xw = X[i,:]

            SM = RungeKutta(Xb, Xw, DelX,dim) # Search        Mechanism(SM)        of        RUN        based        on        Runge        Kutta        Method

            L = np.random.rand(1, dim) < 0.5
            Xc = L  * X[i,:]+(1 - L)  * X[A,:] # (Eq. 17.3)
            Xm = L  * Best_X + (1 - L)  * lBest # (Eq. 17.4)

            vec = [1, -1]
            flag = np.floor(2 * np.random.random(size=[1, nP]))
            r = vec[int(flag[0,i])] # An        Interger        number

            g = 2 * random.random()
            mu = 0.5 + .1 * np.random.randn(1, dim)

            # Determine        New        Solution        Based        on        Runge        Kutta        Method(Eq.18)
            if random.random() < 0.5:
                Xnew = (Xc + r  * SF[i]  * g  * Xc) + SF[i]  * (SM) + mu  * (Xm - Xc)
            else:
                Xnew = (Xm + r  * SF[i]  * g  * Xm) + SF[i]  * (SM) + mu  * (X[A,:] - X[B,:])

            # Check if solutions        go        outside        the        search        space and bring        them        back
            FU = Xnew > ub
            FL = Xnew < lb
            Xnew = (Xnew  * (~(FU + FL))) + ub  * FU + lb  * FL
            CostNew = fobj(Xnew.T)
            if CostNew < Cost[i]:
                X[i,:]=Xnew
                Cost[i] = CostNew


            # # Enhance dsolution quality(ESQ)(Eq.19)
            if random.random() < 0.5:
                EXP = np.exp(-5 * random.random() * it / MaxIt)
                r = np.floor(Unifrnd(-1, 2, 1, 1))

                u = 2 * np.random.rand(dim,1)
                w = Unifrnd(0, 2, 1, dim)  * EXP # (Eq.19-1)

                [A, B, C] = RndX(nP, i)
                Xavg = (X[A,:] + X[B,:]+X[C,:]) / 3 # (Eq.19-2)

                beta = np.random.rand(1, dim)
                Xnew1 = beta  * (Best_X) + (1 - beta)  * (Xavg) # (Eq.19-3)

                for j in range(dim):
                    if w[0,j]< 1:
                        Xnew2[0,j]= Xnew1[0,j]+ r * w[0,j]* abs((Xnew1[0,j]- Xavg[j]) + np.random.normal())
                    else:
                        Xnew2[0,j]= (Xnew1[0,j]- Xavg[j]) + r * w[0,j]* abs((u[j] * Xnew1[0,j]- Xavg[j]) + np.random.normal())

                FU = Xnew2 > ub
                FL = Xnew2 < lb
                Xnew2 = (Xnew2  * (~(FU + FL))) + ub  * FU + lb  * FL
                CostNew = fobj(Xnew2.T)
                if CostNew < Cost[i]:
                    X[i,:]=Xnew2
                    Cost[i] = CostNew
                else:
                    if random.random() < w[0,random.randint(0,dim-1)]:
                        SM = RungeKutta(X[i,:], Xnew2, DelX,dim)
                        Xnew = (Xnew2 - random.random()  * Xnew2) + SF[i] * (SM + (2 * np.random.rand(1, dim)  * Best_X - Xnew2)) # (Eq. 20)

                        FU = Xnew > ub
                        FL = Xnew < lb
                        Xnew = (Xnew  * (~(FU + FL))) + ub  * FU + lb  * FL
                        CostNew = fobj(Xnew.T)

                        if CostNew < Cost[i]:
                            X[i,:]=Xnew
                            Cost[i] = CostNew

            # End of ESQ
            # # Determine the Best Solution
            if Cost[i] < Best_Cost:
                Best_X = X[i,:]
                Best_Cost = Cost[i]

        # Save Best Solution at each iteration
        Convergence_curve[it] = Best_Cost
        print('第{}次迭代'.format(it),'最佳适应度值：',Best_Cost)
        it = it + 1
    return Best_Cost, Best_X, Convergence_curve

# A funtion to determine a random number
# with uniform distribution (unifrnd function in Matlab)
def Unifrnd(a, b, c, dim):
    a2 = a / 2
    b2 = b / 2
    mu = a2 + b2
    sig = b2 - a2
    z = mu + sig  * (2 * np.random.rand(c, dim) - 1)
    return z

# A function to determine thress random indices of solutions
def RndX(nP, i):
    Qi = np.random.permutation(np.array(range(nP)))
    Qi = np.delete(Qi,np.where(Qi == i))
    A = Qi[0]
    B = Qi[1]
    C = Qi[2]
    return A, B, C












