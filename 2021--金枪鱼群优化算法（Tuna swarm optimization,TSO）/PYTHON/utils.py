import numpy as np
import random
from Function import initialization


def TSO_final_version_submit(Particles_no,Max_iter,Low,Up,Dim,fobj):
    Tuna1 = np.zeros([Dim,1])
    Tuna1_fit = np.inf
    T = initialization(Particles_no, Dim, Up, Low)
    fitness = np.ones([np.size(T, 0),1])
    Convergence_curve = np.ones([Max_iter+1,1])
    Iter = 0
    aa = 0.7
    z = 0.05
    while Iter < Max_iter:
        print('迭代数：',Iter)
        C = Iter / Max_iter
        a1 = aa + (1 - aa) * C          #公式3
        a2 = (1 - aa) - (1 - aa) * C    #公式4
        for i in range(np.size(T, 0)):
            Flag4ub = T[i,:] > Up
            Flag4lb = T[i,:] < Low
            T[i,:]=(T[i,:]  * (~(Flag4ub + Flag4lb)))+Up  * Flag4ub + Low  * Flag4lb
            t = fobj(T[i,:])
            fitness[i] = t
            t_pos = T[i,:]
            print('是否更改适应度值：',fitness[i] < Tuna1_fit,fitness[i] , Tuna1_fit)
            if t < Tuna1_fit:
                Tuna1_fit = t
                Tuna1 = t_pos

        # ---------------- Memory saving - ------------------
        if Iter == 0:
            fit_old = fitness
            C_old = T

        for i in range(Particles_no):
            if fit_old[i] < fitness[i]:
                fitness[i] = fit_old[i]
                T[i,:]=C_old [i,:]

        C_old = T
        fit_old = fitness
        # -------------------------------------------------

        t = (1 - Iter / Max_iter)**(Iter / Max_iter)

        if random.random()< z:
            T[0,:]= (Up[0] - Low[0]) * random.random() + Low[0]
        else:
            if 0.5 < random.random():
                r1 = random.random()
                Beta = np.exp(r1 * np.exp(3 * np.cos(np.pi * ((Max_iter - Iter + 1) / Max_iter)))) * (np.cos(2 * np.pi * r1))
                if C > random.random():
                    T[0,:]=a1  * (Tuna1 + Beta * abs(Tuna1 - T[0,:]))+a2  * T[0,:]  # Equation(8.2)
                else:
                    IndivRand = np.random.rand(1, Dim)  * (Up[0] - Low[0]) + Low[0]
                    T[0,:]=a1  * (IndivRand + Beta * abs(IndivRand - T[i,:]))+a2  * T[0,:]  # Equation(8.1)
            else:
                TF = (random.random() > 0.5) * 2 - 1
                if 0.5 > random.random():
                    T[0,:]=Tuna1 + np.random.rand(1, Dim)  * (Tuna1 - T[0,:])+TF  * t**2  * (Tuna1 - T[0,:])  # Equation(9.1)
                else:
                    T[0,:] =TF  * t**2  * T[0,:]  # Equation(9.2)


        for i in range(1,Particles_no):
            if random.random() < z:
                T[i,:]= (Up[0] - Low[0]) * random.random() + Low[0]
            else:
                if 0.5 < random.random():
                    r1 = random.random()
                    Beta = np.exp(r1 * np.exp(3 * np.cos(np.pi * ((Max_iter - Iter + 1) / Max_iter)))) * (np.cos(2 * np.pi * r1))
                    if C > random.random():
                        T[i,:]=a1  * (Tuna1 + Beta * abs(Tuna1 - T[i,:]))+a2  * T[i - 1,:]  # Equation(8.4)
                    else:
                        IndivRand = np.random.rand(1, Dim)  * (Up[0] - Low[0]) + Low[0]
                        T[i,:]=a1  * (IndivRand + Beta * abs(IndivRand - T[i,:]))+a2  * T[i - 1,:]  # Equation(8.2)
                else:
                    TF = (random.random() > 0.5) * 2 - 1
                    if 0.5 > random.random():
                        T[i,:]=Tuna1 + np.random.rand(1, Dim)  * (Tuna1 - T[i,:])+TF * t**2  * (Tuna1 - T[i,:])  # Equation(9.1)
                    else:
                        T[i,:] = TF * t**2  * T[i,:]  # Equation(9.2)
        Iter = Iter + 1
        Convergence_curve[Iter] = Tuna1_fit
        print('迭代数：',Iter,'适应度值：',Tuna1_fit)
    return Tuna1_fit,Tuna1,Convergence_curve