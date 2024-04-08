#!/usr/bin/env python3

"""
Simple module with a few basic statistic functions
"""


import math


def mean(numbers:list) -> float:
	return sum(numbers) / len(numbers)


def stdDev(numbers:list) -> float:
	# find the numerator
	numerator = 0
	for i in range(numbers):
		numerator += (numbers[i] - sum(numbers)) ** 2

	return


def main(numbers:list) -> float:
	"""
	
	"""
	return


if __name__ == '__main__':
	import stdio, stdarray

	a = [1, 2, 3, 4, 5]
	stdio.writeln(str(main(a)))

	b = [2, 6, 312, 5, -94]
	stdio.writeln(str(main(b)))