import os, sys
import glob


dirname = os.getcwd()

images = os.path.join(dirname, "Images")
labels = os.path.join(dirname, "labels")

os.chdir(images)
print ("Current working dir : {}".format(os.getcwd()))
sample = open('sample.txt','a')
os.chdir(labels)
labelsDir = os.listdir(labels)
i=0
#print(labelsDir)

for file in os.listdir(images):
	if not file.endswith(".txt"):
		data = open(labelsDir[i], 'r').read()
		print("./Images/"+str(file)+data)
		sample.write("./Images/"+str(file)+" "+data+"\n")
		i += 1


