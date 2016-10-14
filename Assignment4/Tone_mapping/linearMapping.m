function linearMapping(im)
Min = min(im(:))
Max = max(im(:))
temp = (im - Min)./(Max - Min)
temp = uint8(temp.*255)
imshow(temp)




