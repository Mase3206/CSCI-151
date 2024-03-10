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
		float average
	"""
	return sum(numbers) / len(numbers)


