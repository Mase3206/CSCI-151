#!/usr/bin/env python3

import stdio, stdarray, sys


values = stdarray.create1D(0)
while not stdio.isEmpty():
	values += [stdio.readInt()]

try:
	stdio.writeln('Minimum: ' + str(min(values)))
	stdio.writeln('Maximum: ' + str(max(values)))
except ValueError:
	sys.exit()
