#!/usr/bin/env python

# Load modules
import errno
import sys
import os
import argparse
import glob
from pathlib import Path
import re
import csv



# -------------------- Arguments --------------------
# Parse arguments
parser = argparse.ArgumentParser(description='Extract meta-data from XMP stack and write into a single TSV file.')
parser.add_argument('-v', '--version', action='version', version='XMP stack to TSV Version 0.2',
                   help='show version')
parser.add_argument('-x', '--xmp_dir', metavar='dir', dest='xmp_dir', required=True,
                   help='directory containing the xmp files')
parser.add_argument('-t', '--tsv', metavar='tsv_file', dest='tsv_file', required=True,
                   help='destination tsv file')

args = parser.parse_args()

# Directory containing XMP files
xmp_dir = args.xmp_dir

xmp_files = sorted( [f for f in glob.glob(''.join([xmp_dir, '/', '*.[xX][mM][pP]']))] )

# Destination tsv file
tsv_file = args.tsv_file



# -------------------- MAIN --------------------
import xml.etree.ElementTree as ET
import pandas
pandas.set_option('mode.chained_assignment', None)

# Create empty dataframe
xmp_df = pandas.DataFrame([1])

# Iterate through all xmp files
for xmp_file in xmp_files:
	# Read XMP file
	xmp_data = ET.parse(xmp_file)
	
	# Get tree 
	xmp_tree = xmp_data.getroot()
	
	# Get dictionary from tree
	xmp_dict = xmp_tree[0][0].attrib
	
	# Create new column in TSV if it does not exists yet
	for tag, val in xmp_dict.items():
		if (tag not in xmp_df.columns.tolist()):
			xmp_df = xmp_df.assign(new="")
			xmp_df.columns = [*xmp_df.columns[:-1], str(tag)]
	
	# Add new row
	xmp_df = xmp_df.append(pandas.Series("", index=xmp_df.columns), ignore_index=True)
	
	# Add values
	for tag, val in xmp_dict.items():
		xmp_df.loc[len(xmp_df)-1, str(tag)] = val

# Save dataframe to TSV
xmp_df.to_csv(tsv_file, header=True, index=False, sep='\t', na_rep='')
