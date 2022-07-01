%_________________________________________________________________________%
%  Rat Swarm Optimizer (RSO)                                              %
%                                                                         %
%  Developed in MATLAB R2019b                                             %
%                                                                         %
%  Designed and Developed: Dr. Gaurav Dhiman                              %
%                                                                         %
%         E-Mail: gdhiman0001@gmail.com                                   %
%                 gaurav.dhiman@ieee.org                                  %
%                                                                         %
%       Homepage: http://www.dhimangaurav.com                             %
%                                                                         %
%  Published paper: G. Dhiman et al.                                      %
%          A novel algorithm for global optimization: Rat Swarm Optimizer %
%               Jounral of Ambient Intelligence and Humanized Computing   %
%               DOI: https://doi.org/10.1007/s12652-020-02580-0           %
%                                                                         %
%_________________________________________________________________________%

function Pos=init(SearchAgents,dimension,upperbound,lowerbound)

Boundary= size(upperbound,2); 
if Boundary==1
    Pos=rand(SearchAgents,dimension).*(upperbound-lowerbound)+lowerbound;
end

if Boundary>1
    for i=1:dimension
        ub_i=upperbound(i);
        lb_i=lowerbound(i);
        Pos(:,i)=rand(SearchAgents,1).*(ub_i-lb_i)+lb_i;
    end
end