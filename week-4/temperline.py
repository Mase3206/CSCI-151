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

# =============================================================================
# EXAMPLE USAGE
# -----------------------------------------------------------------------------
#
# $ python randomintseq.py 100 100 |python temperline.py
#    48   69   63   63   52   68   99   47   27   89
#    28    5   25   11   93   83   98   23   58   78
#     4   84   16   52   82   64   21   56    2   13
#    99   18   22   69   59    6   33   26   43   79
#    35   78    0   83   82   17   98   50   61   83
#    50   44   16   89   54   14   72   69   49   55
#    39   50   69    9   36   87   38   92   14   65
#     8   94   88    7   73   90   18   11   50   14
#    76    0   36    0   84   71   12   54    8   38
#    28   98   23   66   17   17    5   12   94    0
#
# $ python randomintseq.py 100 10000 | python temperline.py
#  7332 7795 5171 3292 3782 1080 7477 2114 6693 2103
#  6709 2103 6912 9167 9030 6015 4471 5572 4241 9950
#  8674 9205 2418 2197 3386 8658 2041  200 5143  698
#  7229 9064 2142 3439 3005 9746 3176 5375 4337 4346
#  9249 5163 9912 6672 4234 7876 8093 4958 9476 3486
#  4859 8517 7495 4892 9165  542 7644 8339 5396  254
#  8164 8693 6252 6480 6722 2962 6214 2631 3837 3861
#  1044 4493 3339 1995  105 5263 3577 5504 2027 7530
#  4260 2290 3912 3468 7349 5834 6796 5091 8475 3039
#  9011 2120  391 1174 8515  956 6869 1647 3752 2637
#
#
# -----------------------------------------------------------------------------
# EXTRA NOTES
# -----------------------------------------------------------------------------
#
# 1. Upon reading EOF, the program exits.
#
# 2. The `DebugObj` class makes debugging with print statements much cleaner by
#    separating the tests into its own code block.
#
# =============================================================================
