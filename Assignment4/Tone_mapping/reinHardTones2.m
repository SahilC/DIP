function reinHardTones2(im)
shape = size(im);
N = shape(1)*shape(2)
R = 16*im(:,:,1);
G = 16*im(:,:,2);
B = 16*im(:,:,3);

Lr = exp(sum(log(R(:) + 0.01))/N)
Lg = exp(sum(log(G(:)+ 0.01))/N)
Lb = exp(sum(log(B(:)+0.01))/N)

lr = 0.18*4**((2*log2(Lr) - log2(0.001+min(R(:))) - log2(max(R(:))))/(log2(max(R(:))) - log2(0.001+min(R(:)))))
lg = 0.18*4**((2*log2(Lg) - log2(0.001+min(G(:))) - log2(max(G(:))))/(log2(max(G(:))) - log2(0.001+min(G(:)))))
lb = 0.18*4**((2*log2(Lb) - log2(0.001+min(B(:))) - log2(max(B(:))))/(log2(max(B(:))) - log2(0.001+min(B(:)))))

(2*log2(Lr) - log2(min(R(:))) - log2(max(R(:))))/(log2(max(R(:))) - log2(min(R(:))))

R = ((lr/Lr).*R)
G = ((lg/Lg).*G)
B = ((lb/Lb).*B)

R = (R./(1+R)).^(1/2.2)
G = (G./(1+G)).^(1/2.2)
B = (B./(1+B)).^(1/2.2)

imresult(:,:,1) = uint8(255*R);
imresult(:,:,2) = uint8(255*G);
imresult(:,:,3) = uint8(255*B);

#imresult

figure;imshow(imresult)







