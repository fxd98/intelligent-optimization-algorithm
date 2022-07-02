from Fuction import  Get_Functions_details,COOT
from matplotlib import pyplot as plt

N=30                                # Number of search agents

Function_name='F13' # Name of the test function 

Max_iter=500                # Maximum number of iterations

# Load details of the selected benchmark function
lb,ub,dim,fobj =Get_Functions_details(Function_name)

[Convergence_curve,gBest,gBestScore]=COOT(N,Max_iter,lb,ub,dim,fobj)

print('The best location of COOT is: ', gBest)
print('The best fitness of COOT is: ', gBestScore)

plt.rcParams['font.sans-serif'] = ['SimHei'] # 解决汉字显示为□指定默认字体为黑体。
plt.rcParams['axes.unicode_minus'] = False   # 解决保存图像时 负号'-' 显示为□和报错的问题
#Draw objective space
# plt.subplot(1,2,2)
plt.plot(range(len(Convergence_curve.T)),Convergence_curve.T)

plt.title('Objective space')
plt.xlabel('Iterations')
plt.ylabel('Best score')
plt.grid()
plt.title('COOT')
plt.show()