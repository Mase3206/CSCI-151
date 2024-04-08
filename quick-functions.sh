
function same-out-py() {
	# Runs the two given Python 3 scripts and compares their output.
	# Usage: same-out-py script1 script2 [args...]

	out1=$(python $1 ${@:3})
	if [[ $? -ne 0 ]] || ; then
		echo "Failed to store output of first script."
		return 1
	fi

	out2=$(python $2 ${@:3})
	if [[ $? -ne 0 ]]; then
		echo "Failed to store output of second script."
		return 1
	fi

	echo "$1: $out1"
	echo "$2: $out2"

	if [[ $out1 == $out2 ]]; then
		echo "equal"
	else
		echo "not equal"
	fi
}