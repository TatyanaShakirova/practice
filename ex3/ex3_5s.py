str = raw_input("input string: ")

dic = {}
for word in str.split():
	lenth = len(word)
	if dic.get(lenth):
		dic[lenth] = dic[lenth] + "\n" + word
	else:
		dic[lenth] = word
for key in sorted(dic):
	print dic[key]