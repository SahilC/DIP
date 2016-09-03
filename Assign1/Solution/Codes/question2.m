im = imread('green_screen.jpg');
norm = double(im)/255;
greens = norm(:,:,2).*(norm(:,:,2)-norm(:,:,1)).*(norm(:,:,2)-norm(:,:,3));
mask = (1 - greens) > 0.99;
back = imread('result_image.jpg');
z = im;
for j = 1:3
    rgb1 = im(:,:,j);  
    rgb2 = back(:,:,j); 
    rgb2(mask) = rgb1(mask);
    z(:,:,j) = rgb2;
end


imwrite(z,'result_image.png','png')