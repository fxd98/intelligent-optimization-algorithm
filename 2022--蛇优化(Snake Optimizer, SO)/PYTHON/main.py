from utils import  SO
from matplotlib import  pyplot as plt

fitfun = 'Chung_Reynolds'
dim=30
Max_iteration=1000
SearchAgents_no=30
lb=-100
ub=100
tlt='Chung Reynolds'
i=1
Xfood, Xvalue,CNVG = SO(SearchAgents_no,Max_iteration,fitfun, dim,lb,ub)

plt.figure(figsize=(10,10))
plt.plot(range(Max_iteration),CNVG)
plt.xlim([1,1000])
plt.show()