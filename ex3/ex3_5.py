
n = input()
res = n
for i in range (2, n):
    while n%i ==0:
        n = n/i
        res = i
print res	