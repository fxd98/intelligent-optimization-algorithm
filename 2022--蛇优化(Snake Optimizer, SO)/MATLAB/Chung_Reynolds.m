%___________________________________________________________________%
%  Snake Optimizer (SO) source codes version 1.0                    %
%                                                                   %
%  Developed in MATLAB R2021b                                       %
%                                                                   %
%  Author and programmer:  Fatma Hashim & Abdelazim G. Hussien      %
%                                                                   %
%         e-Mail: fatma_hashim@h-eng.helwan.edu.eg                  %
%                 abdelazim.hussien@liu.se                          %
%                 aga08@fayoum.edu.eg                               %
%                                                                   %
%                                                                   %
%   Main paper: Fatma Hashim & Abdelazim G. Hussien                 %
%               Knowledge-based Systems                             %
%               in press,                                           %
%               DOI: 10.1016/j.knosys.2022.108320                   %
%                                                                   %
%___________________________________________________________________%
function objval = Chung_Reynolds(x)%[-5.12,5.12]
 n = size(x,2); 
f = 0;
for i = 1:n;
    f = f+(x(i).^2).^2;
end
objval = f;
