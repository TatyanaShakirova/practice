
n = input("enter number: ")

summ = 0
mult = 0 if n == 0 else 1

while n > 0:
	summ += int(n%10)
	mult *= int(n%10)
	n = n/10

print "sum =", summ, "multiple =", mult
