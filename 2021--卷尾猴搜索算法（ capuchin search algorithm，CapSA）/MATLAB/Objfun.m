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

function [ fit ] = Objfun (z)
    fit = sum ( abs(z) ) + prod( abs(z) );
end