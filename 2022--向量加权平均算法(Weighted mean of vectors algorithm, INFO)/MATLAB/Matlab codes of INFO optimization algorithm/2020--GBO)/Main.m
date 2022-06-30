%---------------------------------------------------------------------------------------------------------------------------
%  Author, inventor and programmer: Iman Ahmadianfar,
%  Assistant Professor, Department of Civil Engineering, Behbahan Khatam Alanbia University of Technology, Behbahan, Iran

%  Researchgate: https://www.researchgate.net/profile/Iman_Ahmadianfar

%  e-Mail: im.ahmadian@gmail.com, i.ahmadianfar@bkatu.ac.ir,
%---------------------------------------------------------------------------------------------------------------------------
%  Co-author:
%             Omid Bozorg-Haddad(OBHaddad@ut.ac.ir)
%             Xuefeng Chu(xuefeng.chu@ndsu.edu) 
%---------------------------------------------------------------------------------------------------------------------------
% Please refer to the main paper:
% Gradient-Based Optimizer: A New Metaheuristic Optimization Algorithm
% Iman Ahmadianfar, Omid Bozorg-Haddad, Xuefeng Chu
% Information Sciences,2020
% DOI: https://doi.org/10.1016/j.ins.2020.06.037
% https://www.sciencedirect.com/science/article/pii/S0020025520306241
% ------------------------------------------------------------------------------------------------------------
% Website of GBO: http://imanahmadianfar.com/
% You can find and run the GBO code online at http://imanahmadianfar.com/

% You can find the GBO paper at https://doi.org/10.1016/j.ins.2020.06.037
% Please follow the paper for related updates in researchgate: https://www.researchgate.net/profile/Iman_Ahmadianfar
%---------------------------------------------------------------------------------------------------------------------------
%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

clear 
close all
clc

nP=50;          % Number of Population

Func_name='F1'; % Name of the test function, range from F1-F14

MaxIt=500;      % Maximum number of iterations

% Load details of the selected benchmark function
[lb,ub,dim,fobj]=BenchmarkFunctions(Func_name);

[Best_fitness,BestPositions,Convergence_curve] = GBO(nP,MaxIt,lb,ub,dim,fobj);

%% Plots
figure,
hold on
semilogy(Convergence_curve,'Color','b','LineWidth',3);
title('Convergence curve')
xlabel('Iteration');
ylabel('Best fitness obtained so far');
axis tight
grid off
box on
legend('GBO')

























