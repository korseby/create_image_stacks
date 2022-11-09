#!/usr/bin/env python

# Load modules
import errno
import sys
import os
import argparse
import glob
from pathlib import Path
import re



# -------------------- Arguments --------------------
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
parser.add_argument('-r', '--recursive', dest='recursive', action='store_true', required=False,
                   help='recurse into subdirectories and also rename subdirectories')

args = parser.parse_args()

# Verbosity
__DEBUG__ = args.verbose

# Dry-run
__DRY_RUN__ = args.dryrun

# Recursive
__RECURSIVE__ = args.recursive

# Destination image directory
dest_dir = args.dest_dir



# -------------------- Rename files --------------------
def rename_files(dest_files):
	# Rename files
	old_names = [str(Path(i)) for i in dest_files]
	new_names = [str(Path(i)) for i in dest_files]
	
	new_names = [re.sub(" am ", " on ", i) for i in new_names]
	new_names = [re.sub(" an ", " on ", i) for i in new_names]
	new_names = [re.sub(" Ansatzstelle ", " ", i) for i in new_names]
	new_names = [re.sub(" Antheridienstand ", " antheridiophore ", i) for i in new_names]
	new_names = [re.sub(" Antheridien ", " antheridia ", i) for i in new_names]
	new_names = [re.sub(" Antheridiumgameten ", " gametophytes ", i) for i in new_names]
	new_names = [re.sub(" Antheridium ", " antheridium ", i) for i in new_names]
	new_names = [re.sub(" Archegonienstand ", " archegoniophore ", i) for i in new_names]
	new_names = [re.sub(" Archegonien ", " archegonia ", i) for i in new_names]
	new_names = [re.sub(" Archegonium ", " archegonium ", i) for i in new_names]
	new_names = [re.sub(" Atemporen ", " air pores ", i) for i in new_names]
	new_names = [re.sub(" Atempore ", " air pore ", i) for i in new_names]
	new_names = [re.sub(" Aufsicht ", " anterior view ", i) for i in new_names]
	new_names = [re.sub(" Balgen ", " macro bellow ", i) for i in new_names]
	new_names = [re.sub(" Balgengeraet ", " macro bellow ", i) for i in new_names]
	new_names = [re.sub(" basales ", " basal ", i) for i in new_names]
	new_names = [re.sub(" basaler ", " basal ", i) for i in new_names]
	new_names = [re.sub(" basalen ", " basal ", i) for i in new_names]
	new_names = [re.sub(" basale ", " basal ", i) for i in new_names]
	new_names = [re.sub(" Bauchschuppen ", " ventral scales ", i) for i in new_names]
	new_names = [re.sub(" Bauchschuppe ", " ventral scale ", i) for i in new_names]
	new_names = [re.sub(" Blatt Querschnitt ", " leaf cross section ", i) for i in new_names]
	new_names = [re.sub(" Blattachsel ", " leaf axis ", i) for i in new_names]
	new_names = [re.sub(" Blattbasis ", " leaf base ", i) for i in new_names]
	new_names = [re.sub(" Blattgrund ", " leaf base ", i) for i in new_names]
	new_names = [re.sub(" Blattlappen ", " leaf lobes ", i) for i in new_names]
	new_names = [re.sub(" Blattmitte ", " leaf center ", i) for i in new_names]
	new_names = [re.sub(" Blattrand ", " leaf margin ", i) for i in new_names]
	new_names = [re.sub(" Blattsaum ", " bordered margin ", i) for i in new_names]
	new_names = [re.sub(" Blattspitze ", " leaf apex ", i) for i in new_names]
	new_names = [re.sub(" Blatt ", " leaf ", i) for i in new_names]
	new_names = [re.sub(" breit ", " wide ", i) for i in new_names]
	new_names = [re.sub(" Brutblatt ", " perigon leaf ", i) for i in new_names]
	new_names = [re.sub(" Brutbecher ", " gemmae cup ", i) for i in new_names]
	new_names = [re.sub(" Brutgemmen ", " gemmae ", i) for i in new_names]
	new_names = [re.sub(" Brutgemme ", " gemmae ", i) for i in new_names]
	new_names = [re.sub(" Brutkoerper ", " gemmae ", i) for i in new_names]
	new_names = [re.sub(" Elateren ", " elaters ", i) for i in new_names]
	new_names = [re.sub(" Elatere ", " elater ", i) for i in new_names]
	new_names = [re.sub(" erweitertes ", " extended ", i) for i in new_names]
	new_names = [re.sub(" erweiterter ", " extended ", i) for i in new_names]
	new_names = [re.sub(" erweiterte ", " extended ", i) for i in new_names]
	new_names = [re.sub(" erweitert ", " extended ", i) for i in new_names]
	new_names = [re.sub(" Flankenblatt ", " lateral leaf ", i) for i in new_names]
	new_names = [re.sub(" Gemmen ", " gemmae ", i) for i in new_names]
	new_names = [re.sub(" geoeffneten ", " opened ", i) for i in new_names]
	new_names = [re.sub(" geoeffnete ", " opened ", i) for i in new_names]
	new_names = [re.sub(" geoeffnet ", " opened ", i) for i in new_names]
	new_names = [re.sub(" geoffnete ", " opened ", i) for i in new_names]
	new_names = [re.sub(" gerundetes ", " rounded ", i) for i in new_names]
	new_names = [re.sub(" gerundeter ", " rounded ", i) for i in new_names]
	new_names = [re.sub(" gerundete ", " rounded ", i) for i in new_names]
	new_names = [re.sub(" gerundet ", " rounded ", i) for i in new_names]
	new_names = [re.sub(" gerundere ", " rounded ", i) for i in new_names]
	new_names = [re.sub(" gesaeumter ", " bordered ", i) for i in new_names]
	new_names = [re.sub(" gesaeumtes ", " bordered ", i) for i in new_names]
	new_names = [re.sub(" gesaeumte ", " bordered ", i) for i in new_names]
	new_names = [re.sub(" gesaeumt ", " bordered ", i) for i in new_names]
	new_names = [re.sub(" gezaehntes ", " toothed ", i) for i in new_names]
	new_names = [re.sub(" gezaehnter ", " toothed ", i) for i in new_names]
	new_names = [re.sub(" gezaehnte ", " toothed ", i) for i in new_names]
	new_names = [re.sub(" gezaehnt ", " toothed ", i) for i in new_names]
	new_names = [re.sub(" Habitus ", " stature ", i) for i in new_names]
	new_names = [re.sub(" Habitus", " stature", i) for i in new_names]
	new_names = [re.sub(" herablaufendes ", " winged ", i) for i in new_names]
	new_names = [re.sub(" herablaufender ", " winged ", i) for i in new_names]
	new_names = [re.sub(" herablaufende ", " winged ", i) for i in new_names]
	new_names = [re.sub(" herablaufend ", " winged ", i) for i in new_names]
	new_names = [re.sub(" Herbarbeleg ", " voucher specimen ", i) for i in new_names]
	new_names = [re.sub(" Herbarbeleg", " voucher specimen", i) for i in new_names]
	new_names = [re.sub(" Innenseite ", " interior side ", i) for i in new_names]
	new_names = [re.sub("(Innenseite)", "interior side", i) for i in new_names]
	new_names = [re.sub(" Kapsel ", " capsule ", i) for i in new_names]
	new_names = [re.sub(" kollenchymatisch verdickt ", " collenchym ", i) for i in new_names]
	new_names = [re.sub(" maennliches ", " male ", i) for i in new_names]
	new_names = [re.sub(" maennlichen ", " male ", i) for i in new_names]
	new_names = [re.sub(" maennliche ", " male ", i) for i in new_names]
	new_names = [re.sub(" maennlich ", " male ", i) for i in new_names]
	new_names = [re.sub(" Mittelrippe ", " vitta ", i) for i in new_names]
	new_names = [re.sub(" mittleres ", " middle ", i) for i in new_names]
	new_names = [re.sub(" mittlerer ", " middle ", i) for i in new_names]
	new_names = [re.sub(" mittlere ", " middle ", i) for i in new_names]
	new_names = [re.sub(" mittler ", " middle ", i) for i in new_names]
	new_names = [re.sub(" mit ", " with ", i) for i in new_names]
	new_names = [re.sub(" oberes ", " upper ", i) for i in new_names]
	new_names = [re.sub(" oberer ", " upper ", i) for i in new_names]
	new_names = [re.sub(" obere ", " upper ", i) for i in new_names]
	new_names = [re.sub(" Ober- ", " antical ", i) for i in new_names]
	new_names = [re.sub(" Oberlappen ", " antical lobe ", i) for i in new_names]
	new_names = [re.sub(" Oberseite ", " ventral side ", i) for i in new_names]
	new_names = [re.sub(" Papillen ", " papillae ", i) for i in new_names]
	new_names = [re.sub(" Papille ", " papille ", i) for i in new_names]
	new_names = [re.sub(" Paraphysen ", " paraphyses ", i) for i in new_names]
	new_names = [re.sub(" Perianthmuendung ", " perianth mouth ", i) for i in new_names]
	new_names = [re.sub(" Perianthien ", " perianths ", i) for i in new_names]
	new_names = [re.sub(" Perianth ", " perianth ", i) for i in new_names]
	new_names = [re.sub(" Perichaetialblatt ", " perichaetial leaf ", i) for i in new_names]
	new_names = [re.sub(" Pflanzenspitze ", " plant apex ", i) for i in new_names]
	new_names = [re.sub(" Pflanzen ", " plants ", i) for i in new_names]
	new_names = [re.sub(" Pflanze ", " plant ", i) for i in new_names]
	new_names = [re.sub(" Querschnitt ", " cross section ", i) for i in new_names]
	new_names = [re.sub(" Rand ", " margin ", i) for i in new_names]
	new_names = [re.sub(" Rippe ", " vitta ", i) for i in new_names]
	new_names = [re.sub(" Saum ", " bordered margin ", i) for i in new_names]
	new_names = [re.sub(" Seitenansicht ", " lateral side ", i) for i in new_names]
	new_names = [re.sub(" Spitze ", " apex ", i) for i in new_names]
	new_names = [re.sub(" Sporogonen ", " sporphytes ", i) for i in new_names]
	new_names = [re.sub(" Sporogon ", " sporophyte ", i) for i in new_names]
	new_names = [re.sub(" Sporophyt ", " sporophyte ", i) for i in new_names]
	new_names = [re.sub(" Sporenkapseln ", " spore capsules ", i) for i in new_names]
	new_names = [re.sub(" Sporenkapsel ", " spore capsule ", i) for i in new_names]
	new_names = [re.sub(" Sporen ", " spores ", i) for i in new_names]
	new_names = [re.sub(" Spore ", " spore ", i) for i in new_names]
	new_names = [re.sub(" Staemmchen ", " stem ", i) for i in new_names]
	new_names = [re.sub(" Thallus ", " thallus ", i) for i in new_names]
	new_names = [re.sub(" Thallusende ", " thallus apex ", i) for i in new_names]
	new_names = [re.sub(" und ", " and ", i) for i in new_names]
	new_names = [re.sub(" unreifes ", " immature ", i) for i in new_names]
	new_names = [re.sub(" unreifer ", " immature ", i) for i in new_names]
	new_names = [re.sub(" unreifen ", " immature ", i) for i in new_names]
	new_names = [re.sub(" unreife ", " immature ", i) for i in new_names]
	new_names = [re.sub(" unreif ", " immature ", i) for i in new_names]
	new_names = [re.sub(" Unterblatt ", " underleaf ", i) for i in new_names]
	new_names = [re.sub(" unteres ", " lower ", i) for i in new_names]
	new_names = [re.sub(" unterer ", " lower ", i) for i in new_names]
	new_names = [re.sub(" untere ", " lower ", i) for i in new_names]
	new_names = [re.sub(" Unterlappen ", " postical lobe ", i) for i in new_names]
	new_names = [re.sub(" Unterseite ", " dorsal side ", i) for i in new_names]
	new_names = [re.sub(" weibliches ", " female ", i) for i in new_names]
	new_names = [re.sub(" weiblichen ", " female ", i) for i in new_names]
	new_names = [re.sub(" weibliche ", " female ", i) for i in new_names]
	new_names = [re.sub(" weiblich ", " female ", i) for i in new_names]
	new_names = [re.sub(" Zaehne ", " teeth ", i) for i in new_names]
	new_names = [re.sub(" Zahn ", " tooth ", i) for i in new_names]
	new_names = [re.sub(" Zellen ", " cells ", i) for i in new_names]
	
	# Fix spelling errors
	new_names = [re.sub(" Scapania nemoroea ", " Scapania nemorea ", i) for i in new_names]
	
	# Show renaming action
	if (__DRY_RUN__):
		print("The following renaming in batches will be done:")
		base_names = [re.sub("(IMG_\d\d\d\d |IMG_\d\d\d\d-\d\d\d\d |\.CR(2|3)|\.TIF|\.JPG|\.xmp)", "", i) for i in new_names]
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
					if (os.path.isfile(old_names[j])) or (os.path.isdir(old_names[j])):
						print('mv' + ' ' + '\"' + old_names[j] + '\"' + ' ' + '\"' + new_names[j] + '\"')
			if (__DRY_RUN__ == False):
				for j in range(0, len(old_names)):
					if (os.path.isfile(old_names[j])) or (os.path.isdir(old_names[j])):
						os.rename(old_names[j], new_names[j])
	
	if (__DEBUG__ == True): print("Renaming of " + str(len(new_names)) + " files done.")



# -------------------- MAIN --------------------
if (__RECURSIVE__ == False):
	# Rename files
	dest_files = sorted( filter(lambda p: p.suffix in {".CR2", ".CR3", ".DNG", ".TIF", ".tiff", ".JPG", ".xmp", ".XMP"}, Path(dest_dir).glob("*")) )
	rename_files(dest_files)
else:
	# Rename directories first
	dest_dirs = sorted( glob.glob(f'{dest_dir}/*/**/', recursive=True) )
	rename_files(dest_dirs)
	
	# Rename files afterwards in all subdirectories
	dest_files = sorted( filter(lambda p: p.suffix in {".CR2", ".CR3", ".DNG", ".TIF", ".tiff", ".JPG", ".xmp", ".XMP"}, Path(dest_dir).rglob("*")) )
	rename_files(dest_files)


