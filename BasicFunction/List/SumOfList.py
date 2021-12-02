def Sum_Of_Ele( l ):
    sum = 0
    for ele in range (0,len(l)):
        sum = sum + l[ele] 
    print(sum)

list = []
n = int(input())

for _ in range(0,n):
    ele = int(input())
    list.append(ele)

Sum_Of_Ele(list)
