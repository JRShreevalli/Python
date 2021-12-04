def alphabet (n):
    # value of 'A' is 65 ..................
    val = 65
    for i in range(n):
        for j in range(i+1):
            
            char = chr(val)
            print(char,end=" ")
            val = val + 1 
            
        print("\r")
    
t = int(input())
alphabet(t)