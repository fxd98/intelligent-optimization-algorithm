from matplotlib import pyplot as plt
from Function import Get_Functions_details
from utils import TSO_final_version_submit

Particles_no = 3  # Number of search agents

Function_name = 'F1'  # Name of the test function that can be from F1 to F23(Table 1, 2, 3 in the paper)

Max_iter = 10  # Maximum numbef of iterations

# Load details of the selected benchmark function
lb, ub, Dim, fobj = Get_Functions_details(Function_name)

Best_score, Best_pos, TSO_cg_curve = TSO_final_version_submit(Particles_no, Max_iter, lb, ub, Dim, fobj)

# figure('Position', [500 500 660 290])
# # Draw
# search
# space
# subplot(1, 2, 1)
# func_plot(Function_name)
# title('Parameter space')
# xlabel('x_1')
# ylabel('x_2')
# zlabel([Function_name, '( x_1 , x_2 )'])

# Draw objective space
# plt.subplot(1, 2, 2)
plt.plot(range(len(TSO_cg_curve)),TSO_cg_curve, label = 'TSO')
plt.title('Objective space')
plt.xlabel('Iteration')
plt.ylabel('Best score obtained so far')
plt.legend()
plt.show()

print('The best solution obtained by TSO is : ', Best_pos)
print('The best optimal value of the objective funciton found by TSO is : ', Best_score)





