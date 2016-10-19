function [A] = reinHardTonesLocal(im,key,phi)
  alpha = 1/(2*sqrt(2))
  v1 = zeros(size(im,1), size(im,2), 8);
  v = zeros(size(im,1), size(im,2), 8);
  for scale = 1:(8+1)
    s = 1.6^scale;
    s_alpha = alpha*s;
    radius = ceil(2*s_alpha);
    si = 2*ceil(2*s_alpha) + 1;
    gauss_horizontal = fspecial('gaussian', [si 1], s_alpha);
    v1(:,:,scale) = conv2(im(:,:,1), gauss_horizontal, 'same');
    gauss_vertical = fspecial('gaussian', [1 si], s_alpha);
    v1(:,:,scale) = conv2(v1(:,:,scale), gauss_vertical, 'same');
  endfor
  
  for scale = 1:8
    v(:,:,scale) = abs(v1(:,:,scale) - v1(:,:,scale+1)) ./ (((2^phi)*key)/scale^2 + v1(:,:,scale));
  endfor
  
  scales = 8*ones(size(v,1),size(v,2));
  
  for i = 1:size(v,1)
    for j = 1:size(v,2)
      for k = 1:size(v,3)
        if v(i,j,k) > 0.05
          if (scale == 1) 
            scales(i,j) = 1;
          end
                    
          if (scale > 1)
            scales(i,j) = scale-1;
          end

          break;
        end        
      endfor
    endfor
  endfor


  #scales(sm == 0) = 8;
  lum_final = zeros(size(v,1), size(v,2))
  for i=1:size(v1,1)
        for j=1:size(v1,2)
            lum_final(i,j) = v1(i,j,scales(i,j));
        end
  end
  
  A = im./(1+lum_final);
  #imshow(A);