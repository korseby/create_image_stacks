#!/usr/bin/env bash

VERSION="0.9"

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
		if [[ ${DRY_RUN} == True ]]; then echo "Looking for IMG_* files in \"${i}\"..."; fi
		
		# Supported methods
		case $(echo ${i} | perl -pe 's/.*\///') in
			z21)	METHOD="2-1";;
			z42)	METHOD="4-2";;
			z84)	METHOD="8-4";;
			z88)	METHOD="8-8";;
			z168)	METHOD="16-8";;
			z2416)	METHOD="24-16";;
			z248)	METHOD="24-8";;
			z3220)	METHOD="32-20";;
			z328)	METHOD="32-8";;
			z408)	METHOD="40-8";;
			z508)	METHOD="50-8";;
			zc)		METHOD="C";;
			zd)		METHOD="DMap";;
			za)		METHOD="A";;
			zp)		METHOD="P";;
			z42zc)	METHOD="4-2_C";;
			z84zc)	METHOD="8-4_C";;
			z168zc)	METHOD="16-8_C";;
			z2416c)	METHOD="24-16_C";;
			zdzc)	METHOD="DMap_C";;
			zdzp)	METHOD="DMap_P";;
			*)		echo "Error! Unknown method \"${i}\""; exit 10;;
		esac
		
		# Names of stacked images to be renamed
		NEW_NAMES=$(find -s ${i} -iname "*[TIF]")
		NEW_NAMES=(${NEW_NAMES})
		
		# Check for same number of images
		if [[ ${#NAMES[@]} -ne ${#NEW_NAMES[@]} ]]; then
			echo "Error! Number of images (${#NAMES[@]}) does not match number of stacked images (${#NEW_NAMES[@]}) to be renamed in ${METHOD}."
			exit 11
		fi
		
		# Get file type
		FILE_TYPE="$(echo ${NEW_NAMES[${1}]^^} | perl -pe 's/.*\.//')"
		
		for ((c=0;c<${#NEW_NAMES[@]};c++)); do
			if [[ ${DRY_RUN} == True ]]; then echo "mv \"${NEW_NAMES[${c}]}\" \"${i}/${NAMES[${c}]} (${METHOD}).${FILE_TYPE}\"..."; fi
			if [[ ${DRY_RUN} == False ]]; then mv "${NEW_NAMES[${c}]}" "${i}/${NAMES[${c}]} (${METHOD}).${FILE_TYPE}"; fi
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


