#!/usr/bin/env bash

VERSION="0.2"

IFS=$'\n'



# Help function
function help() {
	echo "${0} renames stacked images in a stack of stacked images."
	echo "A stack of stacked images is a directory beginning with a z."
	echo ""
	echo "Usage: ${0} [-n] [dir]"
	echo ""
	echo "The parameter -n is optional and means dry-run."
	echo "The directory is mandatory. Or just use . as the current directory."
	echo ""
	echo "send bug-reports to <kristian@korseby.net>"
}



# Process function
function process() {
	echo "Renaming in directory \"${DIR}\"..."
	
	# Name of stacks of stacked images
	STACKS=$(find ${DIR} -name "z*" -maxdepth 1 -type d)
	
	# Names of stacked images
	NAMES=$(find -s ${DIR} -name "*IMG_*" -maxdepth 1 -type d | perl -pe 's/.*\///')
	NAMES=(${NAMES})
	
	# Process
	for i in ${STACKS}; do
		if [[ ${DRY_RUN} == True ]]; then echo "Looking for *.JPG files in \"${i}\"..."; fi
		
		# Supported methods
		case $(echo ${i} | perl -pe 's/.*\///') in
			z42)	METHOD="4-2";;
			z84)	METHOD="8-4";;
			z168)	METHOD="16-8";;
			z2416)	METHOD="24-16";;
			z3220)	METHOD="32-20";;
			zc)		METHOD="C";;
			zd)		METHOD="DMap";;
			za)		METHOD="A";;
			zp)		METHOD="P";;
			*)		echo "Error! Unknown method \"${i}\""; exit 10;;
		esac
		
		# Names of stacked images to be renamed
		NEW_NAMES=$(find -s ${i} -iname "*.JPG")
		NEW_NAMES=(${NEW_NAMES})
		
		# Check for same number of images
		if [[ ${#NAMES[@]} -ne ${#NEW_NAMES[@]} ]]; then
			echo "Error! Number of images (${#NAMES[@]}) does not match number of stacked images (${#NEW_NAMES[@]}) to be renamed."
			exit 11
		fi
		
		for ((c=0;c<${#NEW_NAMES[@]};c++)); do
			if [[ ${DRY_RUN} == True ]]; then echo "mv \"${NEW_NAMES[${c}]}\" \"${i}/${NAMES[${c}]} (${METHOD}).JPG\"..."; fi
			if [[ ${DRY_RUN} == False ]]; then mv "${NEW_NAMES[${c}]}" "${i}/${NAMES[${c}]} (${METHOD}).JPG"; fi
		done
	done
}



# Check
if [[ ${#} -eq 0 ]] || [[ ${#} -gt 2 ]] || [[ ${1} == "-h" ]] || [[ ${1} == "--help" ]] || [[ ${2} == "-h" ]] || [[ ${2} == "--help" ]]; then
	help
fi

# Parameter dry-run
if [[ ${1} == "-n" ]] || [[ ${2} == "-n" ]] || [[ ${1} == "--dry-run" ]] || [[ ${2} == "--dry-run" ]]; then
	DRY_RUN=True
	echo "Enabled dry-run."
else
	DRY_RUN=False
fi

# Check for parameters
if [[ ${#} -eq 1 ]] && [[ ${1:0:1} == "-" ]]; then
	help
elif [[ ${#} -eq 2 ]] && [[ ${1:0:1} == "-" ]] && [[ ${2:0:1} == "-" ]]; then
	help
else
	if [[ ${#} -eq 2 ]] && [[ ${1:0:1} == "-" ]]; then
		DIR=${2}
	elif [[ ${#} -eq 2 ]] && [[ ${2:0:1} == "-" ]]; then
		DIR=${1}
	else
		DIR=${1}
	fi
	
	process
fi


