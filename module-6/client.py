#!/usr/bin/env python3

# =============================================================================
# client.py
#
# Simple client program to interface with my wacky module
#
# Noah S. Roberts
# 03.10.2024
# Assignment 9
# for Module 6
# Book Excercise ???
# =============================================================================


import helpful, stdio, stdarray


def help():
	stdio.writeln('Simple client program to interface with my wacky module\n\nARGUMENT:\n\tlist: string-enclosed list object containing ints and/or floats')


def main(arg: list[int|float]):
	"""
	Uses `helpful` to calculate and write the average and median values of the given list to stdout using booksite `stdio`.

	Argument
	--------
		arg: list of ints or float

	Returns
	-------
		None
	"""

	average = helpful.avg(arg)
	median = helpful.median(arg)

	stdio.writef('Avg: %.5f\n', average)
	stdio.writef('Med: %.5f\n', median)



if __name__ == '__main__':
	import sys
	if len(sys.argv) == 1:
		stdio.writeln('Missing required argument: list')
		exit(1)
	if (given := sys.argv[1]) == '-h':
		help()
	else:
		given_list = helpful.stdinList(given)
		main(given_list)

