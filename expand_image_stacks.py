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
parser = argparse.ArgumentParser(description='Expand full list of images from an image stack.')
parser.add_argument('-v', '--version', action='version', version='Expand image stacks Version 0.2',
                   help='show version')
parser.add_argument('-d', '--dir', metavar='dest_dir', dest='dest_dir', required=False,
                   help='destination directory of image files')
parser.add_argument('-s', '--stdin', dest='stdin', action='store_true', required=False,
                   help='read list of images from stdin')

args = parser.parse_args()

# Standard input
__STDIN__ = args.stdin

# Destination image directory
dest_dir = args.dest_dir



# -------------------- MAIN --------------------
if (__STDIN__ == False) and (type(dest_dir) != None):
	print("Error! Need to read list of images either from stdin or from directory.")
	exit(1)

# Read from stdin
if (__STDIN__ == True):
	image_stack = sorted(sys.stdin.readlines())
	image_stack = [i.strip() for i in image_stack]
else:
	image_stack = sorted( [f for f in glob.glob(''.join([dest_dir, '/', '*.']))] )
	image_stack = [Path(i).stem for i in image_stack]

# Iterate through object
for i, label in enumerate(image_stack, start=1):
	# Expand stack
	if (len(label) > 13):
		if (label[8] == "-"):
			start = int(label[4:8])
			end = int(label[9:13])
			name = label[13:]
			print(start)
			print(end)
			for j in range(start, end+1):
				#print("IMG_" + str(j).zfill(4) + name)
				print(label)
		else:
			print(label)


