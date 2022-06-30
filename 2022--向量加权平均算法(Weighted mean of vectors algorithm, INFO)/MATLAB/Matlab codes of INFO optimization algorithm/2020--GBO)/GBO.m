%---------------------------------------------------------------------------------------------------------------------------
%  Author, inventor and programmer: Iman Ahmadianfar,
%  Assistant Professor, Department of Civil Engineering, Behbahan Khatam Alanbia University of Technology, Behbahan, Iran

%  Researchgate: https://www.researchgate.net/profile/Iman_Ahmadianfar

%  e-Mail: im.ahmadian@gmail.com, i.ahmadianfar@bkatu.ac.ir,
%---------------------------------------------------------------------------------------------------------------------------
%  Co-author:
%             Omid Bozorg-Haddad(OBHaddad@ut.ac.ir)
%             Xuefeng Chu(xuefeng.chu@ndsu.edu) 
%---------------------------------------------------------------------------------------------------------------------------
% Please refer to the main paper:
% Gradient-Based Optimizer: A New Metaheuristic Optimization Algorithm
% SIman Ahmadianfar, Omid Bozorg-Haddad, Xuefeng Chu
% Information Sciences,2020
% DOI: https://doi.org/10.1016/j.ins.2020.06.037
% https://www.sciencedirect.com/science/article/pii/S0020025520306241
% ------------------------------------------------------------------------------------------------------------
% Website of GBO: http://imanahmadianfar.com/
% You can find and run the GBO code online at http://imanahmadianfar.com/

% You can find the GBO paper at https://doi.org/10.1016/j.ins.2020.06.037
% Please follow the paper for related updates in researchgate: https://www.researchgate.net/profile/Iman_Ahmadianfar
%--------------------------------------------------------------------------------------------------------------------------- 
%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [Best_Cost,Best_X,Convergence_curve]=GBO(nP,MaxIt,lb,ub,dim,fobj)
%% Initialization
nV = dim;                        % Number f Variables
pr = 0.5;                        % Probability Parameter
lb = ones(1,dim).*lb;            % lower boundary 
ub = ones(1,dim).*ub;            % upper boundary
Cost = zeros(nP,1);
X = initialization(nP,nV,ub,lb); %Initialize the set of random solutions
Convergence_curve = zeros(1,MaxIt);

for i=1:nP
    Cost(i) = fobj(X(i,:));      % Calculate the Value of Objective Function
end

[~,Ind] = sort(Cost);     
Best_Cost = Cost(Ind(1));        % Determine the vale of Best Fitness
Best_X = X(Ind(1),:);
Worst_Cost=Cost(Ind(end));       % Determine the vale of Worst Fitness
Worst_X=X(Ind(end),:);
%% Main Loop
for it=1:MaxIt
    
    beta = 0.2+(1.2-0.2)*(1-(it/MaxIt)^3)^2;                        % Eq.(14.2)
    alpha = abs(beta.*sin((3*pi/2+sin(3*pi/2*beta))));              % Eq.(14.1)

    for i=1:nP                
        A1 = fix(rand(1,nP)*nP)+1;                                  % Four positions randomly selected from population        
        r1 = A1(1);r2 = A1(2);   
        r3 = A1(3);r4 = A1(4);        
        
        Xm = (X(r1,:)+X(r2,:)+X(r3,:)+X(r4,:))/4;                   % Average of Four positions randomly selected from population        
        ro = alpha.*(2*rand-1);ro1 = alpha.*(2*rand-1);        
        eps = 5e-3*rand;                                            % Randomization Epsilon
        
        DM = rand.*ro.*(Best_X-X(r1,:));Flag = 1;                   % Direction of Movement Eq.(18)
        GSR=GradientSearchRule(ro1,Best_X,Worst_X,X(i,:),X(r1,:),DM,eps,Xm,Flag);      
        DM = rand.*ro.*(Best_X-X(r1,:));
        X1 = X(i,:) - GSR + DM;                                     % Eq.(25)
        
        DM = rand.*ro.*(X(r1,:)-X(r2,:));Flag = 2;
        GSR=GradientSearchRule(ro1,Best_X,Worst_X,X(i,:),X(r1,:),DM,eps,Xm,Flag); 
        DM = rand.*ro.*(X(r1,:)-X(r2,:));
        X2 = Best_X - GSR + DM;                                     % Eq.(26)            
        
        Xnew=zeros(1,nV);
        for j=1:nV                                                  
            ro=alpha.*(2*rand-1);                       
            X3=X(i,j)-ro.*(X2(j)-X1(j));           
            ra=rand;rb=rand;
            Xnew(j) = ra.*(rb.*X1(j)+(1-rb).*X2(j))+(1-ra).*X3;     % Eq.(27)          
        end
        
        % Local escaping operator(LEO)                              % Eq.(28)
        if rand<pr           
            k = fix(rand*nP)+1;
            f1 = -1+(1-(-1)).*rand();f2 = -1+(1-(-1)).*rand();         
            ro = alpha.*(2*rand-1);
            Xk = unifrnd(lb,ub,1,nV);%lb+(ub-lb).*rand(1,nV);       % Eq.(28.8)

            L1=rand<0.5;u1 = L1.*2*rand+(1-L1).*1;u2 = L1.*rand+(1-L1).*1;
            u3 = L1.*rand+(1-L1).*1;                                    
            L2=rand<0.5;            
            Xp = (1-L2).*X(k,:)+(L2).*Xk;                           % Eq.(28.7)
                                                 
            if u1<0.5
                Xnew = Xnew + f1.*(u1.*Best_X-u2.*Xp)+f2.*ro.*(u3.*(X2-X1)+u2.*(X(r1,:)-X(r2,:)))/2;     
            else
                Xnew = Best_X + f1.*(u1.*Best_X-u2.*Xp)+f2.*ro.*(u3.*(X2-X1)+u2.*(X(r1,:)-X(r2,:)))/2;   
            end
        end
        
        % Check if solutions go outside the search space and bring them back
        Flag4ub=Xnew>ub;
        Flag4lb=Xnew<lb;
        Xnew=(Xnew.*(~(Flag4ub+Flag4lb)))+ub.*Flag4ub+lb.*Flag4lb;                
        Xnew_Cost = fobj(Xnew);
        % Update the Best Position        
        if Xnew_Cost<Cost(i)
            X(i,:)=Xnew;
            Cost(i)=Xnew_Cost;
            if Cost(i)<Best_Cost
                Best_X=X(i,:);
                Best_Cost=Cost(i);
            end            
        end
       % Update the Worst Position 
        if Cost(i)>Worst_Cost
            Worst_X= X(i,:);
            Worst_Cost= Cost(i);
        end               
    end
    
    Convergence_curve(it) = Best_Cost;
    % Show Iteration Information
    disp(['Iteration ' num2str(it) ': Best Fitness = ' num2str(Convergence_curve(it))]);
end
end
% _________________________________________________
% Gradient Search Rule
function GSR=GradientSearchRule(ro1,Best_X,Worst_X,X,Xr1,DM,eps,Xm,Flag)
    nV = size(X,2);
    Delta = 2.*rand.*abs(Xm-X);                            % Eq.(16.2)
    Step = ((Best_X-Xr1)+Delta)/2;                         % Eq.(16.1)
    DelX = rand(1,nV).*(abs(Step));                        % Eq.(16)
    
    GSR = randn.*ro1.*(2*DelX.*X)./(Best_X-Worst_X+eps);   % Gradient search rule  Eq.(15)
    if Flag == 1
      Xs = X - GSR + DM;                                   % Eq.(21)
    else
      Xs = Best_X - GSR + DM;
    end    
    yp = rand.*(0.5*(Xs+X)+rand.*DelX);                    % Eq.(22.6)
    yq = rand.*(0.5*(Xs+X)-rand.*DelX);                    % Eq.(22.7)
    GSR = randn.*ro1.*(2*DelX.*X)./(yp-yq+eps);            % Eq.(23)   
end






    
    
    
    




