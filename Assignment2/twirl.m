%im = imread('face.png')
%im = double(im)

%[nr nc] = size(im)
%x = linspace(-0.5,0.5,nc)';
%y = flipud(linspace(-0.5,0.5,nr)');


%[X Y] = meshgrid(x,y)
%R = (X.^2 + Y.^2).^0.5
%P = X + Y.*cos(R) 
%Q = Y + X.*sin(R)

%g = interp2(X,Y,im,P,Q,'cubic',0);
%imagesc(x,y,g);colormap gray
%axis square ; axis xy

function g = twirl()
  r = @(x) sqrt(x(:,1).^2 + x(:,2).^2)
  w = @(x) atan2(x(:,2), x(:,1)) + 7.*((10-r(x))/10)
  f = @(x) [r(x) .* cos(w(x)), r(x) .* sin(w(x))];
  g = @(x, unused) f(x);
end

