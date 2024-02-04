#!/usr/bin/env bash

VERSION="0.9"

IFS=$'\n'
DIR1="z84"
DIR2="zc"



# Help function
function help() {
	echo "${0} created directories for combining finished Helicon Focus 8-4 and Pyramid stacks."
	echo ""
	echo "Usage: ${0} [-n] [z84] [zc]"
	echo ""
	echo "The parameter -n is optional and means dry-run."
	echo "The two directories are mandatory. Per default, all individual files in z84 and zc are used consecutively."
	echo ""
	echo "send bug-reports to <kristian@korseby.net>"
}



# Process function
function process() {
	# Get files in DIR1
	if [[ ${DRY_RUN} == True ]]; then echo "Looking for IMG_ files in \"${DIR1}\"..."; fi
	FILES1=$(find -s ${DIR1} -name "*IMG_*" -maxdepth 1 | perl -pe 's/.*\///')
	FILES1=(${FILES1})
	
	# Get files in DIR2
	if [[ ${DRY_RUN} == True ]]; then echo "Looking for IMG_ files in \"${DIR2}\"..."; fi
	FILES2=$(find -s ${DIR2} -name "*IMG_*" -maxdepth 1 | perl -pe 's/.*\///')
	FILES2=(${FILES2})
	
	# Create working directory
	mkdir -p "${DIR1}${DIR2}"
	# Check for same number of images
	if [[ ${#FILES1[@]} -ne ${#FILES2[@]} ]]; then
		echo "Error! Number of images (${#FILES1[@]}) does not match number of stacked images (${#FILES2[@]}) to be renamed."
		exit 11
	fi
	
	# Create sub directories and copy files
	for ((c=0;c<${#FILES1[@]};c++)); do
		SUBDIR="${DIR1}${DIR2}/$(echo ${FILES1[${c}]} | perl -pe 's/\)\..*//')_$(echo ${FILES2[${c}]} | perl -pe 's/.*\(//' | perl -pe 's/\).*//'))"
		if [[ ${DRY_RUN} == False ]]; then mkdir -p $SUBDIR; fi
		if [[ ${DRY_RUN} == True ]]; then echo "cp \"${DIR1}/${FILES1[${c}]}\" \"${DIR2}/${FILES2[${c}]}\" \"${SUBDIR}/\"..."; fi
		if [[ ${DRY_RUN} == False ]]; then cp "${DIR1}/${FILES1[${c}]}" "${DIR2}/${FILES2[${c}]}" "${SUBDIR}/"; fi
	done
}



# Check
if [[ ${#} -gt 3 ]] || [[ ${1} == "-h" ]] || [[ ${1} == "--help" ]] || [[ ${2} == "-h" ]] || [[ ${2} == "--help" ]] || [[ ${3} == "-h" ]] || [[ ${3} == "--help" ]]; then
	help
	exit 0
fi

# Parameter dry-run
if [[ ${1} == "-n" ]] || [[ ${2} == "-n" ]] || [[ ${3} == "-n" ]] || [[ ${1} == "--dry-run" ]] || [[ ${2} == "--dry-run" ]] || [[ ${3} == "--dry-run" ]]; then
	DRY_RUN=True
	echo "Enabled dry-run."
else
	DRY_RUN=False
fi

# Check for parameters
if [[ ${#} -eq 0 ]]; then
	echo "Using default settings."
elif [[ ${#} -eq 1 ]] && [[ ${1} == "-n" ]]; then
	echo "Using default settings."
elif [[ ${#} -eq 2 ]] && [[ ${1:0:1} == "-" ]]; then
	DIR1=${2}
elif [[ ${#} -eq 2 ]] && [[ ${2:0:1} == "-" ]]; then
	DIR1=${1}
elif [[ ${#} -eq 3 ]] && [[ ${1:0:1} == "-" ]]; then
	DIR1=${2}
	DIR2=${3}
elif [[ ${#} -eq 3 ]] && [[ ${2:0:1} == "-" ]]; then
	DIR1=${1}
	DIR2=${3}
elif [[ ${#} -eq 3 ]] && [[ ${3:0:1} == "-" ]]; then
	DIR1=${1}
	DIR2=${2}
elif [[ ${#} -eq 1 ]]; then
	DIR1=${1}
elif [[ ${#} -eq 2 ]]; then
	DIR1=${1}
	DIR2=${2}
fi

echo "Using directories ${DIR1} and ${DIR2} for combining stacks."
process


