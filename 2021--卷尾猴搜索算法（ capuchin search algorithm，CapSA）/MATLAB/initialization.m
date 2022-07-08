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

% This function initialize the first population of chameleons
function pos=initialization(searchAgents,dim,u,l)

% number of boundaries
Bound_no= size(u,1); 

% If the boundaries of all variables are equal, and user enters a signle number for both u and l
if Bound_no==1
    pos=rand(searchAgents,dim).*(u-l)+l;
end

% If each variable has a different boundary l and u
if Bound_no>1
    for i=1:dim
        u_i=u(i);
        l_i=l(i);
        pos(:,i)=rand(searchAgents,1).*(u_i-l_i)+l_i;
    end
end

