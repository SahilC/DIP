%translate
g = @ (x) [x(:,1)-0.1, x(:,2)-0.1]
tform = maketform('custom', 2, 2, [], g, []);
twirl = imtransform(im, tform, 'UData', [-1 1], 'VData', [-1 1],'XData', [-1 1], 'YData', [-1 1]);
%figure; imshow(twirl)
imwrite(twirl,'translate.png')
%rotate

g = @ (x) [x(:,1)*cosd(30) + x(:,2)*sind(30), x(:,2)*cosd(30) - x(:,1)*sind(30)]
tform = maketform('custom', 2, 2, [], g, []);
twirl = imtransform(im, tform, 'UData', [-1 1], 'VData', [-1 1],'XData', [-1 1], 'YData', [-1 1]);
%figure; imshow(twirl)
imwrite(twirl,'rotate.png')


%shear 
g = @ (x) [x(:,1) + 0.5*x(:,2), x(:,2)]
tform = maketform('custom', 2, 2, [], g, []);
twirl = imtransform(im, tform, 'UData', [-1 1], 'VData', [-1 1],'XData', [-1 1], 'YData', [-1 1]);
%figure; imshow(twirl)
imwrite(twirl,'shear.png')

%twirl 
r = @(x) sqrt(x(:,1).^2 + x(:,2).^2)
w = @(x) atan2(x(:,2), x(:,1)) + 7.*((10-r(x))/10)
f = @(x) [r(x) .* cos(w(x)), r(x) .* sin(w(x))];
g = @(x, unused) f(x);


tform = maketform('custom', 2, 2, [], f, []);
twirl = imtransform(im, tform, 'UData', [-1 1], 'VData', [-1 1],'XData', [-1 1], 'YData', [-1 1]);
figure; imshow(twirl)

imwrite(twirl,'twirl.png')