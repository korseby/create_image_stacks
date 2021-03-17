#!/usr/bin/env python

# Load modules
import errno
import sys
import os
import argparse
import glob
from pathlib import Path
import re

# Parse arguments
parser = argparse.ArgumentParser(description='Rename image files and translate german terms to english term.')
parser.add_argument('-v', '--version', action='version', version='Translate bryophyte files Version 0.3',
                   help='show version')
parser.add_argument('-n', '--dry-run', dest='dryrun', action='store_true', required=False,
                   help='show what would be done')
parser.add_argument('-d', '--dir', metavar='dest_dir', dest='dest_dir', required=True,
                   help='destination directory of image files')

args = parser.parse_args()

# Dry-run
__DRY_RUN__ = args.dryrun

# Destination image directory
dest_dir = args.dest_dir

dest_files = sorted( filter(lambda p: p.suffix in {".CR2", ".CR3", ".DNG", ".TIF", ".JPG", ".xmp", ".XMP"}, Path(dest_dir).glob("*")) )

# Rename files
old_names = [Path(i).stem for i in dest_files]
new_names = [Path(i).stem for i in dest_files]
new_names = [re.sub(" Antheridien ", " antheridia ", i) for i in new_names]
new_names = [re.sub(" Antheridiumgameten ", " gametophytes ", i) for i in new_names]
new_names = [re.sub(" Antheridium ", " antheridium ", i) for i in new_names]
new_names = [re.sub(" Archegonien ", " archegonia ", i) for i in new_names]
new_names = [re.sub(" Archegonium ", " archegonium ", i) for i in new_names]
new_names = [re.sub(" Aufsicht ", " anterior view ", i) for i in new_names]
new_names = [re.sub(" Blatt Querschnitt ", " leaf cross section ", i) for i in new_names]
new_names = [re.sub(" Blattbasis ", " leaf base ", i) for i in new_names]
new_names = [re.sub(" Blattlappen ", " leaf lobes ", i) for i in new_names]
new_names = [re.sub(" Blattmitte ", " leaf center ", i) for i in new_names]
new_names = [re.sub(" Blattrand ", " leaf margin ", i) for i in new_names]
new_names = [re.sub(" Blattspitze ", " leaf apex ", i) for i in new_names]
new_names = [re.sub(" Blatt ", " leaf ", i) for i in new_names]
new_names = [re.sub(" Brutgemmen ", " gemmae ", i) for i in new_names]
new_names = [re.sub(" Brutkoerper ", " gemmae ", i) for i in new_names]
new_names = [re.sub(" Elateren ", " elaters ", i) for i in new_names]
new_names = [re.sub(" Elatere ", " elater ", i) for i in new_names]
new_names = [re.sub(" Flankenblatt ", " lateral leaf ", i) for i in new_names]
new_names = [re.sub(" Gemmen ", " gemmae ", i) for i in new_names]
new_names = [re.sub(" geoeffneten ", " opened ", i) for i in new_names]
new_names = [re.sub(" geoeffnete ", " opened ", i) for i in new_names]
new_names = [re.sub(" geoeffnet ", " opened ", i) for i in new_names]
new_names = [re.sub(" geoffnete ", " opened ", i) for i in new_names]
new_names = [re.sub(" Habitus ", " stature ", i) for i in new_names]
new_names = [re.sub(" Herbarbeleg ", " voucher specimen ", i) for i in new_names]
new_names = [re.sub(" Herbarbeleg$", " voucher specimen", i) for i in new_names]
new_names = [re.sub(" Innenseite ", " interior side ", i) for i in new_names]
new_names = [re.sub(" Kapsel ", " capsule ", i) for i in new_names]
new_names = [re.sub(" kollenchymatisch verdickt ", " collenchym ", i) for i in new_names]
new_names = [re.sub(" maennliches ", " male ", i) for i in new_names]
new_names = [re.sub(" maennlichen ", " male ", i) for i in new_names]
new_names = [re.sub(" maennliche ", " male ", i) for i in new_names]
new_names = [re.sub(" maennlich ", " male ", i) for i in new_names]
new_names = [re.sub(" mit ", " with ", i) for i in new_names]
new_names = [re.sub(" Oberlappen ", " antical lobe ", i) for i in new_names]
new_names = [re.sub(" Oberseite ", " ventral side ", i) for i in new_names]
new_names = [re.sub(" Paraphysen ", " paraphyses ", i) for i in new_names]
new_names = [re.sub(" Perianthmuendung ", " perianth mouth ", i) for i in new_names]
new_names = [re.sub(" Perianthien ", " perianths ", i) for i in new_names]
new_names = [re.sub(" Perianth ", " perianth ", i) for i in new_names]
new_names = [re.sub(" Querschnitt ", " cross section ", i) for i in new_names]
new_names = [re.sub(" Seitenansicht ", " lateral side ", i) for i in new_names]
new_names = [re.sub(" Sporogonen ", " sporphytes ", i) for i in new_names]
new_names = [re.sub(" Sporogon ", " sporphyte ", i) for i in new_names]
new_names = [re.sub(" Sporenkapseln ", " spore capsules ", i) for i in new_names]
new_names = [re.sub(" Sporenkapsel ", " spore capsule ", i) for i in new_names]
new_names = [re.sub(" Sporen ", " spores ", i) for i in new_names]
new_names = [re.sub(" Spore ", " spore ", i) for i in new_names]
new_names = [re.sub(" Staemmchen ", " stem ", i) for i in new_names]
new_names = [re.sub(" Thallus ", " thallus ", i) for i in new_names]
new_names = [re.sub(" und ", " and ", i) for i in new_names]
new_names = [re.sub(" Unterblatt ", " underleaf ", i) for i in new_names]
new_names = [re.sub(" Unterlappen ", " postical lobe ", i) for i in new_names]
new_names = [re.sub(" Unterseite ", " dorsal side ", i) for i in new_names]
new_names = [re.sub(" weibliches ", " female ", i) for i in new_names]
new_names = [re.sub(" weiblichen ", " female ", i) for i in new_names]
new_names = [re.sub(" weibliche ", " female ", i) for i in new_names]
new_names = [re.sub(" weiblich ", " female ", i) for i in new_names]
new_names = [re.sub(" Zellen ", " cells ", i) for i in new_names]

new_names = [re.sub(" Scapania nemoroea ", " Scapania nemorea ", i) for i in new_names]

base_names = [re.sub("IMG_\d\d\d\d ", "", i) for i in new_names]
#for i, label in enumerate(base_names, start=0):
#	print( base_names[i] )
for i, label in enumerate(dict.fromkeys(base_names), start=0):
	print( label )
#print( dict.fromkeys(base_names) )

exit()

# Some information
if (__DEBUG__) or (__DRY_RUN__):
	print("Number of image files: " + str(len(img_files)))

# Check whether number of input and output files match
if (len(xmp_files) != len(img_files)):
	if (__FORCE__ == True):
		if (len(img_files) <= 0):
			extension=".TIF"
		else:
			extension = os.path.splitext(img_files[0])[1]
		img_files = [Path(i).stem for i in xmp_files]
		img_files = [''.join([img_dir, '/', f, extension]) for f in img_files]
	else:
		print("Error! Number of xmp files (" + str(len(xmp_files)) + ") does not match number of image files (" + str(len(img_files)) + ").")
		exit(3)

# Image files and names
img_bases = [Path(i).stem for i in img_files]
img_exts = [os.path.splitext(f)[1] for f in img_files]
img_names = [re.sub("IMG_\d\d\d\d ", "", i) for i in img_bases]
img_nums = [re.sub("(IMG_|\ .*)", "", i) for i in img_bases]

# Create stacks
img_stacks = []
stack_start = 1
stack_end = 1
stack_label = ""
for i, label in enumerate(xmp_labels, start=1):
	if (i >= len(xmp_labels)) or (label != stack_label) or (label == ""):
		if (i == 1) or (i >= len(xmp_labels)):
			stack_end = i
		else:
			stack_end = i-1
		stack_label = label
		
		# Singular file
		if (stack_start == stack_end):
			if ((__DEBUG__ == True) and (os.path.isfile(img_nums[stack_start-1]))): print('Singular file: ' + 'IMG_' + img_nums[stack_start-1] + ' ' + img_names[stack_start-1])
		# Stack with several files
		else:
			# Create directory for stack
			dir_name = list(set(img_names[stack_start-1:stack_end]))
			if (len(dir_name) == 0):
				print("Error! No names in stack.")
				exit(4)
			elif (len(dir_name) > 1):
				print("Error! More than one unique name in stack.")
				exit(5)
			dir_name = str(str(img_dir) + '/' + 'IMG_' + img_nums[stack_start-1] + '-' + img_nums[stack_end-1] + ' ' + str(dir_name[0]) + '/')
			if (__DEBUG__ == True):
				if ((os.path.isfile(img_files[stack_start-1])) or ((__FORCE__ == True) and (__DIRS_ONLY__ == True))):
					print('mkdir' + ' ' + '\"' + dir_name + '\"')
			if (__DRY_RUN__ == False):
				if ((os.path.isfile(img_files[stack_start-1])) or ((__FORCE__ == True) and (__DIRS_ONLY__ == True))):
					os.makedirs(dir_name, exist_ok=True)
			
			# Move files into directory (stack)
			if (__DIRS_ONLY__ == False):
				dir_files = img_files[stack_start-1:stack_end]
				dir_bases = img_bases[stack_start-1:stack_end]
				dir_exts = img_exts[stack_start-1:stack_end]
				if (__DEBUG__ == True):
					for j in range(0, len(dir_files)):
						if (os.path.isfile(dir_files[j])):
							print('mv' + ' ' + '\"' + dir_files[j] + '\"' + ' ' + '\"' + str(dir_name + '/' + dir_bases[j] + dir_exts[j]) + '\"')
				if (__DRY_RUN__ == False):
					for j in range(0, len(dir_files)):
						if (os.path.isfile(dir_files[j])):
							os.rename(dir_files[j], str(dir_name + '/' + dir_bases[j] + dir_exts[j]))
		
		stack_start = i

if (__DEBUG__ == True): print("Done.")
