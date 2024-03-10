#!/usr/bin/env python3

"""
Helpful functions that really should be built-in.

Functions
---------
* `avg(numbers: list[int|float]) -> float`
* `median(numbers: list[int|float]) -> int|float`

---

Average
=======
Returns the average of the given list

Argument
--------
	numbers: list of floats or ints

Returns
-------
	float

---

Median
======
Returns the median of the given list

Argument
--------
	numbers: list of floats or ints

Returns
-------
	int or float
"""

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

	# sort numbers
	numbers = list(sorted(numbers))

	if len(numbers) % 2 == 0:
		# if even
		low = numbers[int(len(numbers) / 2 - 1)]
		high = numbers[int(len(numbers) / 2)]

		return avg([low, high])
	
	else:
		# if odd
		return numbers[int(len(numbers) / 2 - 0.5)]


def stdinList(a: str) -> list:
	"""
	Converts a string-enclosed list (default format for stdin or sys.argv inputs) to a proper list

	Argument
	--------
		a: str-enclosed list; i.e. `"[1, 3.2, [4, 5], 'a', {'b': 4}, True, (7, 'v')]"`

	Returns
	-------
		true Python list object; i.e. `[1, 3.2, [4, 5], 'a', {'b': 4}, True, (7, 'v')]`
	"""

	import re

	b = re.findall(r'"\s*([^"]*?)\s*"', a)

	return b


def _testClient():
	"""
	NOT PART OF THE API.
	--------------------

	Simple test client. 
	"""

	import stdarray
	import stdio


	odd = stdarray.create1D(5, 0)
	odd = [20, 15, 16, 16, 9, 6, 19, 0, 19, 12, 3, 5, 2, 11, 10]

	even = stdarray.create1D(6, 0)
	even = [19, 7, 5, 10, 4, 0, 18, 16, 9, 16, 13, 0, 1, 6, 8, 14]


	stdio.writeln('\n--- Helpful.py Test Client ---')
	stdio.writeln('NOTE: This function is not part of the API and is only here for testing purposes.\n')

	stdio.writef('odd:\n\torig = %s\n\tsorted = %s\n', str(odd), str(list(sorted(odd))))
	stdio.writef('even:\n\torig = %s\n\tsorted = %s\n', str(even), str(list(sorted(even))))

	stdio.writeln('\nAll values printed first as an integer and later as a float fix 4.')

	stdio.writef('avg(odd):\n\tint: %d\n\tfloat: %.4f\n', avg(odd), avg(odd))
	stdio.writef('avg(even):\n\tint: %d\n\tfloat: %.4f\n', avg(even), avg(even))

	stdio.writef('median(odd):\n\tint: %d\n\tfloat: %.4f\n', median(odd), median(odd))
	stdio.writef('median(even):\n\tint: %d\n\tfloat: %.4f\n', median(even), median(even))

	stdio.writeln('\n--- End Test Client ---\n')


if __name__ == '__main__':
	_testClient()