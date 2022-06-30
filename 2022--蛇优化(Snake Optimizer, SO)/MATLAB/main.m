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
close all
clear all
clc
fitfun = @Chung_Reynolds;
dim=30;
Max_iteration=1000;
SearchAgents_no=30;
lb=-100;
ub=100;
tlt='Chung Reynolds';
i=1;
[Xfood, Xvalue,CNVG] = SO(SearchAgents_no,Max_iteration,fitfun, dim,lb,ub)
figure,
plot(CNVG,'Color', 'r')
xlim([1 1000]);
