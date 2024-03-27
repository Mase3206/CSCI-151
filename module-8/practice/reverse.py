#!/usr/bin/env python3

import stdio

def reverse(string):
	stdio.writef("%s -> ", string)
	if len(string) == 1:
		return string
	else:
		stdio.writef("%s + %s\n", string[1:], string[0])
		return reverse(string[1:]) + string[0]
	

def main(a: str):
	a_len = len(a)
	stdio.writeln(reverse(a))


if __name__ == '__main__':
	import sys
	main(sys.argv[1])