#!/usr/bin/env python3

# =============================================================================
# temperline.py
#
# Nicely formats given numbers into columns of ten; for use with randomintseq.py
#
# Noah S. Roberts
# 02/09/2024
# Assignment 6
# for Week 4
# Book Excercise 1.5.10
# =============================================================================

import stdio, stdarray, sys

debug = False


class DebugObj:
	def __init__(self, value:str, JSON=False):
		self.value = value
		self.useJSON = JSON
	
	def show(self):
		try:
			null = int(value)
			isInt = True
			isEOF = False
		except ValueError:
			isInt = False

			if self.value.lower() == 'eof':
				isEOF = True
			else:
				isEOF = False
		
		if self.useJSON:
			stdio.writeln( {
				"value": self.value,
				"isInt": isInt,
				"isEOF": isEOF
			} )
		else:
			stdio.writeln('Given value:', self.value)
			stdio.writeln('Is integer:', isInt)
			stdio.writeln('Is EOF:', isEOF)
		stdio.writeln()


while True:
	numbers = stdarray.create1D(10)

	for i in range(0,10):
		value = stdio.readLine()
		if debug:
			stdinDebug = DebugObj(value)
			stdinDebug.show()
		
		try:
			valueInt = int(value)
			numbers[i] = valueInt

		except ValueError:
			if value.lower() == "eof":
				sys.exit(0)
			else:
				raise

	for i in range(10):
		stdio.writef("%5d", numbers[i])

	del numbers
	if debug:
		stdinDebug
	
	stdio.writeln()
