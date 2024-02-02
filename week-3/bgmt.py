#!/usr/bin/env python3

# =============================================================================
# boysandgirls.py
#
# Simulate the number of children required to have one of each sex
#
# Noah S. Roberts
# 02/01/2024
# Assignment 3
# for Week 3
# Book Excercise ???
# =============================================================================

import stdio, stdarray, random, sys, concurrent.futures


debug = False
debugTrials = 1


def avg(l:list):
	return float(sum(l) / len(l))


class FloatToIntWarning(UserWarning):
	pass


def oneTrial():
	# Initialize the `children` array with NoneType
	# male = True; female = False (just makes comparisons easier)
	children = stdarray.create1D(1, None)

	# create the first child; will be used to compare against later children
	children[0] = bool(random.randint(0,1))

	# loop until a different sex is created
	i = 1
	while True:
		children += [bool(random.randint(0, 1))]

		# if this newly-created child has a different sex from the first child, end the loop.
		if children[0] != children[i]:
			break

		i += 1
	
	# return the number of created children
	return len(children)



def worker(trialPart:int):
	counts = stdarray.create1D(trialPart, 0)

	# run a trial `trials` times and set trial `i` to `counts[i]`
	for i in range(trialPart):
		counts[i] = oneTrial()

	return counts



def simulate(trials:int, threads=1):
	if threads < 1:
		raise ValueError(f"Thread count must be more than 1. Given: {threads}")
	if type(trials / threads) == float:
		raise FloatToIntWarning(f"Given number of trials and threads is not evenly divisible. Trial count per thread will be rounded down to nearest int. Total resulting trials: {(trials // threads) * threads}")
	
	# create an array `counts` of length `trials`
	workerCounts = stdarray.create1D(threads, 0)

	with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as worker:
		worker.submit(trials // threads)



def getFrequencies(counts:list):
	# create an array size max(counts) - 2
	# the `frequencies` array must have enough elements to hold the smallest and largest counts + everything in-between
	# the `- 2` allows for simple indexing, as the minimum count is 2 and the minimum index is 0.
	rawFrequencies = stdarray.create1D(max(counts) - 1, 0)
	frequencies = stdarray.create1D(4, 0)

	for qty in counts:
		rawFrequencies[qty - 2] += 1

	# rawFrequencies may not have at least 4 elements, so only copy what's there
	frequencies[0:min(3, len(rawFrequencies))] = rawFrequencies[0:min(3, len(rawFrequencies))]

	# When rawFrequencies has fewer than 4 elements, it may result in an IndexError. 
	# This is okay, because those counts just don't exist, so make sure to handle that specific error.
	# Other errors will still get thrown.
	try:
		frequencies[3] = sum(rawFrequencies[3:])
	except IndexError:
		pass

	return list[int](frequencies)



if __name__ == '__main__':
	if debug:
		trials = debugTrials
	else:
		trials = int(sys.argv[1])
	counts = simulate(trials)
	frequencies = getFrequencies(counts)

	stdio.writeln("Avg # children: " + str(avg(counts).__floor__()))
	stdio.writeln("Trials with 2 children: " + str(frequencies[0]))
	stdio.writeln("Trials with 3 children: " + str(frequencies[1]))
	stdio.writeln("Trials with 4 children: " + str(frequencies[2]))
	stdio.writeln("Trials with 5 or more children: " + str(frequencies[3]))






# Expected output
"""
> python boysandgirls.py 1000
Avg # children: 3
Trials with 2 children: 490
Trials with 3 children: 260
Trials with 4 children: 143
Trials with 5 or more children: 107

> python boysandgirls.py 1000
Avg # children: 3
Trials with 2 children: 509
Trials with 3 children: 245
Trials with 4 children: 119
Trials with 5 or more children: 127
"""