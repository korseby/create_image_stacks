#!/usr/bin/env python3.7

# Load modules
import errno
import sys
import os
import argparse
import glob
from pathlib import Path
import re

# Parse arguments
parser = argparse.ArgumentParser(description='Create script to build image stacks based on a list of XMP files containing color badges.')
parser.add_argument('-v', '--version', action='version', version='Create Image Stacks Version 0.3',
                   help='show version')
parser.add_argument('-V', '--verbose', dest='verbose', action='store_true', required=False,
                   help='be verbose and show what is being done')
parser.add_argument('-n', '--dry-run', dest='dryrun', action='store_true', required=False,
                   help='do not do anything, just show what is being done')
parser.add_argument('-c', '--create_dirs_only', dest='dirs_only', action='store_true', required=False,
                   help='only create output directories and do not move destination images')
parser.add_argument('-x', '--xmp_dir', metavar='dir', dest='xmp_dir', required=True,
                   help='directory containing the xmp files')
parser.add_argument('-d', '--img_dir', metavar='dir', dest='img_dir', required=True,
                   help='destination image directory')
parser.add_argument('-f', '--force', dest='force', action='store_true', required=False,
                   help='force action and do not exit when image file(s) do not exist')

args = parser.parse_args()

# Verbosity
__DEBUG__ = args.verbose

# Dry-run
__DRY_RUN__ = args.dryrun

# Dirs only
__DIRS_ONLY__ = args.dirs_only

# Force
__FORCE__ = args.force

# Directory containing XMP files
xmp_dir = args.xmp_dir

xmp_files = sorted( [f for f in glob.glob(''.join([xmp_dir, '/', '*.[xX][mM][pP]']))] )

# Grab xmp labels
xmp_labels = []
for xmp_filename in xmp_files:
	xmp_file = open(xmp_filename, "r")
	xmp_label = False
	for line in xmp_file:
		if re.search("xmp\:Label\=", line):
			line = line.lower().rstrip('\r\n')
			line = re.sub(".*xmp\:label\=", "", line)
			line = re.sub("\"", "", line)
			xmp_labels.append(line)
			xmp_label = True
	if (xmp_label == False): xmp_labels.append('')
	xmp_file.close()

# Check whether number of labels matches number of xmp files
if (len(xmp_labels) != len(xmp_files)):
	print("Error! Number of xmp labels does not match number of xmp files.")
	exit(2)

# Destination image directory
img_dir = args.img_dir

img_files = sorted( [f for f in glob.glob(''.join([img_dir, '/', '*.[tTjJ][iIpP][fFgG]']))] )

# Check whether number of input and output files match
if (len(xmp_files) != len(img_files)):
	if (__FORCE__ == True):
		extension = os.path.splitext(img_files[0])[1]
		img_files = [Path(i).stem for i in xmp_files]
		img_files = [''.join([img_dir, '/', f, extension]) for f in img_files]
	else:
		print("Error! Number of xmp files does not match number of image files.")
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
	if (i > 1) and ( (i >= len(xmp_labels)) or (label != stack_label) or (label == "")):
		if (i >= len(xmp_labels)):
			stack_end = i
		else:
			stack_end = i-1
		stack_label = label
		
		# Singular file
		if (stack_start == stack_end):
			if (__DEBUG__ == True): print('# Singular file: ' + 'IMG_' + img_nums[stack_start-1] + ' ' + img_names[stack_start-1])
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
				if (os.path.isfile(img_files[stack_start-1])): print('mkdir' + ' ' + '\"' + dir_name + '\"')
			if (__DRY_RUN__ == False):
				if (os.path.isfile(img_files[stack_start-1])): os.makedirs(dir_name, exist_ok=True)
			
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

if (__DEBUG__ == True): print("# Done.")
