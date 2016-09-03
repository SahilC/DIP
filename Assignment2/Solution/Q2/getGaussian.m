function g = getGaussian(im,N)
  X = im
  g = cell(0)
  for i=1:3 
    X = imsmooth(X,'Average',[5,5])
    %X = downsample(downsample(X',2)',2)
    X = imresize(X,0.5)
    %X = getNextGaussianLevel(X)
    %figure; imshow(X)
%    file = sprintf('g%d.png', i)
%    imwrite(X,file)
    g{i} = X
  end
end