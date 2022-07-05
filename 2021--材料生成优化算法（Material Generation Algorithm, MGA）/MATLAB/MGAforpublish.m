%% Material Generation Algorithm (MGA)  For Unconstrained Benchmark Problems
% Developer and programmer: Siamak Talatahyari, Mahdi Azizi, Amir H. Gandome
% Contact Info:
%       E-Mail:  Siamak.Talat@gmail.com, mehdi.azizi875@gmail.com, Gandomi@uts.edu.au
% Main paper:
% Material Generation Algorithm: A Novel Metaheuristic Algorithm
% for Optimization of Engineering Problems
% Journal: Processes, 2021
%%
clc;clear all;                                                              
%% Get Required Problem Information
ObjFuncName = @(x) Sphere(x); % @CostFunction ;
Var_Number = 10 ; % Number of variables ;
VarMin = -10 *ones(1,Var_Number) ;  % Lower bound of variable ;
VarMax = 10 *ones(1,Var_Number) ;  % Upper bound of variable ;

%% Get Required Algorithm Parameters
MaxIteration = 20 ; % Maximum number of Iterations ;
NCompan = 10 ; % Maximum number of initial Companent ;

Globalbest=0;
%% Create Initial Companant
Compan.Position=unifrnd(repmat(VarMin,NCompan,1),repmat(VarMax,NCompan,1));

% Evaluate Initial CompnMats
for ind=1:NCompan
    Compan.Fun_Eval(ind)=feval(ObjFuncName,Compan.Position(ind,:));
end

% Find  So Far Best
[value, Index1]=min(Compan.Fun_Eval);
BestSoFar.Fun_Eval(1) =value;
BestSoFar.Position (1,:)= Compan.Position(Index1,:);

%% Main Loop of MSS
for Iter=2:MaxIteration
    %New Companent 1
    Index=NCompan.*(0:Var_Number-1)+randperm(NCompan,Var_Number);
    disp(Compan.Position(Index))
    CompnNew.Position(1,:)= Compan.Position(Index)+unifrnd(-1,1).*randn(1,Var_Number);
    %New Companent 2
    Index=randperm(NCompan,1);
    Index2= randperm(NCompan,Index);
    CMs=randn(Index,1);
    CMs=CMs/sum(CMs);
    disp(size(CMs))
    disp(size(Compan.Position(Index2,:)))
    CompnNew.Position(2,:)=sum(CMs.*Compan.Position(Index2,:));
    
    % Apply Lower and Upper Bound Limits
    CompnNew.Position = max(CompnNew.Position,VarMin);
    CompnNew.Position = min(CompnNew.Position,VarMax);
    
    % Evaluation
    for ind3=1:size(CompnNew.Position,1)
        CompnNew.Fun_Eval(ind3)=feval(ObjFuncName,CompnNew.Position(ind3,:));
    end
    
    % Update Companent
    AllCompn.Position=[Compan.Position;CompnNew.Position];
    AllCompn.Fun_Eval=[Compan.Fun_Eval,CompnNew.Fun_Eval];
    [~, Index1]=sort(AllCompn.Fun_Eval);
    Compan.Position=AllCompn.Position(Index1(1:NCompan),:);
    Compan.Fun_Eval=AllCompn.Fun_Eval(Index1(1:NCompan));
    % Update So Far Best
    To_UpdateG= Compan.Fun_Eval(1) < BestSoFar.Fun_Eval(Iter-1);
    best = (1-To_UpdateG).*BestSoFar.Position(Iter-1,:)+To_UpdateG.*Compan.Position(1,:);
    BestSoFar.Fun_Eval (Iter)= (1-To_UpdateG).*BestSoFar.Fun_Eval(Iter-1)+To_UpdateG.*Compan.Fun_Eval(1);
    BestSoFar.Position(Iter,:)=best;
    % Show Iteration Information
    Showindex=1;
    if   Showindex
        disp(['Iteration ' num2str(Iter) ': Best Cost = ' num2str(BestSoFar.Fun_Eval (Iter))]);
    end
    
    % Checking The Termination Criteria
    if BestSoFar.Fun_Eval (Iter)<Globalbest 
        break
    end
    
end
Eval_Number=NCompan+2*Iter;
Conv_History=BestSoFar.Fun_Eval;

%% Plot Results
FinalConHis=1;
if FinalConHis
    figure;
    % plot(Conv_History,'LineWidth',2);
    semilogy(Conv_History,'LineWidth',2);
    xlabel('Iteration');
    ylabel('Best Cost');
    grid on;
end

%% Objective Function
function z=Sphere(x)
    z=sum(x.^2);
end
