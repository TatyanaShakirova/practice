
n = input("input number: ")

summ, mult = 0, 1
for i in list(str(n)):
	summ += int(i)
	mult *= int(i)
print "sum =", summ, "\nmultiple =", mult
