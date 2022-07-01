import numpy as np

from Fuction import BenchmarkFunctions,RSO,fun_plot
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

SearchAgents=30
Fun_name='F1'  
Max_iterations=10
[lowerbound,upperbound,dimension,fitness]= BenchmarkFunctions(Fun_name)
[Best_score,Best_pos,SHO_curve]=RSO(SearchAgents,Max_iterations,lowerbound,upperbound,dimension,fitness)

plt.rcParams['font.sans-serif'] = ['SimHei'] # 解决汉字显示为□指定默认字体为黑体。
plt.rcParams['axes.unicode_minus'] = False   # 解决保存图像时 负号'-' 显示为□和报错的问题
#Draw objective space
# plt.subplot(1,2,2)
plt.plot(range(Max_iterations),SHO_curve.T)

plt.title('Objective space')
plt.xlabel('Iterations')
plt.ylabel('Best score')
plt.grid()
plt.title('RSO')
plt.show()
print(['The best optimal value of the objective function found by RSO is : ', Best_score])
#Draw search space
# fig = plt.figure()
# ax1 = plt.axes(projection='3d')
# plt.subplot(1,2,1)
# x_ = np.linspace(0,13,1000)
# y_ = 5 * np.sin(x_)
# z_ = 5 * np.cos(x_)
# x,y,f = fun_plot(Fun_name)
# for i in range(np.size(f,0)):
#     ax1.scatter3D(x,y,f[i,:], cmap='Blues')  #绘制散点图
#     ax1.plot3D(x_,y_,z_,'gray')    #绘制空间曲线
#     plt.title('Parameter space 第{}维'.format(i))
#     plt.show()

