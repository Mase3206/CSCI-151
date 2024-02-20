#!/usr/bin/env python3

# =============================================================================
# circle.py
#
# description
#
# Noah S. Roberts
# 02/19/2024
# Assignment 7
# for Module 4
# Book Excercise 1.5.19
# =============================================================================


import math
import random
import sys

import stdarray
import stddraw


class RangeError(ValueError):
	pass


def calculateCoordinates(point:int, totalPoints:int):
	# calculate the quadrant the point-to-be should be drawn in
	progress = (point) / (totalPoints)
	angle = progress * 2 * math.pi	# radians

	# gotta do this to be booksite-compliant (even though it's *very* not Python-like)
	coords = stdarray.create1D(2, 0)
	coords = [math.cos(angle), math.sin(angle)]
	return coords


def drawPoints(totalPoints:int) -> list[list[float]]:
	points = stdarray.create1D(totalPoints)

	# collect the points to be drawn
	for point in range(totalPoints):
		# add the calculated coordinates to the `points` list
		points[point] = calculateCoordinates(point, totalPoints)
		# draw the newly-calculated point
		stddraw.point(points[point][0], points[point][1])

	# return the coordinates for later use
	return points


def drawLines(points:list[tuple[float, float]], totalPoints:int, probability:float):
	# how many lines will be drawn
	lineQty = int(totalPoints ** 2 * probability)

	for i in range(lineQty):
		# grab random points to draw the line between
		point1 = random.randint(0, totalPoints - 1)
		point2 = random.randint(0, totalPoints - 1)

		# this eyesore pulls draws the correct coordinate from each randomly-
		# selected point and draws a line between them
		stddraw.line(points[point1][0], points[point1][1], points[point2][0], points[point2][1])



def main(totalPoints:int, probability:float, frametime=math.inf):
	# gotta draw the line somewhere (makes any errors less cryptic)
	if totalPoints < 1:
		raise RangeError(f'Point quantity must be a positive integer. Given: {totalPoints}; ')

	if not 0.0 <= probability <= 1.0:
		raise RangeError(f'Probability must be a float between 0.0 and 1.0. Given: {probability}')

	# initialize the window
	stddraw.clear()
	stddraw.setXscale(-1.25, 1.25)
	stddraw.setYscale(-1.25, 1.25)

	# settings for points
	stddraw.setPenColor(stddraw.BLACK)
	stddraw.setPenRadius(0.01)
	# omg i love dots
	points = drawPoints(totalPoints)

	# setting for lines
	stddraw.setPenRadius(0.001)
	# draw dem lines
	drawLines(points, totalPoints, probability)

	# share your beautiful creation with the world
	stddraw.show(frametime)


# should probably make this modular
if __name__ == '__main__':
	totalPoints = int(sys.argv[1])
	probability = float(sys.argv[2])

	main(totalPoints, probability)