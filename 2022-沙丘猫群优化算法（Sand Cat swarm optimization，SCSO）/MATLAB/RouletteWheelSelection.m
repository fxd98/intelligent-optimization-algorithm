function j=RouletteWheelSelection(P) 
    r=rand; 
    s=sum(P);
    P=P./s;
    C=cumsum(P); 
    j=find(r<=C,1,'first'); %find(X,n,direction)（其中 direction 为 'last'）查找与 X 中的非零元素对应的最后 n 个索引。direction 的默认值为 'first'，即查找与非零元素对应的前 n 个索引。
end