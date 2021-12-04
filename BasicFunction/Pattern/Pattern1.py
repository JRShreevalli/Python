def program(n):
	for i in range(1, n+1):
		for j in range(1, i+1):
			print("* ",end="")
		print("\r")

n = int(input())
program(n)

# to get gap after each row use -->  \r
