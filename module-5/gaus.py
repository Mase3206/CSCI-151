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


# built-ins
import math
import random

# booksite modules
import stdarray
import stddraw
import stdio
import stdstats


def gaussian() -> float:
	"""
	Generate a random number following the Gaussian (normal, bell) distribution

	Returns
	-------
		Gaussian random float
	"""
	
	# initialize r
	r = 0.0

	# loop until r = (-∞,0)U(0,1)
	while (r >= 1.0) or (r == 0.0):
		x = random.uniform(-1.0, 1.0)
		y = random.uniform(-1.0, 1.0)
		r = x*x + y*y

	# do some magic on r before returning it
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
	Trim the data to be between a pre-defined minimum and maximum

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
			# if data[i] is between the low and high values, increment count[i]
			if low <= data[j] <= high:
				counts[i] += 1

	return counts


def printStats(data:list[float]) -> None:
	"""
	Prints some basic statistics

	Parameter
	---------
		`data`: list of floats to do statistics on
	"""
	stdio.writef('\nµ    = %7.4f\n', stdstats.mean(data))
	stdio.writef('med  = %7.4f\n', stdstats.median(data))
	stdio.writef('%s    = %7.4f\n', chr(0x03c3), stdstats.stddev(data))
	stdio.writef('%s%s   = %7.4f\n\n', chr(0x03c3), chr(0x00B2), stdstats.var(data))
	# 0x03c3 is lowercase sigma, 0x00B2 is superscript 2


def plotData(data:list[float]) -> None:
	"""
	Plot filled rectangles using pygame-based booksite `stddraw`

	Parameter
	---------
		`data`: list of floats to plot on a histogram-style graph
	"""
	stdio.writeln('Plotting data...')

	# set x scale to just above and below range
	stddraw.setXscale(-0.6, 19.5)

	# set y scale max to just above most frequent point
	stddraw.setYscale(0, max(data) * 1.05)

	# misc parameters
	stddraw.setPenRadius(0.01)
	stddraw.setPenColor(stddraw.BLACK)

	# draw dem rectangles
	for i in range(20):
		stddraw.filledRectangle(i - 0.5, 0, 0.9, data[i])

	stddraw.show()


def main(nPoints:int):
	# get the points
	data = collectData(nPoints)

	# only include a specific range of points 
	dataInRange = trimData(data)

	# print some basic stats
	printStats(data)

	# show the data in a pretty graphic!
	plotData(dataInRange)


if __name__ == '__main__':
	# sys is only needed in the test client, so only import it here
	import sys

	# take the command line argument here to allow for portability
	main(int(sys.argv[1]))


# =============================================================================
# EXAMPLE USAGE
# -----------------------------------------------------------------------------
#
# $ python gaus.py 1000000
# 	(pygame hello)
# 
# 	µ    = -0.0006
# 	med  = -0.0013
# 	σ    =  1.0008
# 	σ²   =  1.0017
# 
# 	Plotting data...
#	(display graphic)
#
# 
# $ python gaus.py 1000
# 	(pygame hello)
# 
# 	µ    = -0.0169
# 	med  = -0.0385
# 	σ    =  1.0194
# 	σ²   =  1.0391
# 
# 	Plotting data...
# 	(display graphic)
#
#
# =============================================================================
