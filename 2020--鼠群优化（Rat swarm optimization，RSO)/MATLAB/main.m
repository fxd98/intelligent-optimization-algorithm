%_________________________________________________________________________%
%  Rat Swarm Optimizer (RSO)                                              %
%                                                                         %
%  Developed in MATLAB R2019b                                             %
%                                                                         %
%  Designed and Developed: Dr. Gaurav Dhiman                              %
%                                                                         %
%         E-Mail: gdhiman0001@gmail.com                                   %
%                 gaurav.dhiman@ieee.org                                  %
%                                                                         %
%       Homepage: http://www.dhimangaurav.com                             %
%                                                                         %
%  Published paper: G. Dhiman et al.                                      %
%          A novel algorithm for global optimization: Rat Swarm Optimizer %
%               Jounral of Ambient Intelligence and Humanized Computing   %
%               DOI: https://doi.org/10.1007/s12652-020-02580-0           %
%                                                                         %
%_________________________________________________________________________%

clear all 
clc
SearchAgents=30; 
Fun_name='F1';  
Max_iterations=1000; 
[lowerbound,upperbound,dimension,fitness]=fun_info(Fun_name);
[Best_score,Best_pos,SHO_curve]=rso(SearchAgents,Max_iterations,lowerbound,upperbound,dimension,fitness);

figure('Position',[500 500 660 290])
%Draw search space
subplot(1,2,1);
fun_plot(Fun_name);
title('Parameter space')
xlabel('x_1');
ylabel('x_2');
zlabel([Fun_name,'( x_1 , x_2 )'])

%Draw objective space
subplot(1,2,2);
plots=semilogy(SHO_curve,'Color','g');
set(plots,'linewidth',2)
title('Objective space')
xlabel('Iterations');
ylabel('Best score');

axis tight
grid on
box on

legend('RSO')

display(['The best optimal value of the objective function found by RSO is : ', num2str(Best_score)]);

        



