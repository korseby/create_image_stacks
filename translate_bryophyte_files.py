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
parser.add_argument('-V', '--verbose', dest='verbose', action='store_true', required=False,
                   help='be verbose and show what is being done')
parser.add_argument('-n', '--dry-run', dest='dryrun', action='store_true', required=False,
                   help='show what would be done')
parser.add_argument('-d', '--dir', metavar='dest_dir', dest='dest_dir', required=True,
                   help='destination directory of image files')

args = parser.parse_args()

# Verbosity
__DEBUG__ = args.verbose

# Dry-run
__DRY_RUN__ = args.dryrun

# Destination image directory
dest_dir = args.dest_dir

dest_files = sorted( filter(lambda p: p.suffix in {".CR2", ".CR3", ".DNG", ".TIF", ".JPG", ".xmp", ".XMP"}, Path(dest_dir).glob("*")) )

# Rename files
old_names = [str(Path(i)) for i in dest_files]
new_names = [str(Path(i)) for i in dest_files]

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

# Fix spelling errors
new_names = [re.sub(" Scapania nemoroea ", " Scapania nemorea ", i) for i in new_names]

# Show renaming action
if (__DRY_RUN__):
	print("The following renaming in batches will be done:")
	base_names = [re.sub("(IMG_\d\d\d\d |\.CR(2|3)|\.TIF|\.JPG|\.xmp)", "", i) for i in new_names]
	for i, label in enumerate(dict.fromkeys(base_names), start=0):
		print( label )

# Perform renaming of files on drive
if (__DRY_RUN__ == False) or (__DEBUG__ == True):
	if (len(old_names) != len(new_names)):
		print("Error! Number of old files (" + str(len(old_names)) + ") does not match number of new files (" + str(len(new_names)) + ").")
		exit(3)
	else:
		if (__DEBUG__ == True):
			for j in range(0, len(old_names)):
				if (os.path.isfile(old_names[j])):
					print('mv' + ' ' + '\"' + old_names[j] + '\"' + ' ' + '\"' + new_names[j] + '\"')
		if (__DRY_RUN__ == False):
			for j in range(0, len(old_names)):
				if (os.path.isfile(old_names[j])):
					os.rename(old_names[j], new_names[j])

if (__DEBUG__ == True): print("Renaming of " + str(len(new_names)) + " files done.")


