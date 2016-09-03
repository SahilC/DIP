function reconstruct(l,g,n)
  Y = g
  for i=1:2
    [nr nc c] = size(l{i})
    temp = imresize(Y,[nr nc])
    Y = temp + l{i}
%    figure; imshow(Y,[])
    %imwrite(Y,'out.png')
    file = sprintf('r%d.png', i)
    imwrite(Y,file)
  end
end