im = imread('source.jpg.jpg')
im2 = imread('target.jpg.jpg')
im3 = imread('mask.png')

n = 2

g = getGaussian(im,n)
l = getLaplacian(g,n)


[x bl] = blend(im,im2,im3,n)
reconstruct(bl,x,n)