def maximum( x , y , z ) :
    if x > y and x > z :
        return x 
    elif y > x and y > z :
        return y 
    else :
        return z 

x = int(input('Enter x = '))
y = int(input('Enter y = '))
z = int(input('Enter z = '))
print(maximum(x,y,z))

# in x place can't we write (()) -> yeah we can write but don't give in list format give 
# only in one input nextline input format
