def Pattern2(n):
    for i in range (n):
        
        val = 1 
        
        for j in range (0 , i+1):
            print(val , end=" ")
            val = val+ 1
        print("\r")

val = int(input())
Pattern2(val)

