def Pal_Check(s):
    return(s[::-1] == s)


n = input()
if(Pal_Check(n) == True):
    print("Yes")
else:
    print("No")
