#!/usr/bin/env python3


def print_sum(n: int) -> int:
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return print_sum(n-1) + n
	

def main(n: int):
	import stdio
	stdio.writeln(print_sum(n))


if __name__ == '__main__':
	import sys
	main(int(sys.argv[1]))