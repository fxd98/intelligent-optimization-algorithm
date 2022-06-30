%___________________________________________________________________%                                                           %
%  Gradien-Based Optimizer source code (Developed in MATLAB R2017a) %
%                                                                   %
%  programming: Iman Ahmadianfar                                    %
%                                                                   %
%         e-Mail: im.ahmadian@gmail.com                             %
%                 i.ahmadianfar@bkatu.ac.ir                         %
%                                                                   %
% Source codes demo version 1.0
% ------------------------------------------------------------------------------------------------------------
% Main paper (Please refer to the main paper):
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
% ------------------------------------------------------------------------------------------------------------
%  Co-author:
%             Omid Bozorg-Haddad(OBHaddad@ut.ac.ir)
%             Xuefeng Chu(xuefeng.chu@ndsu.edu)           
% _____________________________________________________
%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% This function initialize the first population 
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
        X(:,i)=rand(nP,1).*(ub(i)-lb(i))+lb(i);
    end
end