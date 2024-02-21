#!/usr/bin/env python3

# =============================================================================
# tenperline.py
#
# Nicely formats given numbers into columns of ten; for use with randomintseq.py
#
# Noah S. Roberts
# 02/09/2024
# Assignment 6
# for Week 4
# Book Excercise 1.5.10
# =============================================================================


import stdio, stdarray

debugEnabled = False

def debug(value:str, JSON=False):
	try:
		value = int(value)
		isInt = True
		isEOF = False
	except ValueError:
		isInt = False

		if value.lower() == 'eof':
			isEOF = True
		else:
			isEOF = False

	if JSON:
		stdio.writeln( {
			"value": value,
			"isInt": isInt,
			"isEOF": isEOF
		} )
	else:
		stdio.writef('Given value: %s\n', value)
		stdio.writef('Is integer: %s\n', isInt)
		stdio.writef('Is EOF: %s\n', isEOF)
	
	stdio.writeln()


more = True
while more == True:
	numbers = stdarray.create1D(0)

	for i in range(0,10):
		value = stdio.readString()
		if debugEnabled:
			debug(value, JSON=True)

		if stdio.isEmpty():
			numbers += {int(value)}
			more = False
			break
		else:
			numbers += [int(value)]

	for i in range(len(numbers)):
		stdio.writef("%5d", numbers[i])

	stdio.writeln()


# =============================================================================
# EXAMPLE USAGE
# -----------------------------------------------------------------------------
#
# $ python randomintseq.py 100 100 | python tenperline.py
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
# $ python randomintseq.py 100 74 | python tenperline.py
#    55   30   13   97   95   15   85    4   35   94
#     7   31   76   72   15   88   20    8   25   11
#    93   98   54   83   12   55   50   69   21   63
#    85   94   73   40   36   26   15    1   55   36
#    17   24   82   51   57   30   62   31   85   46
#    94   29   59   17   55   43   57   89    6   79
#    48   72   60   88   16   77   88   91   74   39
#    80   25   87   78
#
#
# -----------------------------------------------------------------------------
# EXTRA NOTES
# -----------------------------------------------------------------------------
#
# 1. The `debug` function makes brute-force debugging much cleaner by
#    separating the tests into its own code block.
#
# =============================================================================
