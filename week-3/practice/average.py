#!/usr/bin/env python3

import stdio


total = 0.0
count = 0

while not stdio.isEmpty():
	value = stdio.readFloat()
	total += value
	count += 1

avg = total / count
stdio.writeln("Average is " + str(avg))
