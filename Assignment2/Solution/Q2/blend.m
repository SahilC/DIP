function [x bl] = blend(im1,im2,mask,n)
  g1 = getGaussian(im1)
  g2 = getGaussian(im2)
  g3 = getGaussian(uint8(mask))
  x = g1{3}
  m = g3{3} > 0
  
  rgb1 = g1{3}(:,:,1);  
  rgb2 = g2{3}(:,:,1); 
  rgb2(m) = rgb1(m);
  x(:,:,1) = rgb2;
  
  rgb1 = g1{3}(:,:,2);  
  rgb2 = g2{3}(:,:,2); 
  rgb2(m) = rgb1(m);
  x(:,:,2) = rgb2;
  
  rgb1 = g1{3}(:,:,3);  
  rgb2 = g2{3}(:,:,3); 
  rgb2(m) = rgb1(m);
  x(:,:,3) = rgb2;
  
  bl = cell(0)
  
  l1 = getLaplacian(g1)
  l2 = getLaplacian(g2)
  for i = 1:2
    z = l1{i}
    m = g3{3-i} > 0
    z = l1{i}
    rgb1 = l1{i}(:,:,1);  
    rgb2 = l2{i}(:,:,1); 
    rgb2(m) = rgb1(m);
    z(:,:,1) = rgb2;
  
    rgb1 = l1{i}(:,:,2);  
    rgb2 = l2{i}(:,:,2); 
    rgb2(m) = rgb1(m);
    z(:,:,2) = rgb2;
  
    rgb1 = l1{i}(:,:,3);  
    rgb2 = l2{i}(:,:,3); 
    rgb2(m) = rgb1(m);
    z(:,:,3) = rgb2;
    
    bl{i} = z
    %figure; imshow(bl{i})
  end
end