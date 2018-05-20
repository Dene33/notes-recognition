import os, sys
import glob
import shutil


dirname = os.getcwd()

toMove = os.path.join(dirname, "Images")
moved = os.path.join(dirname, "ImagesTest")

print ("Current working dir : {}".format(os.getcwd()))
os.chdir(toMove)

print(os.path.splitext("path_to_file")[0])

for file in os.listdir(toMove):
	noExt = os.path.splitext(file)[0]
	if int(noExt) >= 89984:
		filePath = os.path.join(toMove, file)
		shutil.move(filePath, moved)

