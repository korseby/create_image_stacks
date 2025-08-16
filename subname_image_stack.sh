#!/usr/bin/env bash

VERSION="0.9"

IFS=$'\n'



# Help function
function help() {
	echo "${0} renames (sub)directories with stacked images based on the IMG_ numbers and descriptions."
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
	for i in ${DIR}/*/; do
		START="$(ls ${i} | sort | grep ^IMG_ | head -n 1 | perl -pe 's/IMG_//' | perl -pe 's/ .*//')"
		END="$(ls ${i} | sort | grep ^IMG_ | tail -n 1 | perl -pe 's/IMG_//' | perl -pe 's/ .*//')"
		DESCR="$(ls ${i} | sort | grep ^IMG_ | head -n 1 | perl -pe 's/IMG_\d\d\d\d //' | perl -pe 's/\..*//')"
		SUBNAME="IMG_${START}-${END} ${DESCR}"
		echo "Renaming \"${i}\" to \"${SUBNAME}\"."
		if [[ ${DRY_RUN} == False ]]; then
			mv "${i}" "${SUBNAME}"
		fi
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


