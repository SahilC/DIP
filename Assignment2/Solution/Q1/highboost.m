pkg load image
im = imread('bell.jpg')
smooth = imsmooth(im,'Average',[10,10])
imwrite(smooth,'gauss.png')
diff = im - smooth

imwrite(diff,'diff.png')
eq(:,:,1) = histeq(diff(:,:,1))
eq(:,:,2) = histeq(diff(:,:,2))
eq(:,:,3) = histeq(diff(:,:,3))

imwrite(eq,'eq.png')
%for i = 1:10
%  k = i*10
%  smooth = im + k*eq
%  outputString = sprintf('smooth%d.png', k)
%  imwrite(smooth,outputString)
%end