
n = input()
res = "true"
for i in range(2, n):
	if n % i == 0:
		res = "false"
		break
print res	