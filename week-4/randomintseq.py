#!/usr/bin/env python3

# =============================================================================
# randomintseq.py
#
# Generates a sequence of random integers; for use with temperline.py
#
# Noah S. Roberts
# 02/09/2024
# Assignment 6
# for Week 4
# Book Excercise 1.5.10
# =============================================================================


import stdio, sys, random

# get the parameters from command line
count = int(sys.argv[1])
maxRand = int(sys.argv[2]) - 1


for i in range(count):
	# storing then writing may address some edge cases where only one character
	# out of the intended string is read
	rand = str(random.randint(0, maxRand))
	stdio.writeln(rand)


# =============================================================================
# EXAMPLE USAGE
# -----------------------------------------------------------------------------
# 
# $ python randomintseq.py 10 100
#	4
#	88
#	57
#	43
#	94
#	53
#	29
#	84
#	43
#	56
#
# $ python randomintseq.py 10 10000
#	6396
#	1688
#	1671
#	6279
#	4710
#	6666
#	6601
#	6932
#	7351
#	8801
#
#
# -----------------------------------------------------------------------------
# EXTRA NOTES
# -----------------------------------------------------------------------------
#
# 1. The `EOF` line at the end of the output is used by temperline.py as a 
#    keyword to stop reading lines.
#
# =============================================================================
