%part 1
%im = imread('face.png')
%filtered = nlfilter(im,[5 5],@bilateralSum)
%filtered = nlfilter(im,[5 5],@bilateralSum)
%imshow(filtered,[])
%imwrite(filtered,'out.png')


%part 2
im = imread('boy_smiling.jpg')
out = im
%filtered = nlfilter(im,[5 5],@bilateralSum)
out(:,:,1) = nlfilter(im(:,:,1),[5 5],@bilateralSum)
out(:,:,2) = nlfilter(im(:,:,2),[5 5],@bilateralSum)
out(:,:,3) = nlfilter(im(:,:,3),[5 5],@bilateralSum)
%out(:,:,1) = colfilt(im(:,:,3),[5 5],'sliding',@bilateralSum)
%out(:,:,2) = colfilt(im(:,:,3),[5 5],'sliding',@bilateralSum)
%out(:,:,3) = colfilt(im(:,:,3),[5 5],'sliding',@bilateralSum)
imwrite(out,'out.png')
imshow(out,[])