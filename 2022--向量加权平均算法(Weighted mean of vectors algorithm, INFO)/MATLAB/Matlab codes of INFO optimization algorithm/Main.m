%---------------------------------------------------------------------------------------------------------------------------
% weIghted meaN oF vectOrs (INFO)
% INFO: An Efficient Optimization Algorithm based on Weighted Mean of Vectors
% Codes of INFO:http://imanahmadianfar.com/codes/
% Website and codes of INFO:http://www.aliasgharheidari.com/INFO.html

% Iman Ahmadianfar, Ali asghar Heidari, Saeed Noushadian, Huiling Chen, and Amir H. Gandomi 

%  Last update: 01-10-2022

%  e-Mail: im.ahmadian@gmail.com,i.ahmadianfar@bkatu.ac.ir.
%  e-Mail: as_heidari@ut.ac.ir, aliasghar68@gmail.com,
%  
%---------------------------------------------------------------------------------------------------------------------------
%  Authors: Ali Asghar Heidari(as_heidari@ut.ac.ir, aliasghar68@gmail.com),Saeed Noushadian, Huiling Chen(chenhuiling.jlu@gmail.com), and Amir H Gandomi, 
%---------------------------------------------------------------------------------------------------------------------------

% After use, please cite to the main paper:
% Iman Ahmadianfar, Ali asghar Heidari, Saeed Noushadian, Huiling Chen, Amir H. Gandomi  
% INFO: An Efficient Optimization Algorithm based on Weighted Mean of Vectors
% Expert Systems With Applications, 116516, 2022, doi: https://doi.org/10.1016/j.eswa.2022.116516 (Q1, 5-Year Impact Factor: 6.95)
%---------------------------------------------------------------------------------------------------------------------------
% You can also follow the paper for related updates in researchgate: 
% https://www.researchgate.net/profile/Iman_Ahmadianfar
% https://www.researchgate.net/profile/Ali_Asghar_Heidari.

%  Website and codes of INFO:%  http://www.aliasgharheidari.com/INFO.html

% You can also use and compare with our other new optimization methods:
                                                                       %(INFO)-2020-http://www.imanahmadianfar.com/codes.
                                                                       %(GBO)-2020-http://www.imanahmadianfar.com/codes.
                                                                       %(INFO)-2022- http://www.aliasgharheidari.com/INFO.html
																	   %(RUN)-2021- http://www.aliasgharheidari.com/RUN.html
                                                                       %(HGS)-2021- http://www.aliasgharheidari.com/HGS.html
                                                                       %(SMA)-2020- http://www.aliasgharheidari.com/SMA.html
                                                                       %(HHO)-2019- http://www.aliasgharheidari.com/HHO.html  

%---------------------------------------------------------------------------------------------------------------------------

clear 
close all
clc

nP=30;          % Number of Population

Func_name='F10'; % Name of the test function, range from F1-F23

MaxIt=500;      % Maximum number of iterations

% Load details of the selected benchmark function
[lb,ub,dim,fobj]=BenchmarkFunctions(Func_name);

[Best_fitness,BestPositions,Convergence_curve] = INFO(nP,MaxIt,lb,ub,dim,fobj);

%% Draw objective space

figure,
hold on
semilogy(Convergence_curve,'Color','r','LineWidth',4);
title('Convergence curve')
xlabel('Iteration');
ylabel('Best fitness obtained so far');
axis tight
grid off
box on
legend('INFO')


