def program(n):
    add = 0
    for i in range ( 1 , n+1 ) :
        add =  add + (i*i)
    print(add)
     
n = int(input())
program(n)