%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  Honey Badger Algorithm source code 
%  paper:
%     Hashim, Fatma A., Essam H. Houssein, Kashif Hussain, Mai S. %     Mabrouk, Walid Al-Atabany. 
%     "Honey Badger Algorithm: New Metaheuristic Algorithm for %  %     Solving Optimization Problems." 
%     Mathematics and Computers in Simulation, 2021.
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%

clc;clear all;
close all;
fitfun = @sumsqu;
dim=30;
T=1000;
Lb=-10;
Ub=10;
N=30;
[xmin,fmin,CNVG]=HBA(fitfun,dim,Lb,Ub,T,N);
figure,
semilogy(CNVG,'r')
xlim([0 T]);
title('Convergence curve')
xlabel('Iteration');
ylabel('Best fitness obtained so far');
legend('HBA')

display(['The best location= ', num2str(xmin)]);
display(['The best fitness score = ', num2str(fmin)]);

        

