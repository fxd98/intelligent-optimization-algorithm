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