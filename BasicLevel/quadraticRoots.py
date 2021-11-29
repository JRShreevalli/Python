import cmath
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
d = (b*b) - (4*a*c)
root1 = ( -b + cmath.sqrt(d)) / 2*a 
root2 = (  b - cmath.sqrt(d)) / 2*a 
print('The Solutions are :  {0} , {1}  '.format(root1 , root2))
