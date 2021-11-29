def CompoundIntrest( p , t , r ):
    a = p * (( 1 + r/100 ) ** t)
    compound = a - p 
    print(compound)

a = int(input())
b = int(input())
c = float(input())
CompoundIntrest( a , b , c )

#  2nd line can alternatively return as a = p * (pow(( 1 + r/100) , t))
# flat value nii return avatle y 