#!/usr/bin/env python3


def sum_list(a: list) -> int|float:
	if len(a) == 1:
		return a[0]
	else:
		return sum_list(a[:len(a)-1]) + a[len(a) - 1]
	

def main(a: list) -> None:
	import stdio
	stdio.writeln(sum_list(a))


if __name__ == '__main__':
	main([1, 5, 3])