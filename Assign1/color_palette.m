n = 3;                %// number of colors

t = linspace(0,4*pi,50);

B = sin(t)*0.5 + 0.5;  %// Blue from 0 to 1 as sine
R = cos(t)*0.5 + 0.5;  %// Red from 0 to 1 as cosine
G = (sin(t))*0.5 + 0.5;   %// Green all zero

colormap( [R(:), G(:), B(:)] );  %// create colormap

%// some example figure
figure(1)
surf(peaks)
colorbar