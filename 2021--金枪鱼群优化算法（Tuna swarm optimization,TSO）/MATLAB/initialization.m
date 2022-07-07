%___________________________________________________________________%
%                    Tuna swarm optimization (TSO)                  %
%                                                                   %
% Developed in MATLAB R2016b                                        %
%                                                                   %
% Author and programmer: Andi Tang                                  %
%                                                                   %
%         E-mail: 418932433@qq.com                                  %
%                 andisu_afeu@163.com                               %
%                                                                   %
% Main paper: Tuna swarm optimization: A novel swarm-based            %
%             metaheuristic algorithm for global optimization       %
%               DOI: 10.1155/2021/9210050                                                    %
%             Computational Intelligence and Neuroscience%
%                                                                   %
%                                                                   %
%___________________________________________________________________%

% This function initialize the first population of search agents
function Positions=initialization(SearchAgents_no,dim,ub,lb)

Boundary_no= size(ub,2); % numnber of boundaries

% If the boundaries of all variables are equal and user enter a signle
% number for both ub and lb
if Boundary_no==1
    Positions=rand(SearchAgents_no,dim).*(ub-lb)+lb;
end

% If each variable has a different lb and ub
if Boundary_no>1
    for i=1:dim
        ub_i=ub(i);
        lb_i=lb(i);
        Positions(:,i)=rand(SearchAgents_no,1).*(ub_i-lb_i)+lb_i;
    end
end