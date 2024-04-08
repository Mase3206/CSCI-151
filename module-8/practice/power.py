#!/usr/bin/env python3

# implement exponent using recursion


def power(base, exponent):
	if exponent == 0:
		return 1
	else:
		return base * power(base, exponent - 1)
	

if __name__ == '__main__':
	import stdio, sys
	# stdio.writeln(power(int(sys.argv[1]), int(sys.argv[2])))

	stdio.writeln(power(2, 3))