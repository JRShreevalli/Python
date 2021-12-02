def Max_Ele(l):
    max = l[0] 
    for i in range(1,len(l)):
        if l[i] > max :
            max = l[i]
    print(max)

n = int(input())
lst = [ ]
for _ in range(0,n):
    m = int(input())
    lst.append(m)
Max_Ele(lst)