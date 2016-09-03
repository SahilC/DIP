function f = translate(a,b)
  f = @ (x) [x(:,1)-a, x(:,2)-b]
end