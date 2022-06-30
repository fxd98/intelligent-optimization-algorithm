function [lb,ub,dim,fobj] = BenchmarkFunctions(F)

D=30;
switch F
    case 'F1'
        fobj = @F1;
        lb=-100;
        ub=100;
        dim=D;
        
    case 'F2'
        fobj = @F2;
        lb=-100;
        ub=100;
        dim=D;
        
    case 'F3'
        fobj = @F3;
        lb=-100;
        ub=100;
        dim=D;
        
    case 'F4'
        fobj = @F4;
        lb=-100;
        ub=100;
        dim=D;
        
    case 'F5'
        fobj = @F5;
        lb=-100;
        ub=100;
        dim=D;
        
    case 'F6'
        fobj = @F6;
        lb=-100;
        ub=100;
        dim=D;
        
    case 'F7'
        fobj = @F7;
        lb=-100;
        ub=+100;
        dim=D;
        
    case 'F8'
        fobj = @F8;
        lb=-100;
        ub=100;
        dim=D;
        
    case 'F9'
        fobj = @F9;
        lb=-100;
        ub=100;
        dim=D;
        
    case 'F10'
        fobj = @F10;
        lb=-32.768;
        ub=32.768;
        dim=D;
        
    case 'F11'
        fobj = @F11;
        lb=-100;
        ub=100;
        dim=D;
        
    case 'F12'
        fobj = @F12;
        lb=-100;
        ub=100;
        dim=D;
        
    case 'F13'
        fobj = @F13;
        lb=-100;
        ub=100;
        dim=D;
        
    case 'F14'
        fobj = @F14;
        lb=-10;
        ub=10;
        dim=D;
end
end


function z = F1(x)
% Bent Cigar (Unimodal)
D=size(x,2);
z=x(1)^2+10^6*sum(x(2:D).^2);
end

function z = F2(x)
% Power (Unimodal)
D=size(x,2);
for i=1:D
    
    f(i)=abs(x(i)).^(i+1);
    
end
z=sum(f);
end

function z = F3(x)
% Zakharov (Unimodal)
z=sum(x.^2)+(sum(0.5.*x))^2+(sum(0.5.*x))^4;
end

function z = F4(x)
%% Rosenbrock (Unimodal)
D=size(x,2);
for i=1:D-1
    
    ff(i)=100*(x(i).^2-x(i+1)).^2+(x(i)-1).^2;
    
end

z=sum(ff);
end

function z = F5(x)  %12
%% Discus (Unimodal)
D=size(x,2);
z=10^6*x(1)^2+sum(x(2:D).^2);
end

function z = F6(x) %13
%% High Conditioned Elliptic Function (Unimodal)
D=size(x,2);
for i=1:D
    
f(i)=(((10^6)^((i-1)/(D-1)))*x(i).^2);

end
z=sum(f);
end

%% MultiModal Functions

function z = F7(x)  %4
% Expanded Schaffer’s F6 (Multimodal)
D=size(x,2);
for i=1:D
    if i==D
        
        f(i)=0.5+(sin(sqrt(x(i)^2+x(1)^2))^2-0.5)/(1+0.001*(x(i)^2+x(1)^2))^2;
    else
        f(i)=0.5+(sin(sqrt(x(i)^2+x(i+1)^2))^2-0.5)/(1+0.001*(x(i)^2+x(i+1)^2))^2;

    end
end
z=sum(f);
end

function z = F8(x)  %5
% Levy Function (Multimodal)
D=size(x,2);
for i=1:D-1
    
    w(i)=1+(x(i)-1)/4;
    
    f(i)= (w(i)-1)^2*(1+10*sin(pi*w(i)+1)^2);

end
w(D)=1+(x(D)-1)/4;
z=sin(pi*w(1))^2+sum(f)+(w(D)-1)^2*(1+sin(2*pi*w(D))^2);
end

function z = F9(x) %6
% Modified Schwefel’s Function (Multimodal)
D=size(x,2);
for i=1:D
    y=x(i)+4.209687462275036e+002;
    if abs(y)<500
      f(i)= y*sin(abs(y)^0.5);
    elseif y>500
        
      f(i)=(500-mod(y,500))* sin(sqrt(abs(500-mod(y,500))))-(y-500)^2/(10000*D);
    elseif y<-500
      f(i)=(mod(abs(y),500)-500)* sin(sqrt(abs(mod(abs(y),500)-500)))-(y+500)^2/(10000*D);  
    end
end
z=418.9829*D-sum(f);
end

function z = F10(x)
%% Ackley (Multimodal)
D=size(x,2);
z=-20*exp(-0.2*((1/D)*(sum(x.^2))).^0.5)-exp(1/D*sum(cos(2*pi.*x)))+20+exp(1);
end



function z = F11(x)
%% weierstrass (Multimodal)
D=size(x,2);
x=x+0.5;
a = 0.5;
b = 3;
kmax = 20;
c1(1:kmax+1) = a.^(0:kmax);
c2(1:kmax+1) = 2*pi*b.^(0:kmax);
f=0;
c=-w(0.5,c1,c2);
for i=1:D
f=f+w(x(:,i)',c1,c2);
end
z=f+c*D;
function y = w(x,c1,c2)
y = zeros(length(x),1);
for k = 1:length(x)
	y(k) = sum(c1 .* cos(c2.*x(:,k)));
end

end
end

function z = F12(x)
%% HappyCat Function (Multimodal) 
D=size(x,2);
z=(abs(sum(x.^2)-D))^(1/4)+(0.5*sum(x.^2)+sum(x))/D+0.5;
end

function z = F13(x)
%% HGBat Function (Multimodal) 
D=size(x,2);
z=(abs((sum(x.^2))^2-(sum(x))^2))^(1/2)+(0.5*sum(x.^2)+sum(x))/D+0.5;
end

function z = F14(x)
%% Alpine (Multimodal)

z=sum(abs(x.*sin(x)+0.1.*x));
end










 















