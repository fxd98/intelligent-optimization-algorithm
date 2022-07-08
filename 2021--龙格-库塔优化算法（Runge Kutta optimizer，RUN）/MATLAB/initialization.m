%---------------------------------------------------------------------------------------------------------------------------

% RUNge Kutta optimizer (RUN)
% RUN Beyond the Metaphor: An Efficient Optimization Algorithm Based on Runge Kutta Method
% Codes of RUN:http://imanahmadianfar.com/codes/
% Website of RUN:http://www.aliasgharheidari.com/RUN.html

% Iman Ahmadianfar, Ali asghar Heidari, Amir H. Gandomi , Xuefeng  Chu, and Huiling Chen  

%  Last update: 04-22-2021

%  e-Mail: im.ahmadian@gmail.com,i.ahmadianfar@bkatu.ac.ir.
%  e-Mail: as_heidari@ut.ac.ir, aliasghar68@gmail.com,
%  e-Mail (Singapore): aliasgha@comp.nus.edu.sg, t0917038@u.nus.edu
%---------------------------------------------------------------------------------------------------------------------------
%  Co-author: Ali Asghar Heidari(as_heidari@ut.ac.ir),Amir H Gandomi,Xuefeng Chu,(Huiling Chen(chenhuiling.jlu@gmail.com), 
%---------------------------------------------------------------------------------------------------------------------------

% After use, please refer to the main paper:
% Iman Ahmadianfar, Ali Asghar Heidari,Amir H Gandomi,Xuefeng Chu,Huiling Chen,  
% RUN Beyond the Metaphor: An Efficient Optimization Algorithm Based on Runge Kutta Method
% Expert Systems With Applications, 2021, 115079, https://doi.org/10.1016/j.eswa.2021.115079 (Q1, 5-Year Impact Factor: 5.448, H-INDEX: 184)
%---------------------------------------------------------------------------------------------------------------------------
% You can also follow the paper for related updates in researchgate: https://www.researchgate.net/profile/Iman_Ahmadianfar
% Researchgate: https://www.researchgate.net/profile/Ali_Asghar_Heidari.

%  Website of RUN:%  http://www.aliasgharheidari.com/RUN.html

% You can also use and compare with our other new optimization methods:
                                                                       %(GBO)-2020-http://www.imanahmadianfar.com/codes.
                                                                       %(HGS)-2021- http://www.aliasgharheidari.com/HGS.html
                                                                       %(SMA)-2020- http://www.aliasgharheidari.com/SMA.html
                                                                       %(HHO)-2019- http://www.aliasgharheidari.com/HHO.html  
%---------------------------------------------------------------------------------------------------------------------------
% This function initialize the first population of search agents
function X=initialization(nP,dim,ub,lb)

Boundary_no= size(ub,2); % numnber of boundaries

% If the boundaries of all variables are equal and user enter a signle
% number for both ub and lb
if Boundary_no==1
    X=rand(nP,dim).*(ub-lb)+lb;
end

% If each variable has a different lb and ub
if Boundary_no>1
    for i=1:dim
        ub_i=ub(i);
        lb_i=lb(i);
        X(:,i)=rand(nP,1).*(ub_i-lb_i)+lb_i;
    end
end