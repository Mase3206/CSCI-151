#!/usr/bin/env python3

# -----------------------------------------------------------------------------
# prac2.py
#
# Week 2 practice problem 2
#
# Noah S. Roberts
# 01/24/2024
# Assignment practice 2
# for Week 2
# Book Excercise 1.2.31
# -----------------------------------------------------------------------------

import stdio, sys

def main(num1, num2, num3):
	integers = [num1, num2, num3]


	minimum = min(integers)
	integers.remove(minimum)

	maximum = max(integers)
	integers.remove(maximum)

	mediumest = integers[0]


	sortedIntegers = [str(minimum), str(mediumest), str(maximum)]
	stdio.writeln(' '.join(sortedIntegers))



debug = False

if __name__ == '__main__' and debug == False:
	main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))

if debug == True:
	main(1, 5678, 8)
