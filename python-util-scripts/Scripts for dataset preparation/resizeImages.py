import os, sys
import glob
import shutil
from PIL import Image


dirname = os.getcwd()

toMove = os.path.join(dirname, "toMove")
#moved = os.path.join(dirname, "ImagesTest")

print ("Current working dir : {}".format(os.getcwd()))
os.chdir(toMove)
print ("Current working dir : {}".format(os.getcwd()))

size = 1000,60
target_width = 60

for file in os.listdir(toMove):
	img = Image.open(file)
	(width, height) = img.size   
	#print(width,height)
	target_height = int(height * (1.0 * target_width / width))   
	img.thumbnail(size)
	img.save(file)
	(new_width, new_height) = img.size  
	print(new_width,new_height)