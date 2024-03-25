import sys, stdio


def factorial(n):
	if n == 1:
		return 1
	return n * factorial(n-1)


stdio.writeln(factorial(int(sys.argv[1])))