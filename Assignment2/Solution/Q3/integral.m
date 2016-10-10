im = imread('boy_smiling.jpg')

integral_image = im
x = im

k = [[ 1 -1 0];[ -1 1 0];[0 0 0]]

integralR = cumsum(cumsum(im(:,:,1)')')
integralG = cumsum(cumsum(im(:,:,2)')')
integralB = cumsum(cumsum(im(:,:,3)')')
%integralR = calculateSum(im(:,:,1)')
%integralG = calculateSum(im(:,:,2)')
%integralB = calculateSum(im(:,:,3)')

[nc nr] = size(integralR)
maxR = integralR(nc,nr)
maxB = integralB(nc,nr)
maxG = integralG(nc,nr)

dr = linspace(min(integralR(:)),max(integralR(:)),256)
temp(:,:,1) = uint8(arrayfun(@(x) find(abs(dr(:)-x)==min(abs(dr(:)-x))),integralR))

dg = linspace(min(integralG(:)),max(integralG(:)),256)
temp(:,:,2) = uint8(arrayfun(@(x) find(abs(dg(:)-x)==min(abs(dg(:)-x))),integralG))

db = linspace(min(integralB(:)),max(integralB(:)),256)
temp(:,:,3) = uint8(arrayfun(@(x) find(abs(db(:)-x)==min(abs(db(:)-x))),integralB))

%temp(:,:,1) = uint8((integralR.*255)./maxR)
%temp(:,:,2) = uint8((integralG.*255)./maxG)
%temp(:,:,3) = uint8((integralB.*255)./maxB)

imwrite(temp,'gradient.png')

other(:,:,1) = (double(temp(:,:,1)).*maxR)./255
other(:,:,2) = (double(temp(:,:,2)).*maxG)./255
other(:,:,3) = (double(temp(:,:,3)).*maxB)./255


x(:,:,1) = imfilter(other(:,:,1),k)
x(:,:,2) = imfilter(other(:,:,2),k)
x(:,:,3) = imfilter(other(:,:,3),k)

imwrite(x,'uint8.png')

y = im 
y(:,:,1) = imfilter(integralR,k)
y(:,:,2) = imfilter(integralG,k)
y(:,:,3) = imfilter(integralB,k)

%imwrite(y,'double.png')

figure; imshow(x,[]);

%imwrite(x,'inverseBLF.png')
