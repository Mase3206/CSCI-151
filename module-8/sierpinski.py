#!/usr/bin/env python3

# =============================================================================
# sierpinski.py
#
# Recursively draws Sierpinski triangles.
#
# Noah S. Roberts
# 03.27.2024
# Assignment 10
# for Module 8
# Book Excercise 2.3.27
# =============================================================================


import stddraw, stdio, math, stdarray


globalRootWidth = 0
globalRootOrigin = stdarray.create1D(2, 0)



class Triangle:
	"""
	Perfect triangle object.

	Arguments
	---------
		p1: tuple x and y coordinates of left-most point
		base: int base width
		height: int height
	"""
	def __init__(self, p1: tuple[int, int], base: int):
		self.base = base
		self.height = math.sqrt(base ** 2 - (base / 2) ** 2)

		# left-most point
		self.p1 = p1

		# right-most point
		self.p2 = stdarray.create1D(2, 0)
		self.p2 = (p1[0] + base, p1[1])

		# top point
		self.p3 = stdarray.create1D(2, 0)
		self.p3 = (p1[0] + (base / 2), p1[1] + self.height)

	
	def draw(self):
		"""
		Draws a perfect triangle using the booksite `stddraw` library. 
		"""
		stddraw.line(self.p1[0], self.p1[1], self.p2[0], self.p2[1])
		# stddraw.show(1)
		stddraw.line(self.p2[0], self.p2[1], self.p3[0], self.p3[1])
		# stddraw.show(1)
		stddraw.line(self.p3[0], self.p3[1], self.p1[0], self.p1[1])
		# stddraw.show(1)




def drawSierp(width: float|int, basePoint: tuple[int, int]) -> None:
	"""
	Draws a trio of triangles within a base triangle via recursion.

	Arguments
	---------
		level: int representing how far into the Sierpinski triangle you have recursed
	
	Globals Used
	------------
		globalRootWidth: int set in main(); width of the root (initial, largest) triangle
		globalRootOrigin: int set in main(); leftmost point of the root triangle
	"""
	
	if width == globalRootWidth:
		return
	
	else:
		t1 = Triangle(basePoint, width)

		# the base points of triangles 2 and 3 are points 2 and 3 on triangle 1, respectively
		t2 = Triangle(t1.p2, width)
		t3 = Triangle(t1.p3, width)

		t1.draw()
		t2.draw()
		t3.draw()

		drawSierp(width / 2, t1.p1)
		drawSierp(width / 2, t2.p1)
		drawSierp(width / 2, t3.p1)



def main(levels: int):
	"""
	Takes `levels` levels of Sierpinski triangles and draws `3 ^ (levels - 1)` of them in the correct pattern
	"""

	levels += 1

	global globalRootWidth, globalRootOrigin

	xMin = 0
	xMax = 2
	yMin = xMin
	yMax = xMax

	# set the root width and origins of the root triangle globally
	globalRootWidth = abs(xMin) + abs(xMax) / (2 ** (levels))
	globalRootOrigin = (xMin, yMin)

	stdio.writef('Setting window X scale from %d to %d\n', xMin, xMax)
	stddraw.setXscale(xMin, xMax)

	stdio.writef('Setting window Y scale from %d to %d\n', yMin, yMax)
	stddraw.setYscale(yMin, yMax)


	if levels < 1:
		raise ValueError('Number of levels must be positive.')
	
	# elif levels == 1:
	# 	# root triangle
	# 	rootTriangle = Triangle(globalRootOrigin, globalRootWidth)
	# 	rootTriangle.draw()
	
	else:
		# root triangle
		rootTriangle = Triangle(globalRootOrigin, globalRootWidth * (2 ** (levels)))
		rootTriangle.draw()

		width = globalRootWidth * (2 ** (levels - 1))
		drawSierp(width, rootTriangle.p1)


	stddraw.show()



if __name__ == '__main__':
	import sys
	stdio.writeln()
	main(int(sys.argv[1]))
