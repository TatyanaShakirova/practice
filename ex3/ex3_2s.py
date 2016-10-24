str = raw_input("input string: ")

res = 0
word = 0
for i in str:
	if i.isspace():
		if word != 0:
			res = word if res == 0 else min(res,word)
		word = 0
	else:
		word += 1
if word != 0:
	res = word if res == 0 else min(res,word)
print res