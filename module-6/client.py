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
	return


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

	


if __name__ == '__main__':
	import sys
	if (given := sys.argv[1]) == '-h':
		help()
	else:
		main(helpful.stdinList(given))

