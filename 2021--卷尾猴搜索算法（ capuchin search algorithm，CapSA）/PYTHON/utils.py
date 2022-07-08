import numpy as np
import random,math

def initialization(SearchAgents,dimension,upperbound,lowerbound):
    Boundary_no = len([upperbound])
    # Boundary_no = np.size(upperbound, 1)        # numnber  of  boundaries

#     如果所有变量的边界相等，用户为ub和lb都输入一个数字
    if Boundary_no == 1:
        X = np.random.rand(SearchAgents,dimension) * (upperbound-lowerbound)+lowerbound

#         如果每个变量有不同的lb和ub
    if Boundary_no > 1:
        for i in range(dimension):
            ub_i = upperbound[i]
            lb_i   = lowerbound[i]
            X[:,i] = np.random.rand(SearchAgents,1) * (ub_i - lb_i) + lb_i

    return X

def Objfun (z):
    fit = sum ( abs(z) ) + np.prod( abs(z) )
    return fit

def  CapSA(noP, maxite, LB, UB, dim):
    # # # # *1
    # if size(UB, 2) == 1
        # UB = ones(1, dim) * UB
    # LB = ones(1, dim) * LB
    # end

    # if size(UB, 1) == 1
        # UB = ones(dim, 1) * UB
    # LB = ones(dim, 1) * LB
    # end

    # # # CapSA main program
    # f1 = figure(1)
    # set(gcf, 'color', 'w')
    # hold on
    # xlabel('Iteration', 'interpreter', 'latex', 'FontName', 'Times', 'fontsize', 10)
    # ylabel('Fit value', 'interpreter', 'latex', 'FontName', 'Times', 'fontsize', 10)
    # grid
    #
    cg_curve = np.zeros([maxite,1])

    # # # CapSA     initialization
    # Initialize    the    Pos    of    Caps in the    space
    CapPos = initialization(noP, dim, UB, LB)

    v = 0.1 * CapPos # initial    velocity
    v0 = np.zeros([noP, dim])
    CapFit = np.zeros([noP, 1])

    # Calculate    the    Fit    of    initialCaps
    for i in range(noP):
        CapFit[i] = Objfun(CapPos[i,:])

    # Initial    Fit    of    the    random    Pos
    Fit = CapFit
    fitCapSA            = min(CapFit)
    index = np.where(CapFit == fitCapSA)[1]
    fit_best = np.ones([1, 1]) * (fitCapSA+1)


    CapBestPos = CapPos # Best    Pos    initialization
    Pos = CapPos
    gFoodPos = CapPos[index[0],:] # initial    global Pos

    # # # CapSA    Parameters
    bf = 0.70 # Balance    factor
    cr = 11.0 # Modulus    of    elasticity
    g = 9.81

    # CapSA      velocity    updates
    a1 = 1.250
    a2 = 1.5

    beta = [2,11,2]
    wmax = 0.8
    wmin = 0.1

    # # # CapSA    Main    loop
    for t in range(maxite):
        # Life    time    convergence
        tau = beta[0] * np.exp(-beta[1] * t / maxite)**beta[2]
        w = wmax - (wmax - wmin) * (t / maxite)
        fol = np.ceil((noP - 1)  * np.random.rand(noP, 1))

        # CapSA        velocity        update
        for i in range(noP):
            for j in range(dim):
                v[i, j] = w * v[i, j] +  a1 * (CapBestPos[i, j] - CapPos[i, j]) * random.random() + a2 * (gFoodPos[j] - CapPos[i, j]) * random.random()

        # CapSA        Pos        update
        for i in range(noP):
            if i < noP / 2:
                if (random.random() >= 0.1):
                    r = random.random()
                    if r <= 0.15:
                        CapPos[i,:] =  gFoodPos + bf * ((v[i,:]**2) * np.sin(2 * random.random() * 1.5)) / g            # Jumping(Projection)
                    elif  r > 0.15 and r <= 0.30:
                        CapPos[i,:] =  gFoodPos + cr * bf * ((v[i,:]**2) * np.sin(2 * random.random() * 1.5)) / g       # Jumping(Land)
                    elif  r > 0.30 and r <= 0.9:
                        CapPos[i,:] =    CapPos[i,:] +  v[i,:] # Movement          on            the            ground
                    elif r > 0.9 and r <= 0.95:
                        CapPos[i,:] =      gFoodPos + bf * np.sin(random.random() * 1.5) # Swing # Local            search
                    elif r > 0.95:
                        CapPos[i,:] =       gFoodPos + bf * (v[i,:] - v0[i,:]) # Climbing # Local            search            end
                else:
                        CapPos[i,:] =           tau * (LB + random.random() * (UB - LB))

            # Let            the            followers            follow            the            leaders(update            their            Pos)
            elif i >= noP / 2 and i <= noP:
                eps = ((random.random() + 2 * random.random() ) - (3 * random.random() )) / (1 + random.random() )
                Pos[i,:]=gFoodPos + 2 * (CapBestPos[int(fol[i]),:] - CapPos[i,:])*eps +  2 * (CapPos[i,:] - CapBestPos[i,:])*eps

                CapPos[i,:]=(Pos[i,:] + CapPos[i - 1,:]) / 2
        v0 = v

        for i in range(noP): # relocation(Update, np.exploration)
            u = UB - CapPos[i,:] < 0
            l = LB - CapPos[i,:] > 0
            xor = np.zeros([1,np.size(u,1)])
            for j in range(np.size(u,1)):
                if np.logical_xor(u,l)[0,j] == True:
                    xor[0,j] =0
                else:
                    xor[0, j] = 1
            CapPos[i,:]= LB  * l + UB  * u + CapPos[i,:] *xor
            CapFit[i] = Objfun(CapPos[i,:])

            if CapFit[i] < Fit[i]:
                CapBestPos[i,:]=CapPos[i,:]
                Fit[i] = CapFit[i]

        # # Evaluate        the        new        Pos
        fmin = min(Fit) # finding        out        the        best        Pos
        index = np.where(Fit==fmin)[1]

        # Updating        gPos and best        Fit
        if fmin < fit_best[0,0]:
            gFoodPos = CapBestPos[index[0],:] # Update            the            global best            Pos
            fit_best[0,0] = fmin
        # Obtain        the        convergence        curve
        cg_curve[t] = fit_best[0,0]
    return fitCapSA, CapPos, cg_curve