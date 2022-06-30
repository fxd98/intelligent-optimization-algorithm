% Developed in MATLAB R2017b
% Source codes demo version 1.0
% _____________________________________________________

%  Author, inventor and programmer: Iraj Naruei and Farshid Keynia,
%  e-Mail: irajnaruei@iauk.ac.ir , irajnaruei@yahoo.com
% _____________________________________________________
%  Co-author and Advisor: Farshid Keynia
%
%         e-Mail: fkeynia@gmail.com
% _____________________________________________________
%  Co-authors: Amir Sabbagh Molahoseyni
%        
%         e-Mail: sabbagh@iauk.ac.ir
% _____________________________________________________

% You can find the HPO article at 
% Hunter朴rey optimization: algorithm and applications
% https://doi.org/10.1007/s00500-021-06401-0
% _____________________________________________________
%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clc;
clear;
close all;
tic
function_name='F1';
[dim,CostFunction,ub, lb]  = Select_Functions(function_name);
%% HPO Parameters
  MaxIt = 500;     % Maximum Nomber of Iterations
  nPop = 30;         % Population Size
  Convergence_curve = zeros(1,MaxIt);

% Constriction Coefeicient
B = 0.1;

%% Initialization
 HPpos=rand(nPop,dim).*(ub-lb)+lb;
% for i=1:nPop
%     HPposFitness(i)=inf;
% end
    % Evaluate
for i=1:size(HPpos,1)
HPposFitness(i)=CostFunction(HPpos(i,:));       
end
% NFE = nPop;
 [~,indx] = min(HPposFitness);
% 
 Target = HPpos(indx,:);   % Target HPO
 TargetScore =HPposFitness(indx);
 Convergence_curve(1)=TargetScore;

%nfe = zeros(1,MaxIt);

%% HPO Main Loop
for it = 2:MaxIt

   c = 1 - it*((0.98)/MaxIt);   % Update C Parameter
    kbest=round(nPop*c);        % Update kbest
     for i = 1:nPop
            r1=rand(1,dim)<c;
            r2=rand;
            r3=rand(1,dim);
            idx=(r1==0);
            z=r2.*idx+r3.*~idx;
%             r11=rand(1,dim)<c;
%             r22=rand;
%             r33=rand(1,dim);
%             idx=(r11==0);
%             z2=r22.*idx+r33.*~idx;
        if rand<B
        xi=mean(HPpos);
        dist = pdist2(xi,HPpos);
        [~,idxsortdist]=sort(dist);
        SI=HPpos(idxsortdist(kbest),:);
        HPpos(i,:) =HPpos(i,:)+0.5*((2*(c)*z.*SI-HPpos(i,:))+(2*(1-c)*z.*xi-HPpos(i,:)));
        else
          for j=1:dim
            rr=-1+2*z(j);
          HPpos(i,j)= 2*z(j)*cos(2*pi*rr)*(Target(j)-HPpos(i,j))+Target(j);

          end
        end  
        HPpos(i,:) = min(max(HPpos(i,:),lb),ub);
        % Evaluation
        HPposFitness(i) = CostFunction(HPpos(i,:));
        % Update Target
        if HPposFitness(i)<TargetScore 
            Target = HPpos(i,:);
            TargetScore = HPposFitness(i);
        end
     end
  
    
  Convergence_curve(it)=TargetScore;
   disp(['Iteration: ',num2str(it),' Best Cost = ',num2str(TargetScore)]);
 end

toc

