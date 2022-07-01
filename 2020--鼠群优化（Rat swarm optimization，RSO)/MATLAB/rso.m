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

function[Score,Position,Convergence]=rso(Search_Agents,Max_iterations,Lower_bound,Upper_bound,dimension,objective)
Position=zeros(1,dimension);
Score=inf; 
Positions=init(Search_Agents,dimension,Upper_bound,Lower_bound);
Convergence=zeros(1,Max_iterations);
l=0;
x = 1;
y = 5;
R = floor((y-x).*rand(1,1) + x);
while l<Max_iterations
    for i=1:size(Positions,1)  
        
        Flag4Upper_bound=Positions(i,:)>Upper_bound;
        Flag4Lower_bound=Positions(i,:)<Lower_bound;
        Positions(i,:)=(Positions(i,:).*(~(Flag4Upper_bound+Flag4Lower_bound)))+Upper_bound.*Flag4Upper_bound+Lower_bound.*Flag4Lower_bound;               
        
        fitness=objective(Positions(i,:));
        
        if fitness<Score 
            Score=fitness; 
            Position=Positions(i,:);
        end
        
    end
   
    A=R-l*((R)/Max_iterations); 
    
    for i=1:size(Positions,1)
        for j=1:size(Positions,2)     
            C=2*rand();          
            P_vec=A*Positions(i,j)+abs(C*((Position(j)-Positions(i,j))));                   
            P_final=Position(j)-P_vec;
            Positions(i,j)=P_final;
            
        end
    end
    l=l+1;    
    Convergence(l)=Score;
end
