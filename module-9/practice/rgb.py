#!/usr/bin/env python3

import random
import sys

import stddraw
import stdio
from color import Color

def whoa(r, show=False):
	for i in range(r):
		# take red, green, and blue values from the CLI
		r = random.randrange(0, 255)
		g = random.randrange(0, 255)
		b = random.randrange(0, 255)

		# create booksite `Color` object
		c1 = Color(r, g, b)
		stdio.writeln(c1)

		# set the canvas dimensions
		stddraw.setXscale(0, 4)
		stddraw.setYscale(0, 4)

		# draw dat shit
		stddraw.setPenColor(c1)
		stddraw.setPenRadius(.1)
		stddraw.filledRectangle(random.randrange(-40, 40) / 10, random.randrange(-40, 40) / 10, random.randrange(1, 40) / 10, random.randrange(1, 40) / 10)

		# show your beautiful creation
		if show:
			stddraw.show(1)


# whoa(int(sys.argv[1]), show=True)

for j in range(int(sys.argv[1])):
	whoa(50)
	stddraw.show(.1)
	stddraw.clear()
