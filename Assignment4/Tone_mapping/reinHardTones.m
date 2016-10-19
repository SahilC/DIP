function reinHardTones(im)
shape = size(im);
N = shape(1)*shape(2)
R = im(:,:,1);
G = im(:,:,2);
B = im(:,:,3);

R = (R.*(1+R/4)./(1+R)).^(1/2.2)
G = (G.*(1+G/4)./(1+G)).^(1/2.2)
B = (B.*(1+B/4)./(1+B)).^(1/2.2)


imresult(:,:,1) = uint8(255*R);
imresult(:,:,2) = uint8(255*G);
imresult(:,:,3) = uint8(255*B);

#imresult

figure;imshow(imresult)







