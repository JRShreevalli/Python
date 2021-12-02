import math
def AreaOfCircle(r):
    return (math.pi)*(pow(r,2))

x = int(input("Enter radius : "))
res = AreaOfCircle(x)
print( "Area of Circle = %.3f" %res )

# pi can also be imported with numpy module as :
# import numpy
# can be accessed as:
# numpy.pi