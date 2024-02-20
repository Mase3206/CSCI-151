#!/usr/bin/env python3

# =============================================================================
# dice.py
#
# Simulate the probabilities of each sum of two d6 die and compare against the
# theoretical probabilities.
#
# Noah S. Roberts
# 02/07/2024
# Assignment 4
# for Week 3
# Book Excercise 1.4.20
# =============================================================================

import random
import sys

# booksite modules
import stdarray
import stdio


# set the number of trials
# at least 500,000 trials are required for simulated probabilities to be within 
# 3 decimal digits of exact probabilities; 1,000,000 gives greater chance
debug = False
if debug:
	trials = 1000
else:
	trials = int(sys.argv[1])


def bufferNumber(number:int, maxNumber, after=True):
	"""
	Returns a string containing the given number and a calculated number of spaces before or after to make visual reading easier

	Arguments
	=========
	`number` : number to print
	`maxNumber` : expected maximum number that will be printed
	`after` (default True) : bool for where to add the spaces

	Return
	======
	`bufferedNumber` : string containing given number with added buffer in desired location
	"""

	# calculate the number of digits in each number
	digits = number // 10
	maxDigits = maxNumber // 10

	# length of the buffer is the difference in the number of digits of the two numbers
	bufferLen = maxDigits - digits
	buffer = ''.join(stdarray.create1D(bufferLen, ' '))

	# create the message array of length 2 (one index for the number, one for the buffer)
	bufferedNumber = stdarray.create1D(2)
	if after:
		bufferedNumber = [str(number), buffer]
	else:
		bufferedNumber = [buffer, str(number)]

	# join bufferedNumber w/ no separator and return it
	return ''.join(bufferedNumber)



def oneTrial():
	die1 = random.randint(1, 6)
	die2 = random.randint(1, 6)

	return die1 + die2


def simulate(trials:int):
	sums = stdarray.create1D(trials, 0)
	counts = stdarray.create1D(12, 0)
	frequencies = stdarray.create1D(12, 0.0)

	# run `trials` quantity trials and save sum in `sums[i]`
	for i in range(trials):
		sums[i] = oneTrial()
	
	# sort each sum into `counts` based on its value
	for val in sums:
		counts[val - 1] += 1

	# calculate frequencies from counts
	for j in range(len(counts)):
		frequencies[j] = counts[j] / len(sums)
	# frequencies = [(counts[j] / len(sums)) for j in range(len(counts))]
	
	# that's some stinky garbage
	del counts, sums

	# return the goods
	return list[float](frequencies)


# calculate the exact probabilities
exactProbabilities = stdarray.create1D(13, 0.0)
for i in range(1, 7):
	for j in range(1, 7):
		exactProbabilities[i+j] += 1.0
for k in range(2, 13):
	exactProbabilities[k] /= 36.0

# write the exacts to stdout
stdio.writeln('Exact probabilities for each sum of two d6:')
for i in range(2, 13):
	stdio.writef('    sum = %s:   %7.5f\n', bufferNumber(i, 12),  exactProbabilities[i])


# simulate!
frequencies = simulate(trials)


# write simulated probabilities to stdout
stdio.writeln('\nEmpirical results for each sum of two d6:')
for i in range(2, 13):
	stdio.writef('    sum = %s:   %7.5f\n', bufferNumber(i, 12), frequencies[i - 1])


# write difference in exact and simulated probabilities to stdout
stdio.writeln('\nDifference in exact and empirical probabilities for each sum of two d6:')
stdio.writeln('(exact - simulated)')
withinSpecCount = 0
for i in range(2, 13):
	stdio.writef('    sum = %s:  %8.5f', bufferNumber(i, 12), exactProbabilities[i] - frequencies[i - 1])

	# if the two are within three decimal places, write a check mark and newline to the end of that line
	# if not, write a newline
	if -0.001 < exactProbabilities[i] - frequencies[i - 1] < 0.001:
		stdio.writef(' %c\n', chr(0x2713))  # this prints the check mark
		withinSpecCount += 1
	else:
		stdio.writeln()
stdio.writef('\nNumber of probabilities in spec:  %d of 11\n', withinSpecCount)
stdio.writeln('("within spec" means within three decimal places of each other)')


# =============================================================================
# EXAMPLE USAGE
# -----------------------------------------------------------------------------
# 
# $ python dice.py 1000
#		Exact probabilities for each sum of two d6:
#			sum = 2 :   0.02778
#			sum = 3 :   0.05556
#			sum = 4 :   0.08333
#			sum = 5 :   0.11111
#			sum = 6 :   0.13889
#			sum = 7 :   0.16667
#			sum = 8 :   0.13889
#			sum = 9 :   0.11111
#			sum = 10:   0.08333
#			sum = 11:   0.05556
#			sum = 12:   0.02778
#
#		Empirical results for each sum of two d6:
#			sum = 2 :   0.03300
#			sum = 3 :   0.05400
#			sum = 4 :   0.09600
#			sum = 5 :   0.10900
#			sum = 6 :   0.12000
#			sum = 7 :   0.18100
#			sum = 8 :   0.13200
#			sum = 9 :   0.11500
#			sum = 10:   0.08000
#			sum = 11:   0.05900
#			sum = 12:   0.02100
#
#		Difference in exact and empirical probabilities for each sum of two d6:
#		(exact - simulated)
#			sum = 2 :  -0.00522
#			sum = 3 :   0.00156
#			sum = 4 :  -0.01267
#			sum = 5 :   0.00211
#			sum = 6 :   0.01889
#			sum = 7 :  -0.01433
#			sum = 8 :   0.00689
#			sum = 9 :  -0.00389
#			sum = 10:   0.00333
#			sum = 11:  -0.00344
#			sum = 12:   0.00678
#
#		Number of probabilities in spec:  0 of 11
#		("within spec" means within three decimal places of each other)
#
#
# $ python dice.py 500000
#		Exact probabilities for each sum of two d6:
#			sum = 2 :   0.02778
#			... (shortened)
#
#		Empirical results for each sum of two d6:
#			sum = 2 :   0.02755
#			... (shortened)
#
#		Difference in exact and empirical probabilities for each sum of two d6:
#		(exact - simulated)
#			sum = 2 :   0.00023 ✓
#			sum = 3 :  -0.00009 ✓
#			sum = 4 :   0.00015 ✓
#			sum = 5 :   0.00010 ✓
#			sum = 6 :  -0.00040 ✓
#			sum = 7 :   0.00013 ✓
#			sum = 8 :   0.00004 ✓
#			sum = 9 :  -0.00079 ✓
#			sum = 10:   0.00002 ✓
#			sum = 11:   0.00037 ✓
#			sum = 12:   0.00024 ✓
#
#		Number of probabilities in spec:  11 of 11
#		("within spec" means within three decimal places of each other)
#
# =============================================================================
