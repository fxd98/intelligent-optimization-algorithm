from utiles import fun_info,NGO,fun_plot
from matplotlib import  pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

SearchAgents=30
Fun_name='F2'
Max_iterations=600
lowerbound,upperbound,dimension,fitness=fun_info(Fun_name)
Score,Best_pos,NGO_curve=NGO(SearchAgents,Max_iterations,lowerbound,upperbound,dimension,fitness)
# print('NGO_curve',NGO_curve.T.shape,NGO_curve.T)

fig = plt.figure()
ax1 = plt.axes(projection='3d')

ax1 = plt.axes(projection='3d')
x,y,f = fun_plot(Fun_name)
X,Y = np.meshgrid(x,y)
plt.contourf(X,Y,f)
plt.contour(X, Y, f)

#作图
ax1.plot_surface(X,Y,f,alpha=0.3,cmap='winter')     #生成表面， alpha 用于控制透明度
ax1.contour(X,Y,f,zdir='z', offset=-3,cmap="rainbow")  #生成z方向投影，投到x-y平面
ax1.contour(X,Y,f,zdir='x', offset=-6,cmap="rainbow")  #生成x方向投影，投到y-z平面
ax1.contour(X,Y,f,zdir='y', offset=6,cmap="rainbow")   #生成y方向投影，投到x-z平面
#作图
ax1.plot_surface(X,Y,f,alpha=0.3,cmap='winter')     #生成表面， alpha 用于控制透明度
ax1.contour(X,Y,f,zdir='z', offset=-3,cmap="rainbow")  #生成z方向投影，投到x-y平面
ax1.contour(X,Y,f,zdir='x', offset=-6,cmap="rainbow")  #生成x方向投影，投到y-z平面
ax1.contour(X,Y,f,zdir='y', offset=6,cmap="rainbow")   #生成y方向投影，投到x-z平面
plt.show()

plt.plot(range(Max_iterations),NGO_curve)
plt.ylim([0,2.1717036e-149])
plt.title('Objective space')
plt.xlabel('Iterations')
plt.ylabel('Best score')
plt.title('NGO')
plt.show()

# print('The best solution obtained by NGO is : ', Best_pos,Best_pos.shape)
print('The best optimal value of the objective funciton found by NGO is : ', Score)

