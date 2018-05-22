import os
import glob

def replace_all(text, dic):
	text = text.split(' ')
	text2 = []
	for i in text:
		print()
		if i in toReplace.keys():
			text2.append(dic[i])
	return ''.join(text2)

#######
# C4b #
#######
toReplace = {
			"flatSixteenth-C4" : "track.append(Message('note_on', note=60, velocity=100, time=0))\ntrack.append(Message('note_off', note=60, velocity=100, time=240)) #16\n",
			"flatEighth-C4" : "track.append(Message('note_on', note=60, velocity=100, time=0))\ntrack.append(Message('note_off', note=60, velocity=100, time=480)) #8\n",
			"flatQuarter-C4" : "track.append(Message('note_on', note=60, velocity=100, time=0))\ntrack.append(Message('note_off', note=60, velocity=100, time=960)) #4\n",
			"flatHalf-C4" : "track.append(Message('note_on', note=60, velocity=100, time=0))\ntrack.append(Message('note_off', note=60, velocity=100, time=1920)) #2\n",
			######
			# C4 #
			######
			"Sixteenth-C4" : 'track.append(Message(''note_on'', note=60, velocity=100, time=0))\ntrack.append(Message(''note_off'', note=60, velocity=100, time=240)) #16\n',
			"Eighth-C4" : "track.append(Message('note_on', note=60, velocity=100, time=0))\ntrack.append(Message('note_off', note=60, velocity=100, time=480)) #8\n",
			"Quarter-C4" : "track.append(Message('note_on', note=60, velocity=100, time=0))\ntrack.append(Message('note_off', note=60, velocity=100, time=960)) #4\n",
			"Half-C4" : "track.append(Message('note_on', note=60, velocity=100, time=0))\ntrack.append(Message('note_off', note=60, velocity=100, time=1920)) #2\n",
			#######
			# C#4 #
			#######
			"sharpSixteenth-C4" : "track.append(Message('note_on', note=61, velocity=100, time=0))\ntrack.append(Message('note_off', note=61, velocity=100, time=240)) #16\n",
			"sharpEighth-C4" : "track.append(Message('note_on', note=61, velocity=100, time=0))\ntrack.append(Message('note_off', note=61, velocity=100, time=480)) #8\n",
			"sharpQuarter-C4" : "track.append(Message('note_on', note=61, velocity=100, time=0))\ntrack.append(Message('note_off', note=61, velocity=100, time=960)) #4\n",
			"sharpHalf-C4" : "track.append(Message('note_on', note=61, velocity=100, time=0))\ntrack.append(Message('note_off', note=61, velocity=100, time=1920)) #2\n",
			#######
			# Db4 #
			#######
			"flatSixteenth-D4" : "track.append(Message('note_on', note=61, velocity=100, time=0))\ntrack.append(Message('note_off', note=61, velocity=100, time=240)) #16\n",
			"flatEighth-D4" : "track.append(Message('note_on', note=61, velocity=100, time=0))\ntrack.append(Message('note_off', note=61, velocity=100, time=480)) #8\n",
			"flatQuarter-D4" : "track.append(Message('note_on', note=61, velocity=100, time=0))\ntrack.append(Message('note_off', note=61, velocity=100, time=960)) #4\n",
			"flatHalf-D4" : "track.append(Message('note_on', note=61, velocity=100, time=0))\ntrack.append(Message('note_off', note=61, velocity=100, time=1920)) #2\n",
			######
			# D4 #
			######
			"Sixteenth-D4" : "track.append(Message('note_on', note=62, velocity=100, time=0))\ntrack.append(Message('note_off', note=62, velocity=100, time=240)) #16\n",
			"Eighth-D4" : "track.append(Message('note_on', note=62, velocity=100, time=0))\ntrack.append(Message('note_off', note=62, velocity=100, time=480)) #8\n",
			"Quarter-D4" : "track.append(Message('note_on', note=62, velocity=100, time=0))\ntrack.append(Message('note_off', note=62, velocity=100, time=960)) #4\n",
			"Half-D4" : "track.append(Message('note_on', note=62, velocity=100, time=0))\ntrack.append(Message('note_off', note=62, velocity=100, time=1920)) #2\n",
			#######
			# D#4 #
			#######
			"sharpSixteenth-D4" : "track.append(Message('note_on', note=63, velocity=100, time=0))\ntrack.append(Message('note_off', note=63, velocity=100, time=240)) #16\n",
			"sharpEighth-D4" : "track.append(Message('note_on', note=63, velocity=100, time=0))\ntrack.append(Message('note_off', note=63, velocity=100, time=480)) #8\n",
			"sharpQuarter-D4" : "track.append(Message('note_on', note=63, velocity=100, time=0))\ntrack.append(Message('note_off', note=63, velocity=100, time=960)) #4\n",
			"sharpHalf-D4" : "track.append(Message('note_on', note=63, velocity=100, time=0))\ntrack.append(Message('note_off', note=63, velocity=100, time=1920)) #2\n",
			#######
			# Eb4 #
			#######
			"flatSixteenth-E4" : "track.append(Message('note_on', note=63, velocity=100, time=0))\ntrack.append(Message('note_off', note=63, velocity=100, time=240)) #16\n",
			"flatEighth-E4" : "track.append(Message('note_on', note=63, velocity=100, time=0))\ntrack.append(Message('note_off', note=63, velocity=100, time=480)) #8\n",
			"flatQuarter-E4" : "track.append(Message('note_on', note=63, velocity=100, time=0))\ntrack.append(Message('note_off', note=63, velocity=100, time=960)) #4\n",
			"flatHalf-E4" : "track.append(Message('note_on', note=63, velocity=100, time=0))\ntrack.append(Message('note_off', note=63, velocity=100, time=1920)) #2\n",
			######
			# E4 #
			######
			"Sixteenth-E4" : "track.append(Message('note_on', note=64, velocity=100, time=0))\ntrack.append(Message('note_off', note=64, velocity=100, time=240)) #16\n",
			"Eighth-E4" : "track.append(Message('note_on', note=64, velocity=100, time=0))\ntrack.append(Message('note_off', note=64, velocity=100, time=480)) #8\n",
			"Quarter-E4" : "track.append(Message('note_on', note=64, velocity=100, time=0))\ntrack.append(Message('note_off', note=64, velocity=100, time=960)) #4\n",
			"Half-E4" : "track.append(Message('note_on', note=64, velocity=100, time=0))\ntrack.append(Message('note_off', note=64, velocity=100, time=1920)) #2\n",
			#######
			# E4# #
			#######
			"sharpSixteenth-E4" : "track.append(Message('note_on', note=64, velocity=100, time=0))\ntrack.append(Message('note_off', note=64, velocity=100, time=240)) #16\n",
			"sharpEighth-E4" : "track.append(Message('note_on', note=64, velocity=100, time=0))\ntrack.append(Message('note_off', note=64, velocity=100, time=480)) #8\n",
			"sharpQuarter-E4" : "track.append(Message('note_on', note=64, velocity=100, time=0))\ntrack.append(Message('note_off', note=64, velocity=100, time=960)) #4\n",
			"sharpHalf-E4" : "track.append(Message('note_on', note=64, velocity=100, time=0))\ntrack.append(Message('note_off', note=64, velocity=100, time=1920)) #2\n",			
			#######
			# F4b #
			#######
			"flatSixteenth-F4" : "track.append(Message('note_on', note=65, velocity=100, time=0))\ntrack.append(Message('note_off', note=65, velocity=100, time=240)) #16\n",
			"flatEighth-F4" : "track.append(Message('note_on', note=65, velocity=100, time=0))\ntrack.append(Message('note_off', note=65, velocity=100, time=480)) #8\n",
			"flatQuarter-F4" : "track.append(Message('note_on', note=65, velocity=100, time=0))\ntrack.append(Message('note_off', note=65, velocity=100, time=960)) #4\n",
			"flatHalf-F4" : "track.append(Message('note_on', note=65, velocity=100, time=0))\ntrack.append(Message('note_off', note=65, velocity=100, time=1920)) #2\n",
			######
			# F4 #
			######
			"Sixteenth-F4" : "track.append(Message('note_on', note=65, velocity=100, time=0))\ntrack.append(Message('note_off', note=65, velocity=100, time=240)) #16\n",
			"Eighth-F4" : "track.append(Message('note_on', note=65, velocity=100, time=0))\ntrack.append(Message('note_off', note=65, velocity=100, time=480)) #8\n",
			"Quarter-F4" : "track.append(Message('note_on', note=65, velocity=100, time=0))\ntrack.append(Message('note_off', note=65, velocity=100, time=960)) #4\n",
			"Half-F4" : "track.append(Message('note_on', note=65, velocity=100, time=0))\ntrack.append(Message('note_off', note=65, velocity=100, time=1920)) #2\n",
			#######
			# F#4 #
			#######
			"sharpSixteenth-F4" : "track.append(Message('note_on', note=66, velocity=100, time=0))\ntrack.append(Message('note_off', note=66, velocity=100, time=240)) #16\n",
			"sharpEighth-F4" : "track.append(Message('note_on', note=66, velocity=100, time=0))\ntrack.append(Message('note_off', note=66, velocity=100, time=480)) #8\n",
			"sharpQuarter-F4" : "track.append(Message('note_on', note=66, velocity=100, time=0))\ntrack.append(Message('note_off', note=66, velocity=100, time=960)) #4\n",
			"sharpHalf-F4" : "track.append(Message('note_on', note=66, velocity=100, time=0))\ntrack.append(Message('note_off', note=66, velocity=100, time=1920)) #2\n",
			#######
			# Gb4 #
			#######
			"flatSixteenth-G4" : "track.append(Message('note_on', note=66, velocity=100, time=0))\ntrack.append(Message('note_off', note=66, velocity=100, time=240)) #16\n",
			"flatEighth-G4" : "track.append(Message('note_on', note=66, velocity=100, time=0))\ntrack.append(Message('note_off', note=66, velocity=100, time=480)) #8\n",
			"flatQuarter-G4" : "track.append(Message('note_on', note=66, velocity=100, time=0))\ntrack.append(Message('note_off', note=66, velocity=100, time=960)) #4\n",
			"flatHalf-G4" : "track.append(Message('note_on', note=66, velocity=100, time=0))\ntrack.append(Message('note_off', note=66, velocity=100, time=1920)) #2\n",
			######
			# G4 #
			######
			"Sixteenth-G4" : "track.append(Message('note_on', note=67, velocity=100, time=0))\ntrack.append(Message('note_off', note=67, velocity=100, time=240)) #16\n",
			"Eighth-G4" : "track.append(Message('note_on', note=67, velocity=100, time=0))\ntrack.append(Message('note_off', note=67, velocity=100, time=480)) #8\n",
			"Quarter-G4" : "track.append(Message('note_on', note=67, velocity=100, time=0))\ntrack.append(Message('note_off', note=67, velocity=100, time=960)) #4\n",
			"Half-G4" : "track.append(Message('note_on', note=67, velocity=100, time=0))\ntrack.append(Message('note_off', note=67, velocity=100, time=1920)) #2\n",
			#######
			# G#4 #
			#######
			"sharpSixteenth-G4" : "track.append(Message('note_on', note=68, velocity=100, time=0))\ntrack.append(Message('note_off', note=68, velocity=100, time=240)) #16\n",
			"sharpEighth-G4" : "track.append(Message('note_on', note=68, velocity=100, time=0))\ntrack.append(Message('note_off', note=68, velocity=100, time=480)) #8\n",
			"sharpQuarter-G4" : "track.append(Message('note_on', note=68, velocity=100, time=0))\ntrack.append(Message('note_off', note=68, velocity=100, time=960)) #4\n",
			"sharpHalf-G4" : "track.append(Message('note_on', note=68, velocity=100, time=0))\ntrack.append(Message('note_off', note=68, velocity=100, time=1920)) #2\n",
			#######
			# Ab4 #
			#######
			"flatSixteenth-A4" : "track.append(Message('note_on', note=68, velocity=100, time=0))\ntrack.append(Message('note_off', note=68, velocity=100, time=240)) #16\n",
			"flatEighth-A4" : "track.append(Message('note_on', note=68, velocity=100, time=0))\ntrack.append(Message('note_off', note=68, velocity=100, time=480)) #8\n",
			"flatQuarter-A4" : "track.append(Message('note_on', note=68, velocity=100, time=0))\ntrack.append(Message('note_off', note=68, velocity=100, time=960)) #4\n",
			"flatHalf-A4" : "track.append(Message('note_on', note=68, velocity=100, time=0))\ntrack.append(Message('note_off', note=68, velocity=100, time=1920)) #2\n",
			######
			# A4 #
			######
			"Sixteenth-A4" : "track.append(Message('note_on', note=69, velocity=100, time=0))\ntrack.append(Message('note_off', note=69, velocity=100, time=240)) #16\n",
			"Eighth-A4" : "track.append(Message('note_on', note=69, velocity=100, time=0))\ntrack.append(Message('note_off', note=69, velocity=100, time=480)) #8\n",
			"Quarter-A4" : "track.append(Message('note_on', note=69, velocity=100, time=0))\ntrack.append(Message('note_off', note=69, velocity=100, time=960)) #4\n",
			"Half-A4" : "track.append(Message('note_on', note=69, velocity=100, time=0))\ntrack.append(Message('note_off', note=69, velocity=100, time=1920)) #2\n",
			#######
			# A#4 #
			#######
			"sharpSixteenth-A4" : "track.append(Message('note_on', note=70, velocity=100, time=0))\ntrack.append(Message('note_off', note=70, velocity=100, time=240)) #16\n",
			"sharpEighth-A4" : "track.append(Message('note_on', note=70, velocity=100, time=0))\ntrack.append(Message('note_off', note=70, velocity=100, time=480)) #8\n",
			"sharpQuarter-A4" : "track.append(Message('note_on', note=70, velocity=100, time=0))\ntrack.append(Message('note_off', note=70, velocity=100, time=960)) #4\n",
			"sharpHalf-A4" : "track.append(Message('note_on', note=70, velocity=100, time=0))\ntrack.append(Message('note_off', note=70, velocity=100, time=1920)) #2\n",
			#######
			# Bb4 #
			#######
			"flatSixteenth-B4" : "track.append(Message('note_on', note=70, velocity=100, time=0))\ntrack.append(Message('note_off', note=70, velocity=100, time=240)) #16\n",
			"flatEighth-B4" : "track.append(Message('note_on', note=70, velocity=100, time=0))\ntrack.append(Message('note_off', note=70, velocity=100, time=480)) #8\n",
			"flatQuarter-B4" : "track.append(Message('note_on', note=70, velocity=100, time=0))\ntrack.append(Message('note_off', note=70, velocity=100, time=960)) #4\n",
			"flatHalf-B4" : "track.append(Message('note_on', note=70, velocity=100, time=0))\ntrack.append(Message('note_off', note=70, velocity=100, time=1920)) #2\n",
			######
			# B4 #
			######
			"Sixteenth-B4" : "track.append(Message('note_on', note=71, velocity=100, time=0))\ntrack.append(Message('note_off', note=71, velocity=100, time=240)) #16\n",
			"Eighth-B4" : "track.append(Message('note_on', note=71, velocity=100, time=0))\ntrack.append(Message('note_off', note=71, velocity=100, time=480)) #8\n",
			"Quarter-B4" : "track.append(Message('note_on', note=71, velocity=100, time=0))\ntrack.append(Message('note_off', note=71, velocity=100, time=960)) #4\n",
			"Half-B4" : "track.append(Message('note_on', note=71, velocity=100, time=0))\ntrack.append(Message('note_off', note=71, velocity=100, time=1920)) #2\n",
			#######
			# B4# #
			#######
			"sharpSixteenth-B4" : "track.append(Message('note_on', note=71, velocity=100, time=0))\ntrack.append(Message('note_off', note=71, velocity=100, time=240)) #16\n",
			"sharpEighth-B4" : "track.append(Message('note_on', note=71, velocity=100, time=0))\ntrack.append(Message('note_off', note=71, velocity=100, time=480)) #8\n",
			"sharpQuarter-B4" : "track.append(Message('note_on', note=71, velocity=100, time=0))\ntrack.append(Message('note_off', note=71, velocity=100, time=960)) #4\n",
			"sharpHalf-B4" : "track.append(Message('note_on', note=71, velocity=100, time=0))\ntrack.append(Message('note_off', note=71, velocity=100, time=1920)) #2\n",
			#######
			# C5b #
			#######
			"flatSixteenth-C5" : "track.append(Message('note_on', note=72, velocity=100, time=0))\ntrack.append(Message('note_off', note=72, velocity=100, time=240)) #16\n",
			"flatEighth-C5" : "track.append(Message('note_on', note=72, velocity=100, time=0))\ntrack.append(Message('note_off', note=72, velocity=100, time=480)) #8\n",
			"flatQuarter-C5" : "track.append(Message('note_on', note=72, velocity=100, time=0))\ntrack.append(Message('note_off', note=72, velocity=100, time=972)) #4\n",
			"flatHalf-C5" : "track.append(Message('note_on', note=72, velocity=100, time=0))\ntrack.append(Message('note_off', note=72, velocity=100, time=1920)) #2\n",			
			######
			# C5 #
			######
			"Sixteenth-C5" : "track.append(Message('note_on', note=72, velocity=100, time=0))\ntrack.append(Message('note_off', note=72, velocity=100, time=240)) #16\n",
			"Eighth-C5" : "track.append(Message('note_on', note=72, velocity=100, time=0))\ntrack.append(Message('note_off', note=72, velocity=100, time=480)) #8\n",
			"Quarter-C5" : "track.append(Message('note_on', note=72, velocity=100, time=0))\ntrack.append(Message('note_off', note=72, velocity=100, time=972)) #4\n",
			"Half-C5" : "track.append(Message('note_on', note=72, velocity=100, time=0))\ntrack.append(Message('note_off', note=72, velocity=100, time=1920)) #2\n",
			#######
			# C#5 #
			#######
			"sharpSixteenth-C5" : "track.append(Message('note_on', note=73, velocity=100, time=0))\ntrack.append(Message('note_off', note=73, velocity=100, time=240)) #16\n",
			"sharpEighth-C5" : "track.append(Message('note_on', note=73, velocity=100, time=0))\ntrack.append(Message('note_off', note=73, velocity=100, time=480)) #8\n",
			"sharpQuarter-C5" : "track.append(Message('note_on', note=73, velocity=100, time=0))\ntrack.append(Message('note_off', note=73, velocity=100, time=960)) #4\n",
			"sharpHalf-C5" : "track.append(Message('note_on', note=73, velocity=100, time=0))\ntrack.append(Message('note_off', note=73, velocity=100, time=1920)) #2\n",
			#######
			# Db5 #
			#######
			"flatSixteenth-D5" : "track.append(Message('note_on', note=73, velocity=100, time=0))\ntrack.append(Message('note_off', note=73, velocity=100, time=240)) #16\n",
			"flatEighth-D5" : "track.append(Message('note_on', note=73, velocity=100, time=0))\ntrack.append(Message('note_off', note=73, velocity=100, time=480)) #8\n",
			"flatQuarter-D5" : "track.append(Message('note_on', note=73, velocity=100, time=0))\ntrack.append(Message('note_off', note=73, velocity=100, time=960)) #4\n",
			"flatHalf-D5" : "track.append(Message('note_on', note=73, velocity=100, time=0))\ntrack.append(Message('note_off', note=73, velocity=100, time=1920)) #2\n",
			######
			# D5 #
			######
			"Sixteenth-D5" : "track.append(Message('note_on', note=74, velocity=100, time=0))\ntrack.append(Message('note_off', note=74, velocity=100, time=240)) #16\n",
			"Eighth-D5" : "track.append(Message('note_on', note=74, velocity=100, time=0))\ntrack.append(Message('note_off', note=74, velocity=100, time=480)) #8\n",
			"Quarter-D5" : "track.append(Message('note_on', note=74, velocity=100, time=0))\ntrack.append(Message('note_off', note=74, velocity=100, time=960)) #4\n",
			"Half-D5" : "track.append(Message('note_on', note=74, velocity=100, time=0))\ntrack.append(Message('note_off', note=74, velocity=100, time=1920)) #2\n",
			#######
			# D#5 #
			#######
			"sharpSixteenth-D5" : "track.append(Message('note_on', note=75, velocity=100, time=0))\ntrack.append(Message('note_off', note=75, velocity=100, time=240)) #16\n",
			"sharpEighth-D5" : "track.append(Message('note_on', note=75, velocity=100, time=0))\ntrack.append(Message('note_off', note=75, velocity=100, time=480)) #8\n",
			"sharpQuarter-D5" : "track.append(Message('note_on', note=75, velocity=100, time=0))\ntrack.append(Message('note_off', note=75, velocity=100, time=960)) #4\n",
			"sharpHalf-D5" : "track.append(Message('note_on', note=75, velocity=100, time=0))\ntrack.append(Message('note_off', note=75, velocity=100, time=1920)) #2\n",
			#######
			# Eb5 #
			#######
			"flatSixteenth-E5" : "track.append(Message('note_on', note=75, velocity=100, time=0))\ntrack.append(Message('note_off', note=75, velocity=100, time=240)) #16\n",
			"flatEighth-E5" : "track.append(Message('note_on', note=75, velocity=100, time=0))\ntrack.append(Message('note_off', note=75, velocity=100, time=480)) #8\n",
			"flatQuarter-E5" : "track.append(Message('note_on', note=75, velocity=100, time=0))\ntrack.append(Message('note_off', note=75, velocity=100, time=960)) #4\n",
			"flatHalf-E5" : "track.append(Message('note_on', note=75, velocity=100, time=0))\ntrack.append(Message('note_off', note=75, velocity=100, time=1920)) #2\n",
			######
			# E5 #
			######
			"Sixteenth-E5" : "track.append(Message('note_on', note=76, velocity=100, time=0))\ntrack.append(Message('note_off', note=76, velocity=100, time=240)) #16\n",
			"Eighth-E5" : "track.append(Message('note_on', note=76, velocity=100, time=0))\ntrack.append(Message('note_off', note=76, velocity=100, time=480)) #8\n",
			"Quarter-E5" : "track.append(Message('note_on', note=76, velocity=100, time=0))\ntrack.append(Message('note_off', note=76, velocity=100, time=960)) #4\n",
			"Half-E5" : "track.append(Message('note_on', note=76, velocity=100, time=0))\ntrack.append(Message('note_off', note=76, velocity=100, time=1920)) #2\n",
			#######
			# E5# #
			#######
			"sharpSixteenth-E5" : "track.append(Message('note_on', note=76, velocity=100, time=0))\ntrack.append(Message('note_off', note=76, velocity=100, time=240)) #16\n",
			"sharpEighth-E5" : "track.append(Message('note_on', note=76, velocity=100, time=0))\ntrack.append(Message('note_off', note=76, velocity=100, time=480)) #8\n",
			"sharpQuarter-E5" : "track.append(Message('note_on', note=76, velocity=100, time=0))\ntrack.append(Message('note_off', note=76, velocity=100, time=960)) #4\n",
			"sharpHalf-E5" : "track.append(Message('note_on', note=76, velocity=100, time=0))\ntrack.append(Message('note_off', note=76, velocity=100, time=1920)) #2\n",
			#########
			# pause #
			#########
			"Sixteenth-REST" : "track.append(Message('note_on', note=0, velocity=0, time=0))\ntrack.append(Message('note_off', note=0, velocity=0, time=240)) #16\n",
			"Eighth-REST" : "track.append(Message('note_on', note=0, velocity=0, time=0))\ntrack.append(Message('note_off', note=0, velocity=0, time=480)) #8\n",
			"Quarter-REST" : "track.append(Message('note_on', note=0, velocity=0, time=0))\ntrack.append(Message('note_off', note=0, velocity=0, time=960)) #4\n",
			"Half-REST" : "track.append(Message('note_on', note=0, velocity=0, time=0))\ntrack.append(Message('note_off', note=0, velocity=0, time=1920)) #2\n",
			##########
			# pauseb #
			#########
			"flatSixteenth-REST" : "track.append(Message('note_on', note=0, velocity=0, time=0))\ntrack.append(Message('note_off', note=0, velocity=0, time=240)) #16\n",
			"flatEighth-REST" : "track.append(Message('note_on', note=0, velocity=0, time=0))\ntrack.append(Message('note_off', note=0, velocity=0, time=480)) #8\n",
			"flatQuarter-REST" : "track.append(Message('note_on', note=0, velocity=0, time=0))\ntrack.append(Message('note_off', note=0, velocity=0, time=960)) #4\n",
			"flatHalf-REST" : "track.append(Message('note_on', note=0, velocity=0, time=0))\ntrack.append(Message('note_off', note=0, velocity=0, time=1920)) #2\n",
			##########
			# pause# #
			##########
			"sharpSixteenth-REST" : "track.append(Message('note_on', note=0, velocity=0, time=0))\ntrack.append(Message('note_off', note=0, velocity=0, time=240)) #16\n",
			"sharpEighth-REST" : "track.append(Message('note_on', note=0, velocity=0, time=0))\ntrack.append(Message('note_off', note=0, velocity=0, time=480)) #8\n",
			"sharpQuarter-REST" : "track.append(Message('note_on', note=0, velocity=0, time=0))\ntrack.append(Message('note_off', note=0, velocity=0, time=960)) #4\n",
			"sharpHalf-REST" : "track.append(Message('note_on', note=0, velocity=0, time=0))\ntrack.append(Message('note_off', note=0, velocity=0, time=1920)) #2\n",
			"ClefG" : "",
			"T44" : "",
			"flatT44" : "",
			"flatflatT44" : "",
			"flatflatflatT44" : "",
			"flatflatflatflatT44" : "",
			"flatflatflatflatflatT44" : "",
			"flatflatflatflatflatflatT44" : "",
			"flatflatflatflatflatflatflatT44" : "",	
			"T34" : "",
			"flatT34" : "",
			"flatflatT34" : "",
			"flatflatflatT34" : "",
			"flatflatflatflatT34" : "",
			"flatflatflatflatflatT34" : "",
			"flatflatflatflatflatflatT34" : "",
			"flatflatflatflatflatflatflatT34" : "",
			"T68" : "",
			"flatT68" : "",
			"flatflatT68" : "",
			"flatflatflatT68" : "",
			"flatflatflatflatT68" : "",
			"flatflatflatflatflatT68" : "",
			"flatflatflatflatflatflatT68" : "",
			"flatflatflatflatflatflatflatT68" : "",
			"T44" : "",
			"sharpT44" : "",
			"sharpsharpT44" : "",
			"sharpsharpsharpT44" : "",
			"sharpsharpsharpsharpT44" : "",
			"sharpsharpsharpsharpsharpT44" : "",
			"sharpsharpsharpsharpsharpsharpT44" : "",
			"sharpsharpsharpsharpsharpsharpsharpT44" : "",	
			"T34" : "",
			"sharpT34" : "",
			"sharpsharpT34" : "",
			"sharpsharpsharpT34" : "",
			"sharpsharpsharpsharpT34" : "",
			"sharpsharpsharpsharpsharpT34" : "",
			"sharpsharpsharpsharpsharpsharpT34" : "",
			"sharpsharpsharpsharpsharpsharpsharpT34" : "",
			"T68" : "",
			"sharpT68" : "",
			"sharpsharpT68" : "",
			"sharpsharpsharpT68" : "",
			"sharpsharpsharpsharpT68" : "",
			"sharpsharpsharpsharpsharpT68" : "",
			"sharpsharpsharpsharpsharpsharpT68" : "",
			"sharpsharpsharpsharpsharpsharpsharpT68" : "",
			"bar" : "",
			"sharpbar" : "",
			"bar" : "",
			"flatbar" : "",
			"natural" : "",
			"flatnatural" : "",
			"sharpnatural" : "",
			"flat" : "",
			"sharp" : ""}

directory_in_str = os.getcwd()
#print(directory_in_str)

midoBeforeNotes = "import os\nimport sys\nimport mido\nfrom mido import MidiFile\nfrom mido import Message, MidiFile, MidiTrack, MetaMessage\noutputs = mido.get_output_names()\nportname = None\nmid = MidiFile()\ntrack = MidiTrack()\nmid.tracks.append(track)\ntrack.append(Message('program_change', program=12))\n"

midoAfterNotes = "dirPath = os.getcwd()\nprint(dirPath)\ndir = os.path.basename(dirPath)\nprint(dir)\nmid.save(dir + '.mid')\nwith mido.open_output(portname) as output:\n    try:\n        for message in mid.play():\n            print(message)\n            output.send(message)\n    except KeyboardInterrupt:\n        print()\n        output.reset()\n"

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
	
		with open(word, 'r') as fin:
			data = fin.read().splitlines(True)
		with open(word, 'w') as fout:
			fout.writelines(data[0])
		file = open(word, 'r').read().rstrip()
		replace = replace_all(file,toReplace)
		file = open("./" + folder + '/playMIDI.py', 'w')
		file.write(midoBeforeNotes)
		file.write(replace)
		file.write(midoAfterNotes)
		file.close()
		#base = os.path.splitext(word)[0]
		#os.rename(word, base + ".py")
		print(file)