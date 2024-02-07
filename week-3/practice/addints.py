#!/usr/bin/env python3

import stdio, sys


n = int(sys.argv[1])
total = 0

for i in range(n):
	total += stdio.readInt()
stdio.writeln('Sum is ' + str(total))
