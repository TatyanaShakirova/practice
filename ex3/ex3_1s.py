s = raw_input("input string: ")

dic = {"digits": 0.0, "alphas": 0.0, "others": 0.0}
lenth = len(s)

for i in s:
	if i.isdigit():
		dic["digits"] += 1
	elif i.isalpha():
		dic["alphas"] += 1
	else:
		dic["others"] += 1

for i in dic.keys():
	print i, round(dic[i] / lenth * 100, 2)