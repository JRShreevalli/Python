def order(x):
  
    count = 0
    while (x != 0):
        count = count + 1
        x = x // 10
          
    return count
  

def isArmstrong(x):
      
    n = order(x)
    temp = x
    sum1 = 0
      
    while (temp != 0):
        r = temp % 10
        sum1 = sum1 + pow(r, n)
        temp = temp // 10

    return (sum1 == x)
  

x = int(input())
print(isArmstrong(x))
  
