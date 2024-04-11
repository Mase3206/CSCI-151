#!/usr/bin/env python3

# =============================================================================
# sportsfilter.py
#
# asdfadsf
#
# Noah S. Roberts
# 04.10.2024
# Assignment 11
# for Module 9
# Book Excercise ?????
# =============================================================================

import stdarray
from instream import InStream
from outstream import OutStream



def writeHeader() -> str:
	"""
	It writes the header. 
	
	In case you were wondering, this is a pretty common function I implement in my programs, as it can allow for a dynamic header via function arguments. I'm not taking any arguments with this one, so it's just force of habit
	"""
	return f"""
			Caitlin Clark Statistics - March Madness 2024

	{'Date':>10s} {'Opp':>20s} {'FG%':>8s} {'3P':>8s} {'3PA':>8s} {'3P%':>8s} {'AST':>8s} {'PTS':>8s}"""



def extractData(csvLine: str, delimter=',') -> str:
	"""
	Takes a CSV line and returns a string with the formatted data

	Arguments
	---------
		csvLine (str): one line from a CSV file
		delimiter (kwarg, str): the value delimiter used in the CSV file; defaults to a comma
	
	Returns
	-------
		the game data in a nice, formatted string
	"""
	a = csvLine.split(delimter)

	# throw the data into a dict to make returning the formatted string easier
	data = {
		'Date': str(a[0]),
		'Opp': str(a[2]),
		'FG%': float(a[7]),
		'3P': int(a[11]),
		'3PA': int(a[12]),
		'3P%': float(a[13]),
		'AST': int(a[20]),
		'PTS': int(a[25])
	}

	# return the data in a formatted string by unpacking the dict
	return "\t{Date:>10s} {Opp:>20s} {FG%:8.3f} {3P:8d} {3PA:8d} {3P%:8.3f} {AST:8d} {PTS:8d}".format(**data)



def main(filename: str):
	data = InStream(filename)
	lineList: list[str] = data.readAllLines()[1:]

	output = OutStream('offense.txt')
	output.writeln(writeHeader())
	for line in lineList:
		output.writeln(extractData(line))



if __name__ == '__main__':
	import sys
	main(sys.argv[1])