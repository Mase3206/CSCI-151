#!/usr/bin/env python3

# =============================================================================
# squares.py
#
# Recursively creates `n` number of concentric squares
#
# Noah S. Roberts
# 03.27.2024
# Assignment 
# for Module 8
# Book Excercise 
# =============================================================================


import stddraw


def drawSquare(sideLength: int) -> None:
	"""
	Takes the side 
	"""

	halfSideLength = sideLength / 2
	if halfSideLength > 0:
		stddraw.square(0, 0, halfSideLength)
		drawSquare(sideLength - 2)


def main(qty_squares: int) -> None:
	stddraw.setXscale(-qty_squares, qty_squares)
	stddraw.setYscale(-qty_squares, qty_squares)

	drawSquare(qty_squares * 2)
	stddraw.show()

	return


if __name__ == '__main__':
	import sys
	main(int(sys.argv[1]))


# =============================================================================
# EXAMPLE USAGE
# -----------------------------------------------------------------------------
# 
# $ python squares.py 5
#	[pygame output]
#
# $ python squares.py 8
#	[pygame output]
#
# =============================================================================
