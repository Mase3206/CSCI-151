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
debug = False
if debug:
	trials = 1000
else:
	trials = int(sys.argv[1])

# show progress
try:
	if sys.argv[2] == '-p':
		showProgress = True
except IndexError:
	showProgress = False


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
	counts = stdarray.create1D(11, 0)
	frequencies = stdarray.create1D(11, 0.0)

	if showProgress:
		stdio.writeln()
		sys.stdout.flush()

	# run `trials` quantity trials and save sum in `sums[i]`
	for i in range(trials):
		# add a little progress bar
		# booksite `stdio` does not support this functionality, so I had to implement it with `sys.stdout`
		if showProgress:
			progress = f"\rSimulation progress: {(100 * i) / trials:2.2f}%"
			sys.stdout.write(progress)
		sums[i] = oneTrial()
	
	# sort each sum into `counts` based on its value
	for val in sums:
		counts[val - 2] += 1

	# calculate frequencies from counts
	frequencies = [(counts[j] / len(sums)) for j in range(len(counts))]
	
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
	stdio.writef('    sum = %s:   %7.5f\n', bufferNumber(i, 12), frequencies[i - 2])


# write difference in exact and simulated probabilities to stdout
stdio.writeln('\nDifference in exact and empirical probabilities for each sum of two d6:')
stdio.writeln('(exact - simulated)')
withinSpecCount = 0
for i in range(2, 13):
	stdio.writef('    sum = %s:  %8.5f', bufferNumber(i, 12), exactProbabilities[i] - frequencies[i - 2])

	# if the two are within three decimal places, write a check mark and newline to the end of that line
	# if not, write a newline
	if -0.0001 < exactProbabilities[i] - frequencies[i - 2] < 0.0001:
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
#			sum = 2 :   0.03000
#			sum = 3 :   0.05300
#			sum = 4 :   0.08500
#			sum = 5 :   0.11000
#			sum = 6 :   0.14000
#			sum = 7 :   0.19000
#			sum = 8 :   0.12900
#			sum = 9 :   0.11500
#			sum = 10:   0.06000
#			sum = 11:   0.06000
#			sum = 12:   0.02800
#
#		Difference in exact and empirical probabilities for each sum of two d6:
#		(exact - simulated)
#			sum = 2 :  -0.00222
#			sum = 3 :   0.00256
#			sum = 4 :  -0.00167
#			sum = 5 :   0.00111
#			sum = 6 :  -0.00111
#			sum = 7 :  -0.02333
#			sum = 8 :   0.00989
#			sum = 9 :  -0.00389
#			sum = 10:   0.02333
#			sum = 11:  -0.00444
#			sum = 12:  -0.00022
#
#		Number of probabilities in spec:  0 of 11
#		("within spec" means within three decimal places of each other)
#
#
# $ python dice.py 1000000 -p
#		Exact probabilities for each sum of two d6:
#			sum = 2 :   0.02778
#			... (shortened)
#
#		Simulation progress: 100.00%
#		Empirical results for each sum of two d6:
#			sum = 2 :   0.02800
#			... (shortened)
#
#		Difference in exact and empirical probabilities for each sum of two d6:
#		(exact - simulated)
#			sum = 2 :  -0.00022
#			sum = 3 :  -0.00044
#			sum = 4 :   0.00003 ✓
#			sum = 5 :   0.00008 ✓
#			sum = 6 :  -0.00004 ✓
#			sum = 7 :  -0.00004 ✓
#			sum = 8 :  -0.00016
#			sum = 9 :   0.00022
#			sum = 10:   0.00012
#			sum = 11:   0.00016
#			sum = 12:   0.00029
#
#		Number of probabilities in spec:  4 of 11
#		("within spec" means within three decimal places of each other)
#
#
# -----------------------------------------------------------------------------
# EXTRA NOTES
# -----------------------------------------------------------------------------
#
# On lines 26-30, 80-82, and 88-90, I have code referencing a status or 
# progress indicator. This is an optional thing that can be enabled by using
# the `-p` option following the number of trials. I made this optional, as it
# requires using a non-booksite module for output. 
# 
# It is a non-critical component of the code, but it is a nice quality of life
# improvement to quickly make sure your code hasn't hung. I used it in Usage
# Example #2, but you won't actually be able to see what it does without 
# running it yourself.
# 
# If you are curious about why I did it this way or how it works, let me know!
# I'd be happy to share.
#
# =============================================================================
