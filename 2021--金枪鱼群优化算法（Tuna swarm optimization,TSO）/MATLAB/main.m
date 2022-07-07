%___________________________________________________________________%
%                    Tuna swarm optimization (TSO)                  %
%                                                                   %
% Developed in MATLAB R2016b                                        %
%                                                                   %
% Author and programmer: Andi Tang                                  %
%                                                                   %
%         E-mail: 418932433@qq.com                                  %
%                 andisu_afeu@163.com                               %
%                                                                   %
% Main paper: Tuna swarm optimization: A novel swarm-based            %
%             metaheuristic algorithm for global optimization       %
%               DOI: 10.1155/2021/9210050                                                    %
%             Computational Intelligence and Neuroscience%
%                                                                   %
%                                                                   %
%___________________________________________________________________%

% To run TSO: [Best_score,Best_pos,TSO_cg_curve]=TSO_final_version_submit(Particles_no,Max_iter,lb,ub,Dim,fobj);
%__________________________________________

clear all 
clc

Particles_no=30; % Number of search agents

Function_name='F1'; % Name of the test function that can be from F1 to F23 (Table 1,2,3 in the paper)

Max_iter=500; % Maximum numbef of iterations

% Load details of the selected benchmark function
[lb,ub,Dim,fobj]=Get_Functions_details(Function_name);

[Best_score,Best_pos,TSO_cg_curve]=TSO_final_version_submit(Particles_no,Max_iter,lb,ub,Dim,fobj);

figure('Position',[500 500 660 290])
%Draw search space
subplot(1,2,1);
func_plot(Function_name);
title('Parameter space')
xlabel('x_1');
ylabel('x_2');
zlabel([Function_name,'( x_1 , x_2 )'])

%Draw objective space
subplot(1,2,2);
semilogy(TSO_cg_curve,'Color','r')
title('Objective space')
xlabel('Iteration');
ylabel('Best score obtained so far');

axis tight
grid on
box on
legend('TSO')

display(['The best solution obtained by TSO is : ', num2str(Best_pos)]);
display(['The best optimal value of the objective funciton found by TSO is : ', num2str(Best_score)]);

        



