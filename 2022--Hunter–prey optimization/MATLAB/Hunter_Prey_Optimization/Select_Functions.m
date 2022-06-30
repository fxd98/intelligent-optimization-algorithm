
function [dimensions,fitness,upper_bound, lower_bound] = Select_Functions(func)
d=30;

switch func

    case 'F1'
        fitness = @F1;
        lower_bound=-100;
        upper_bound=100;
        dimensions=d;
        
    case 'F2'
        fitness = @F2;
        lower_bound=-10;
        upper_bound=10;
        dimensions=d;
        
    case 'F3'
        fitness = @F3;
        lower_bound=-100;
        upper_bound=100;
        dimensions=d;
        
    case 'F4'
        fitness = @F4;
        lower_bound=-100;
        upper_bound=100;
        dimensions=d;
        
    case 'F5'
        fitness = @F5;
        lower_bound=-30;
        upper_bound=30;
        dimensions=d;
        
    case 'F6'
        fitness = @F6;
        lower_bound=-100;
        upper_bound=100;
        dimensions=d;
        
    case 'F7'
        fitness = @F7;
        lower_bound=-1.28;
        upper_bound=1.28;
        dimensions=d;
        
    case 'F8'
        fitness = @F8;
        lower_bound=-500;
        upper_bound=500;
        dimensions=d;
        
    case 'F9'
        fitness = @F9;
        lower_bound=-5.12;
        upper_bound=5.12;
        dimensions=d;
        
    case 'F10'
        fitness = @F10;
        lower_bound=-32;
        upper_bound=32;
        dimensions=d;
        
    case 'F11'
        fitness = @F11;
        lower_bound=-600;
        upper_bound=600;
        dimensions=d;
        
    case 'F12'
        fitness = @F12;
        lower_bound=-50;
        upper_bound=50;
        dimensions=d;
        
    case 'F13'
        fitness = @F13;
        lower_bound=-50;
        upper_bound=50;
        dimensions=d;

end

end

% F1

function o = F1(x)
global NFE
NFE=NFE+1;
o=sum(x.^2);
end

% F2

function o = F2(x)
global NFE
NFE=NFE+1;
o=sum(abs(x))+prod(abs(x));
end

% F3

function o = F3(x)
global NFE
NFE=NFE+1;
dim=size(x,2);
o=0; 
for i=1:dim
    o=o+sum(x(1:i))^2;
end
end

% F4

function o = F4(x)
global NFE
NFE=NFE+1;
o=max(abs(x));
end

% F5

function o = F5(x)
global NFE
NFE=NFE+1;
dim=size(x,2);
o=sum(100*(x(2:dim)-(x(1:dim-1).^2)).^2+(x(1:dim-1)-1).^2);
end

% F6

function o = F6(x)
global NFE
NFE=NFE+1;
o=sum(abs((x+.5)).^2);
end

% F7

function o = F7(x)
global NFE
NFE=NFE+1;
dim=size(x,2);
o=sum([1:dim].*(x.^4))+rand;
end

% F8

function o = F8(x)
global NFE
NFE=NFE+1;
o=sum(-x.*sin(sqrt(abs(x))));
end

% F9

function o = F9(x)
global NFE
NFE=NFE+1;
dim=size(x,2);
o=sum(x.^2-10*cos(2*pi.*x))+10*dim;
end

% F10

function o = F10(x)
global NFE
NFE=NFE+1;
dim=size(x,2);
o=-20*exp(-.2*sqrt(sum(x.^2)/dim))-exp(sum(cos(2*pi.*x))/dim)+20+exp(1);

end

% F11

function o = F11(x)
global NFE
NFE=NFE+1;
dim=size(x,2);
o=sum(x.^2)/4000-prod(cos(x./sqrt([1:dim])))+1;
end

% F12

function o = F12(x)
global NFE
NFE=NFE+1;
dim=size(x,2);
o=(pi/dim)*(10*((sin(pi*(1+(x(1)+1)/4)))^2)+sum((((x(1:dim-1)+1)./4).^2).*...
(1+10.*((sin(pi.*(1+(x(2:dim)+1)./4)))).^2))+((x(dim)+1)/4)^2)+sum(Ufun(x,10,100,4));
end

% F13

function o = F13(x)
global NFE
NFE=NFE+1;
dim=size(x,2);
o=.1*((sin(3*pi*x(1)))^2+sum((x(1:dim-1)-1).^2.*(1+(sin(3.*pi.*x(2:dim))).^2))+...
((x(dim)-1)^2)*(1+(sin(2*pi*x(dim)))^2))+sum(Ufun(x,5,100,4));
end


function o=Ufun(x,a,k,m)
o=k.*((x-a).^m).*(x>a)+k.*((-x-a).^m).*(x<(-a));
end
