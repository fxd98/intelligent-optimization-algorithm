%% CapSA (Capuchin search Algorithm)
% Citation details:
% Braik, Malik, Alaa Sheta, and Heba Al-Hiary. "A novel meta-heuristic search algorithm for solving 
% optimization problems: Capuchin search algorithm.
% " Neural Computing and Applications (2020): 1-33

% Programmed by Malik Braik
% Al-Balqa Applied University (BAU) %
% Date of programming: 2020 %
% -------------------------------------------------
% This demo only implements a standard version of CapSA for a minimization problem 
% of a standard test function on MATLAB (R2018).
% -------------------------------------------------	
% Note:
% Due to the stochastic nature of meta-heuristc algorithms, 
% different runs may produce slightly different results.
%____________________________________________________________________________________
   
clear 
close all
clc
%% % Prepare the problem
dim = 2;
ub = 50 * ones(1, 2);
lb = -50 * ones(1, 2);
fobj = @Objfun;

%% % CSA parameters 
noP = 10;
maxIter = 5;
  
             [bestFitness, bestPosition, CSAConvCurve] =CapSA(noP,maxIter,lb,ub,dim,fobj);

              disp(['===> The optimal fitness value found by Standard CapSA is ', num2str(bestFitness, 15)]); 

% %% % Draw the objective space
% 
% figure;  set(gcf,'color','w');
% 
% plot(CSAConvCurve,'LineWidth',2,'Color','b'); grid;
% title({'Objective space','(Convergence characteristic)'},'interpreter','latex','FontName','Times','fontsize',10);
% xlabel('Iteration','interpreter','latex','FontName','Times','fontsize',10)
% ylabel('Best score obtained so far','interpreter','latex','FontName','Times','fontsize',10); 
% 
% axis tight; grid on; box on 
%      
% h1=legend('CapSA','location','northeast');
% set(h1,'interpreter','Latex','FontName','Times','FontSize',10) 
% ah=axes('position',get(gca,'position'),...
%             'visible','off');