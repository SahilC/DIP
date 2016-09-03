function  numsum = inverseBilateralSum(x) 
  sigmad = 2^2
  sigmar = 100^2
  %w1 = exp(-1/(2*sigmad) - (x(2,2)-x(1,2))^2/(2*sigmar))
  %w2 = exp(-1/(2*sigmad) - (x(2,2)-x(2,3))^2/(2*sigmar))
  %w3 = exp(-1/(2*sigmad) - (x(2,2)-x(3,2))^2/(2*sigmar))
  %w4 = exp(-1/(2*sigmad) - (x(2,2)-x(2,1))^2/(2*sigmar))
  [X Y] = meshgrid(1:5)
  X = double(X)
  Y = double(Y)
  x = double(x)
  term1 = double(((X-3).^2+(Y-3).^2)./(2*sigmad))
  term2 = double(((x .- x(3,3)).^2)./(2*sigmar))
  t = double(exp(term1.+term2))
  w = double(t)
  numsum = sum(x.*w)/sum(w)
end