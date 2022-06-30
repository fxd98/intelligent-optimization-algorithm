import numpy as np
from utils import initialization,fobj

def SCSO(SearchAgents_no,Max_iter,lb,ub,dim,fobj):
    BestFit = np.zeros([1,dim])
    Best_Score=np.inf
    Positions=initialization(SearchAgents_no,dim,ub,lb)
    Convergence_curve=np.zeros([1,Max_iter])
    t=0
    # p=[1:360]##似乎定义的不对
    p = np.random.randint(360)

    while t <= Max_iter:
        for i in range(np.size(Positions)):
            # 初始化参数
            Flag4ub=Positions[i,:]>ub
            Flag4lb=Positions[i,:]<lb
            Positions[i,:]=(Positions[i,:] * ( not (Flag4ub+Flag4lb)))+ub * Flag4ub+lb * Flag4lb

            fitness,_,_,_=fobj(1,Positions[i,:])
        
        S=2;                                    #听觉特性
        rg=S-((S)*t/(Max_iter));                # guides R

        for i in range(np.size((Positions,0))):
            # rand = 
            r=np.random.random() * rg
            R=((2*rg)*np.random.random())-rg                 #   controls to transtion phases  
            
            for j in range(np.size(Positions,1)):
                teta=p
                if((-1<=R) and (R<=1)):              # R value is between -1 and 1
                    Rand_position= abs(np.random.random() * BestFit(j)-Positions(i,j))
                    Positions[i,j]=BestFit(j)-r * Rand_position * np.cos(teta)
                else:                 
                        cp=np.floor(SearchAgents_no * np.random.random()+1)
                        CandidatePosition =Positions[cp,:]
                        Positions[i,j]=r * (CandidatePosition(j)-np.random.random()*Positions[i,j])
    t=t+1
    Convergence_curve[t]=Best_Score

    return Best_Score,BestFit,Convergence_curve
