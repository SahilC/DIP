%function cumulative = calculateSum(im)
%  [nr nc] = size(im)
%  cumulative = im
%  for i = 1:nr
%    for j = 1:nc
%        if i == 1 && j == 1
%          cumulative(i,j) = im(i,j)
%        elseif i == 1
%          cumulative(i,j) = im(i,j) + cumulative(i,j-1)
%        elseif j == 1
%          cumulative(i,j) = im(i,j) + cumulative(i-1,j)
%        else
%          cumulative(i,j) = im(i,j) + cumulative(i-1,j)+cumulative(i,j-1)-cumulative(i-1,j-1)
%        end      
%    end
%  end
%end

function cumulative = calculateSum(im)
  [nr nc] = size(im)
  cumulative = double(im)
  for i = 2:nc
    cumulative(:,i) = cumulative(:,i-1) + im(:,i)
%    for j = 2:nc
%      cumulative(i,j) = cumulative(i,j-1) + im(i,j) 
%    end
  end
  
  cumulative = cumulative'
  for i = 2:nr
    cumulative(:,i) = cumulative(:,i-1) + im(:,i)
%    for j = 2:nc
%      cumulative(i,j) = cumulative(i,j-1) + im(i,j) 
%    end
  end
end