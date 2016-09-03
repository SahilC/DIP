function l = getLaplacian(g,n)
  Y = g{3}
  l = cell(0)
  for i=1:2
    %temp = Expand(Y)
    [nr nc c] = size(g{3-i})
    temp = imresize(Y,[nr nc])
    %X = upsample(upsample(X',2)',2)
    l{i} = double(g{3-i}) - double(temp)
    %figure; imshow(l{i},[])
%    file = sprintf('l%d.png', i)
%    imwrite(l{i},file)
    Y = g{3-i}
  end  
end