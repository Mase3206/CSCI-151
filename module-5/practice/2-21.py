#!/usr/bin/env python3

import math

import stdarray
import stdio


def max3(a:float|int, b:float|int, c:float|int) -> float|int:
	"""
	takes three int or float arguments and returns the largest one
	"""
	
	largest = -math.inf
	nums = stdarray.create1D(3, 0)
	nums = [a, b, c]

	for num in nums:
		if num > largest:
			largest = num

	return largest


def count(a:list, value):
	"""
	counts the number of occurances of a value in the given list
	"""
	occurances = 0
	for n in a:
		if n == value:
			occurances += 1

	return occurances


def odd(a:bool, b:bool, c:bool) -> bool:
	"""
	takes three booleans and returns True if an odd number of arguments are True, and False otherwise
	"""

	bools = stdarray.create1D(3, 0)
	bools = [a, b, c]

	occurances = count(bools, True)
	return bool(occurances % 2)


def majority(a:bool, b:bool, c:bool) -> bool:
	"""
	takes three booleans and returns True if at least two of the arguments are True, and False otherwise
	- does not use if statements
	"""
	
	bools = stdarray.create1D(3, 0)
	bools = [a, b, c]

	occurances = count(bools, True)
	return bool(occurances >= 2)


if __name__ == '__main__':
	stdio.writeln('\nTesting max3()')
	stdio.writeln(max3(3, 5, 98))
	stdio.writeln(max3(45, -89, 3))
	stdio.writeln(max3(-1, 34543, 3))
	stdio.writeln(max3(-1, -1, -1))
	stdio.writeln(max3(0, 0, 0))
	stdio.writeln(max3(1, 1, 1))

	stdio.writeln('\nTesting odd()')
	stdio.writeln(odd(False, False, False))
	stdio.writeln(odd(True, False, False))
	stdio.writeln(odd(True, True, False))
	stdio.writeln(odd(True, True, True))

	stdio.writeln('\nTesting majority()')
	stdio.writeln(majority(False, False, False))
	stdio.writeln(majority(True, False, False))
	stdio.writeln(majority(True, True, False))
	stdio.writeln(majority(True, True, True))