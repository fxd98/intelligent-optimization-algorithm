function [random_vulture_X]=random_select(Best_vulture1_X,Best_vulture2_X,alpha,betha)

    probabilities=[alpha, betha ];
    disp('rouletteWheelSelection:')
    disp(rouletteWheelSelection( probabilities ))
    
    if (rouletteWheelSelection( probabilities ) == 1)
            random_vulture_X=Best_vulture1_X;
    else
            random_vulture_X=Best_vulture2_X;
    end

end