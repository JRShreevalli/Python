a = float(input())
b = float(input())
c = float(input())

s = ( a + b + c ) / 2 
area = (s * ( s - a ) * ( s - b ) * ( s - c ) ) ** 0.5 

print( 'Area of triangle = %0.1f \n  ' %area ) 


# ' ' and " " both are valid in python
#  % is used as just take up that particular value 
# \n is used to represent nxtline in python
