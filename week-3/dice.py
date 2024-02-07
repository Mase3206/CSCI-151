#!/usr/bin/env python3

# =============================================================================
# dice.py
#
# Calculate dice roll things
#
# Noah S. Roberts
# 02/07/2024
# Assignment 4
# for Week 3
# Book Excercise 1.4.20
# =============================================================================

import stdio, stdarray, sys, random

debug = False


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

	# length of the buffer is the difference in the number of digits of the two numbers
	digits = number // 10
	maxDigits = maxNumber // 10
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

	stdio.writeln()

	# run `trials` quantity trials and save sum in `sums[i]`
	for i in range(trials):
		# add a little progress bar
		# booksite `stdio` does not support this functionality, so I had to implement it with `sys.stdout`
		sys.stdout.flush()
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


if debug:
	trials = 1000
else:
	trials = int(sys.argv[1])
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
		stdio.writef(' %c\n', chr(0x2713))
		withinSpecCount += 1
	else:
		stdio.writeln()
stdio.writef('\nNumber of probabilities in spec:  %d of 11\n', withinSpecCount)
stdio.writeln('("within spec" means within three decimal places of each other)')