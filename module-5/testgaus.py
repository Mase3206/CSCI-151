#!/usr/bin/env python3

import sys

import stddraw
import stdrandom


trials = int(sys.argv[1])
stddraw.setPenRadius(0.0)

for i in range(trials):
	x = stdrandom.gaussian(0.5, 0.2)
	y = stdrandom.gaussian(0.5, 0.2)
	stddraw.point(x, y)

stddraw.show()
