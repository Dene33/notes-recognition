import os
import glob

def replace_all(text, dic):
	#print(text)
	text = list(text)
	text2 = []
	for i in text:
		text2.append(dic[i])
	print(text2)
	return ''.join(text2)

toReplace = {"!" : "Sixteenth-C4 ",
			'"' : "Sixteenth-D4 ",
			"#" : "Sixteenth-E4 ",
			"$" : "Sixteenth-F4 ",
			"%" : "Sixteenth-G4 ",
			"&" : "Sixteenth-A4 ",
			"'" : "Sixteenth-B4 ",
			"(" : "Sixteenth-C5 ",
			")" : "Sixteenth-D5 ",
			"*" : "Sixteenth-E5 ",
			"+" : "Sixteenth-REST ",
			"," : "Quarter-C4 ",
			"-" : "Quarter-D4 ",
			"." : "Quarter-E4 ",
			"/" : "Quarter-F4 ",
			"0" : "Quarter-G4 ",
			"1" : "Quarter-A4 ",
			"2" : "Quarter-B4 ",
			"3" : "Quarter-C5 ",
			"4" : "Quarter-D5 ",
			"5" : "Quarter-E5 ",
			"6" : "Quarter-REST ",
			"7" : "Eighth-C4 ",
			"8" : "Eighth-D4 ",
			"9" : "Eighth-E4 ",
			":" : "Eighth-F4 ",
			";" : "Eighth-G4 ",
			"<" : "Eighth-A4 ",
			"=" : "Eighth-B4 ",
			">" : "Eighth-C5 ",
			"?" : "Eighth-D5 ",
			"@" : "Eighth-E5 ",
			"A" : "Eighth-REST ",
			"B" : "Half-C4 ",
			"C" : "Half-D4 ",
			"D" : "Half-E4 ",
			"E" : "Half-F4 ",
			"F" : "Half-G4 ",
			"G" : "Half-A4 ",
			"H" : "Half-B4 ",
			"I" : "Half-C5 ",
			"J" : "Half-D5 ",
			"K" : "Half-E5 ",
			"L" : "Half-REST ",
			"M" : "ClefG ",
			"N" : "T44 ",
			"O" : "T34 ",
			"P" : "T68 ",
			"Q" : "bar ",
			"R" : "sharp ",
			"S" : "flat ",
			"T" : "natural ",
			"\n" : "\n"}

directory_in_str = os.getcwd()
#print(directory_in_str)
i=0

for folder in os.listdir(directory_in_str):
	if not folder.endswith(".py") and not folder.endswith(".txt"):
		fldrRename = os.rename(folder, str(i+1))
		i += 1

for folder in os.listdir(directory_in_str):
	print(folder)
	if not folder.endswith(".py") and not folder.endswith(".txt"):
		word = str("./" + folder + "/word.txt")
		print(word)
		#filename = os.fsdecode(file)

		#if filename.endswith(".txt"):
			#addSpace = open(file, 'a')
			#addSpace.write(" ")
			#addSpace.close()
	
		#with open(word, 'r') as fin:
		#	data = fin.read().splitlines(True)
		#with open(word, 'w') as fout:
		#	fout.writelines(data[0])
		file = open(word, 'r').read().rstrip()
		replace = replace_all(file,toReplace)
		file = open(word, 'w')
		file.write(replace)
		print(file)