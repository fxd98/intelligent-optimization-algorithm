 % Hunger Games Search (HGS)
% Visions, Conception, Implementation, Deep Analysis, Perspectives, and Towards Performance Shifts
% Website of HGS: http://www.aliasgharheidari.com/HGS.html

%  Yutao Yang and Professor Huiling Chen (citations above 7000) and Ali Asghar Heidari (citations above 4000)
%  College of Computer Science and Artificial Intelligence, Wenzhou University, Wenzhou, Zhejiang 325035, China
%  Exceptionally Talented Researcher, Department of Computer Science, School of Computing, National University of Singapore, Singapore
%  National Elite, Exceptionally Talented Researcher, School of Surveying and Geospatial Engineering, College of Engineering, University of Tehran, Tehran 1439957131, Iran

%  Thanks to Professor Amir H Gandomi (citations above 19000)
%  Faculty of Engineering & Information Technology, University of Technology Sydney, NSW 2007, Australia

%  Last update: 02-17-2021

%  e-Mail: yutaoyang.style@foxmail.com,
%  e-Mail: as_heidari@ut.ac.ir, aliasghar68@gmail.com,
%  e-Mail (Singapore): aliasgha@comp.nus.edu.sg, t0917038@u.nus.edu
%---------------------------------------------------------------------------------------------------------------------------
%  Co-author: Yutao Yang(yutaoyang.style@foxmail.com), Huiling Chen(chenhuiling.jlu@gmail.com), Ali Asghar Heidari(as_heidari@ut.ac.ir), Amir H Gandomi(a.h.gandomi@gmail.com)
%---------------------------------------------------------------------------------------------------------------------------

% After use, please refer to the main paper:
% Yutao Yang, Huiling Chen, Ali Asghar Heidari, Amir H Gandomi, 
% Hunger Games Search: Visions, Conception, Implementation, Deep Analysis, Perspectives, and Towards Performance Shifts
% Expert Systems With Applications, https://doi.org/10.1016/j.eswa.2021.114864 (Q1, 5-Year Impact Factor: 5.448, H-INDEX: 184)
%---------------------------------------------------------------------------------------------------------------------------

%  Researchgate: https://www.researchgate.net/profile/Ali_Asghar_Heidari
%  Website of HGS: http://www.aliasgharheidari.com/HGS.html

% You can also use and compare with our other new optimization methods: (HHO)-2019- http://www.aliasgharheidari.com/HHO.html
%                                                                       (SMA)-2020- http://www.aliasgharheidari.com/SMA.html
%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

clear all %#ok<CLALL>
close all
clc

N=3; % Number of search agents

Function_name='F11'; % Name of the test function, range from F1-F13

FEs=10; % Maximum number of evaluation times

dimSize = 3;   %dimension size

% Load details of the selected benchmark function
[lb,ub,dim,fobj]=Get_Functions_HGS(Function_name,dimSize);

[Destination_fitness,bestPositions,Convergence_curve]=HGS(N,FEs,lb,ub,dim,fobj);


%Draw objective space
figure,
hold on
semilogy(Convergence_curve,'Color','b','LineWidth',4);
title('Convergence curve')
xlabel('Iteration');
ylabel('Best fitness obtained so far');
axis tight
grid off
box on
legend('HGS')

display(['The best location of HGS is: ', num2str(bestPositions)]);
display(['The best fitness of HGS is: ', num2str(Destination_fitness)]);

        



