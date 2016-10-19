pkg load image;
c = [{'AtriumNight.pfm'},{'church.pfm'},{'doll_doll.pfm'},{'lips.pfm'},{'rosette.pfm'}]
for i = 1:length(c)
  im = getpfmraw(c{i});
  key = 0.1
  phi = 8
  
  R = reinHardTonesLocal(im(:,:,1),key, phi)
  G = reinHardTonesLocal(im(:,:,2),key, phi)
  B = reinHardTonesLocal(im(:,:,3),key,phi)
  
  final_image = zeros(size(im))
  final_image(:,:,1) = R
  final_image(:,:,2) = G
  final_image(:,:,3) = B
  imshow(final_image)
  imwrite(final_image,c{i},'png')
endfor