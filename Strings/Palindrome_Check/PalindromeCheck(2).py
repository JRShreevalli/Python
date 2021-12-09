def Palindrome_Check(lst):
    if (lst == lst[::-1]):
        return True
    return False

list = [ ]
n = int(input())
for i in range(0,n):
    ele = input()
    list.append(ele)
print(Palindrome_Check(list))

