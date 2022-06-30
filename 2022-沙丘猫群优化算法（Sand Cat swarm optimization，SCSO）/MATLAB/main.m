%___________________________________________________________________%
%   SAND CAT OPTIMIZATION ALGORITHM source codes                    %
%   Author and programmer: AMIR SEYYEDABBASI                        %
%   e-Mail: amir.seyedabbasi@gmail.com                              %                                                                 %
%   Main paper: A. Seyyedabbasi, F. kiani                           %
%   DOI: https://doi.org/10.1007/s00366-022-01604-x                 %
%___________________________________________________________________%

clc
clear all

SearchAgents_no=30;
Max_iteration=500;
 
Function_name=1;
[lb,ub,dim,fobj]=Get_Functions_details(Function_name);
[BsSCSO,BpSCSO,SCSO_cg_curve]=SCSO(SearchAgents_no,Max_iteration,lb,ub,dim,fobj);
 
