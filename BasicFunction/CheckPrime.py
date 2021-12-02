def isPrime(n):
    temp = n 
    if temp > 0 :
        for i in range ( 2 , int(temp/2) + 1 ):
            # if any one number is divisible from 2 to n/2 then its not prime ...
            if temp % i == 0 :
                print("{0} is Not Prime".format(n))
                break
        else :
            print("{0} is Prime ".format(n) )     
    else :
        print (" {0} is not a prime".format(n))

n = int(input())
isPrime(n)