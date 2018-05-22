import os

def replace_all(text, dic):
	text = text.split(' ')
	text2 = []
	for i in text:
		text2.append(dic[i])
	return ''.join(text2)

toReplace = {"0" : "!",
			"1" : '"',
			"2" : "#",
			"3" : "$",
			"4" : "%",
			"5" : "&",
			"6" : "'",
			"7" : "(",
			"8" : ")",
			"9" : "*",
			"10" : "+",
			"11" : ",",
			"12" : "-",
			"13" : ".",
			"14" : "/",
			"15" : "0",
			"16" : "1",
			"17" : "2",
			"18" : "3",
			"19" : "4",
			"20" : "5",
			"21" : "6",
			"22" : "7",
			"23" : "8",
			"24" : "9",
			"25" : ":",
			"26" : ";",
			"27" : "<",
			"28" : "=",
			"29" : ">",
			"30" : "?",
			"31" : "@",
			"32" : "A",
			"33" : "B",
			"34" : "C",
			"35" : "D",
			"36" : "E",
			"37" : "F",
			"38" : "G",
			"39" : "H",
			"40" : "I",
			"41" : "J",
			"42" : "K",
			"43" : "L",
			"44" : "M",
			"45" : "N",
			"46" : "O",
			"47" : "P",
			"48" : "Q",
			"49" : "R",
			"50" : "S",
			"51" : "T"}

directory_in_str = os.getcwd()
print(directory_in_str)

for file in os.listdir(directory_in_str):
	filename = os.fsdecode(file)
	if filename.endswith(".txt"):
		#addSpace = open(file, 'a')
		#addSpace.write(" ")
		#addSpace.close()
		str = open(file, 'r').read()
		print(str)
		#print(filename)
		#print(os.path.join(directory_in_str, filename))
		str = replace_all(str,toReplace)
		print(str)
		file = open(file, 'w')
		file.write(str)
		file.close() 
		#continue
	else:
		continue