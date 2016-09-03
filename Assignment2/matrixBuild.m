function  [oldX oldY] = matrixBuild(im)
  [nr nc] = size(im) 
  [x y ] = meshgrid(1:nr,1:nc)
  sX = 10.*sin(2*pi*x/120)
  sY = 15.*sin(2*pi*y/150)
  
  oldX = y + sX
  oldY = x + sY
end


