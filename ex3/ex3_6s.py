str = raw_input("input string: ")
vowels = list("aeiouy")
words = str.split();
str = ""
for word in words:
	newword = word
	for i in word:
		if i not in vowels:
			newword = newword[1:] + i;
		else:
			newword = newword + "ay"
			break
	else:
		newword += "ay"
	str += newword + " "
print str[:-1]