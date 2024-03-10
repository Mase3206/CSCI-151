#!/usr/bin/env python3

# =============================================================================
# helpful.py
#
# Helpful functions that really should be built-in.
#
# Noah S. Roberts
# 03.10.2024
# Assignment 9
# for Module 6
# Book Excercise ???
# =============================================================================


def avg(numbers: list[int|float]) -> float:
	"""
	Returns the average of the given list

	Argument
	--------
		numbers: list of floats or ints
	
	Returns
	-------
		float
	"""

	return sum(numbers) / len(numbers)


def median(numbers: list[int|float]) -> int|float:
	"""
	Returns the median of the given list

	Argument
	--------
		numbers: list of floats or ints

	Returns
	-------
		int or float
	"""

	if len(numbers) % 2 == 0:
		# if even
		low = numbers[len(numbers) / 2 - 1]
		high = numbers[len(numbers) / 2]

		return avg([low, high])
	
	else:
		# if odd
		return numbers[len(numbers) / 2 - 0.5]
	

def _test():
	"""
	NOT PART OF THE API.
	--------------------

	Simple test client. 
	"""

	import stdio, stdarray


	odd = stdarray.create1D(5, 0)
	odd = [0, 1, 2, 3, 4]

	even = stdarray.create1D(6, 0)
	even = [0, 1, 2, 3, 4, 5]


	stdio.writeln('\n--- Helpful.py Test Client ---')
	stdio.writeln('NOTE: This function is not part of the API and is only here for testing purposes.\n')
	stdio.writeln('All values printed first as an integer and later as a float fix 4.')

	stdio.writef('avg(odd):\n\tint: %d\n\tfloat: %.4f\n', avg(odd), avg(odd))
	stdio.writef('avg(even):\n\tint: %d\n\tfloat: %.4f\n', avg(even), avg(even))

	stdio.writef('median(odd):\n\tint: %d\n\tfloat: %.4f\n', median(odd), median(odd))
	stdio.writef('median(even):\n\tint: %d\n\tfloat: %.4f\n', median(even), median(even))

	stdio.writeln('--- End Test Client ---\n')