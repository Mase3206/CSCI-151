#!/usr/bin/env python3


import stdio


def hanoi(n: int, left: bool) -> str:
	if (n == 0): 
		return ' ' 

	move = ''
	if left:
		move = str(n) + 'L'
	else:
		move = str(n) + 'R'

	return hanoi(n-1, not left) + move + hanoi(n-1, not left)


def main(n: int):
	stdio.writeln(hanoi(n, False))


if __name__ == '__main__':
	import sys
	main(int(sys.argv[1]))
