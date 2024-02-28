#!/usr/bin/env python3

# =============================================================================
# gaus.py
#
# your radical description goes here
#
# Noah S. Roberts
# 02.28.2024
# Assignment 8
# for Module 5
# Book Excercise 2.1.25
# =============================================================================


import stdio, stddraw, stdarray, random, math, stdstats, sys


def gaussian() -> float:
	r = 0.0
	while (r >= 1.0) or (r == 0.0):
		x = random.uniform(-1.0, 1.0)
		y = random.uniform(-1.0, 1.0)
		r = x*x + y*y
	return x * math.sqrt(-2.0 * math.log(r) / r)


def collectData(qty:int) -> list[float]:
	"""
	Call and store `gaussian()` `qty` times and return the list of stored floats

	Parameter
	---------
		`qty`: int quantity of gaussian random values

	Returns
	-------
		list of floats
	"""
	data = stdarray.create1D(qty, 0)

	for i in range(qty):
		data[i] = gaussian()

	return data


def trimData(data:list[float]) -> list:
	"""
	Trim the data to be between a defined minimum and maximum

	Parameter
	---------
		`data`: list of floats
	
	Return
	------
		list of floats within defined range
	"""

	counts = stdarray.create1D(20, 0)

	for i in range(20):
		# arbitrary bin-width set by assignment
		low = i * 0.05
		high = (i + 1) * 0.05

		for j in range(len(data)):
			if low <= data[j] <= high:
				counts[i] += 1

	return counts


def printStats(data:list[float]) -> None:
	stdio.writeln()  # put a space after the pygame welcome
	stdio.writef('µ    = %7.4f\n', stdstats.mean(data))
	stdio.writef('med  = %7.4f\n', stdstats.median(data))
	stdio.writef('%s    = %7.4f\n', chr(0x03c3), stdstats.stddev(data))
	stdio.writef('%s%s   = %7.4f\n', chr(0x03c3), chr(0x00B2), stdstats.var(data))
	# 0x03c3 is lowercase sigma, 0x00B2 is superscript 2

	return


def plotData(data:list[float]) -> None:
	# set x scale to just above and below range
	stddraw.setXscale(-1, 20)

	# set y scale max to just above most frequent point
	stddraw.setYscale(0, max(data) * 1.05)

	# misc parameters
	stddraw.setPenRadius(0.01)
	stddraw.setPenColor(stddraw.BLACK)

	for i in range(20):
		stddraw.filledRectangle(i - 0.5, 0, 0.9, data[i])

	stddraw.show()


def main(nPoints:int):
	data = collectData(nPoints)
	dataInRange = trimData(data)
	printStats(data)
	plotData(dataInRange)


if __name__ == '__main__':
	main(int(sys.argv[1]))


# =============================================================================
# EXAMPLE USAGE
# -----------------------------------------------------------------------------
#
# $ python gaus.py urmom
#	ha lol
#
# $ python gaus.py urmom2
#	ha lol 2
#
#
# -----------------------------------------------------------------------------
# EXTRA NOTES
# -----------------------------------------------------------------------------
#
# 1. urmom3
#
# =============================================================================

