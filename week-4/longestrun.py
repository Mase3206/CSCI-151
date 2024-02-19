#!/usr/bin/env python3

# =============================================================================
# longestrun.py
#
# Reads a sequence of integers and writes both the integer that appears in a
# longest consecutive run and the length of the run
#
# Noah S. Roberts
# 02/18/2024
# Assignment 5
# for Week 4
# Book Excercise 1.5.5
# =============================================================================


import stdio, stdarray


def count(numbers:list[int]):
	# using a dict makes returning multiple values easier
	longest = {
		'num': 0,
		'len': 1
	}
	# kind of like a live tally of a number's run length
	longTry = 1

	for i in range(len(numbers)):
		# avoid a false postive with a negative index
		if i == 0:
			longest['num'] = numbers[i]
			continue

		if numbers[i] == numbers[i - 1]:
			longTry += 1
			if longTry > longest['len']:
				longest['num'] = numbers[i]
				longest['len'] = longTry
		else:
			# if the two don't match, that means that any previous run has
			# ended -- so set `longTry` to default of 1
			longTry = 1			
	
	return longest


# initialize numbers array
numbers = stdarray.create1D(0, 0)

while True:
	try:
		numbers += [stdio.readInt()]
	except EOFError:
		break

longest = count(numbers)
stdio.writef('Longest run: %d consecutive %ds\n', longest['len'], longest['num'])


# =============================================================================
# EXAMPLE USAGE
# -----------------------------------------------------------------------------
# 
# $ python longestrun.py 
#	1 2 2 1 5 1 1 7 7 7 7 1 1
#	Longest run: 4 consecutive 7s
#
# $ python longestrun.py 
#	5 5 5 5 0 5 5 5 5 5
#	Longest run: 5 consecutive 5s
#
# $ python randomintseq.py 100000 10 | python longestrun.py
#	Longest run: 7 consecutive 8s
#
# =============================================================================
