import numpy as np

def initialization(SearchAgents_no,dim,ub,lb):
    Boundary_no= np.size(np.array(ub))#输出列数

    # 如果所有变量的边界都相等，用户输入一个
    # ub和lb的编号

    if Boundary_no == 1:
        Positions=np.random.rand(SearchAgents_no,dim) * (ub-lb)+lb
    
    if Boundary_no > 1:
        for i in range(dim):
            ub_i=ub(i)
            lb_i=lb(i)
            Positions[:,i] = np.random.rand(SearchAgents_no,1) * (ub_i-lb_i) + lb_i
    
    return Positions

def fobj(F,x):

    if F == 1:
        fobj = sum( x **2)
        lb=-100
        ub=100
        dim=30
        
    if F == 2:
        fobj = sum(abs(x))+abs(x)
        lb=-10
        ub=10
        dim=30
        
    return fobj,lb,ub,dim