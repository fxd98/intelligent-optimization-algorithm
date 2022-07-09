%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  Honey Badger Algorithm source code 
%  paper:
%     Hashim, Fatma A., Essam H. Houssein, Kashif Hussain, Mai S. %     Mabrouk, Walid Al-Atabany. 
%     "Honey Badger Algorithm: New Metaheuristic Algorithm for %  %     Solving Optimization Problems." 
%     Mathematics and Computers in Simulation, 2021.
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
function [Xprey, Food_Score,CNVG] = HBA(objfunc, dim,lb,ub,tmax,N)
beta       = 6;     % the ability of HB to get the food  Eq.(4)
C       = 2;     %constant in Eq. (3)
vec_flag=[1,-1];
%initialization
X=initialization(N,dim,ub,lb);
%Evaluation
fitness = fun_calcobjfunc(objfunc, X);
[GYbest, gbest] = min(fitness);
Xprey = X(gbest,:);
for t = 1:tmax
    alpha=C*exp(-t/tmax);   %density factor in Eq. (3)
    I=Intensity(N,Xprey,X); %intensity in Eq. (2)
    for i=1:N
        r =rand();
        F=vec_flag(floor(2*rand()+1));
        for j=1:1:dim
            di=((Xprey(j)-X(i,j)));
            if r<.5
                r3=rand;                r4=rand;                r5=rand;
                
                Xnew(i,j)=Xprey(j) +F*beta*I(i)* Xprey(j)+F*r3*alpha*(di)*abs(cos(2*pi*r4)*(1-cos(2*pi*r5)));
            else
                r7=rand;
                Xnew(i,j)=Xprey(j)+F*r7*alpha*di;
            end
        end
        FU=Xnew(i,:)>ub;FL=Xnew(i,:)<lb;Xnew(i,:)=(Xnew(i,:).*(~(FU+FL)))+ub.*FU+lb.*FL;
        
        tempFitness = fun_calcobjfunc(objfunc, Xnew(i,:));
        if tempFitness<fitness(i)
            fitness(i)=tempFitness;
            X(i,:)= Xnew(i,:);
        end
    end
    FU=X>ub;FL=X<lb;X=(X.*(~(FU+FL)))+ub.*FU+lb.*FL;
    [Ybest,index] = min(fitness);
    CNVG(t)=min(Ybest);
    if Ybest<GYbest
        GYbest=Ybest;
        Xprey = X(index,:);
    end
end
Food_Score = GYbest;
end

function Y = fun_calcobjfunc(func, X)
N = size(X,1);
for i = 1:N
    Y(i) = func(X(i,:));
end
end
function I=Intensity(N,Xprey,X)
for i=1:N-1
    di(i) =( norm((X(i,:)-Xprey+eps))).^2;
    S(i)=( norm((X(i,:)-X(i+1,:)+eps))).^2;
end
di(N)=( norm((X(N,:)-Xprey+eps))).^2;
S(N)=( norm((X(N,:)-X(1,:)+eps))).^2;
for i=1:N
    r2=rand;
    I(i)=r2*S(i)/(4*pi*di(i));
end
end
function [X]=initialization(N,dim,up,down)
if size(up,2)==1
    X=rand(N,dim).*(up-down)+down;
end
if size(up,2)>1
    for i=1:dim
        high=up(i);low=down(i);
        X(:,i)=rand(N,1).*(high-low)+low;
    end
end
end
