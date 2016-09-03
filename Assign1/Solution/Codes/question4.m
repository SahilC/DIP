im = imread('lotus.jpg')
a = colfilt(im,[10 10],'sliding',@mode)
imwrite(a,'lotus.png','png')