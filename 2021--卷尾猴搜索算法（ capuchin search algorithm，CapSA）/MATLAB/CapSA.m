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

function [fitCapSA,CapPos,cg_curve]=CapSA(noP,maxite,LB,UB,dim,fobj)
 
warning off; format long;

%%%%* 1
% if size(UB,2)==1
%     UB=ones(1,dim)*UB;
%     LB=ones(1,dim)*LB;
% end

 
% if size(UB,1)==1
%     UB=ones(dim,1)*UB;
%     LB=ones(dim,1)*LB;
% end

% % % CapSA main program
% f1 =  figure (1);
% set(gcf,'color','w');
% hold on
% xlabel('Iteration','interpreter','latex','FontName','Times','fontsize',10)
% ylabel('Fit value','interpreter','latex','FontName','Times','fontsize',10); 
% grid;
%  
cg_curve=zeros(1,maxite);

%% % CapSA initialization

%Initialize the Pos of Caps in the space
CapPos=initialization(noP,dim,UB,LB);

v=0.1*CapPos;% initial velocity
v0=zeros(noP,dim); 
CapFit=zeros(noP,1);

% Calculate the Fit of initialCaps

    for i=1:noP
        CapFit(i,1)=fobj(CapPos(i,:));
    end
 
% Initial Fit of the random Pos

Fit = CapFit;

[fitCapSA,index]=min(CapFit);

CapBestPos = CapPos; % Best Pos initialization
Pos= CapPos; 
gFoodPos = CapPos(index,:); % initial global Pos 

%% % CapSA Parameters
bf=0.70;%Balance factor
cr=11.0;  %Modulus of elasticity
g=9.81;

% CapSA velocity updates
a1=1.250; a2=1.5;   

beta=[2 11 2];
wmax=0.8;
wmin=0.1;
 
%% % CapSA Main loop
  
for t = 1 : maxite

    % Life time convergence
        tau = beta(1) * exp(-beta(2) * t/maxite)^beta(3);
        w   = wmax-(wmax-wmin)*(t/maxite); 
        fol=ceil((noP-1).*rand(noP,1))'; %  

        % CapSA velocity update
for i=1:noP 
    for j=1:dim
        v(i,j)=  w* v(i,j) + ...
                           a1*(CapBestPos(i,j)- CapPos(i,j))*rand + ...
                           a2*(gFoodPos(j)  - CapPos(i,j))*rand;      
    end
end
     
% CapSA Pos update

for i=1:noP
   if i<noP/2
          if (rand()>=0.1)
               r=rand;
              if r<=0.15
                 CapPos(i,:) =  gFoodPos +    bf*((v(i,:).^2)*sin(2*rand()*1.5))/g;  % Jumping (Projection)
              elseif   r>0.15 && r<=0.30  
                  CapPos(i,:) =  gFoodPos +   cr*bf*((v(i,:).^2)*sin(2*rand()*1.5))/g;  % Jumping (Land)  
              elseif   r>0.30 && r<=0.9      
                  CapPos(i,:) =    CapPos(i,:) +  v(i,:); % Movement on the ground    
              elseif  r>0.9 && r<=0.95 
                 CapPos(i,:) =      gFoodPos   +  bf*sin(rand()*1.5);   % Swing % Local search  
              elseif   r>0.95 
                CapPos(i,:) =       gFoodPos   +  bf*(v(i,:)- v0(i,:));    % Climbing   % Local search
              end
          else
               CapPos(i,:) =           tau*(LB  + rand *(UB- LB));   
      end
    
% Let the followers follow the leaders (update their Pos)
elseif i>=noP/2 && i<=noP 
            
           eps=((rand()+2*rand())-(3*rand()))/(1+rand()); 
     
           Pos(i,:)=gFoodPos+2*(CapBestPos(fol(i),:)-CapPos(i,:))*eps +...
                                 2*(CapPos(i,:)-CapBestPos(i,:))*eps;      
 
          CapPos(i,:)=(Pos(i,:)+ CapPos(i-1,:))/(2); 
    
   end
end 
v0 = v;   
 

for i=1:noP % relocation (Update, exploration)
        u=UB-CapPos(i,:)<0;
        l=LB-CapPos(i,:)>0;
     
         CapPos(i,:)= LB.*l+UB.*u+CapPos(i,:).*~xor(u,l);
    
         CapFit(i,1)=fobj (CapPos(i,:)) ;
         
            if CapFit(i,1)<Fit(i)
                CapBestPos(i,:)=CapPos(i,:);
                Fit(i)=CapFit(i,1);
                
            end 
end
%% Evaluate the new Pos

[fmin,index]=min(Fit); % finding out the best Pos  

% Updating gPos and best Fit
if fmin < fitCapSA
    gFoodPos = CapBestPos(index,:); % Update the global best Pos
    fitCapSA = fmin;
end

% %     % Display the iterative results
% 
%          disp(['Iteration# ', num2str(t) , '  Fit= ' , num2str(fitCapSA)]);
% %    

   % Obtain the convergence curve
     cg_curve(t)=fitCapSA;
     
%  if t>2
%      set(0, 'CurrentFigure', f1)
% 
%         line([t-1 t], [cg_curve(t-1) cg_curve(t)],'Color','b'); 
%         xlabel('Iteration');
%         ylabel('Best score obtained so far');
%         drawnow 
%  end
%   
   
end
fitCapSA =fobj(gFoodPos);
end