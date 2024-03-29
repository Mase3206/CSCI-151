
import sys, stdio


def fib(n: int):
	if n <= 1:
		return n
	else:
		return fib(n - 1) + fib(n - 2)


n = int(sys.argv[1])
# n = 3

stdio.writeln('dude bro it\'s Fib bro')
for i in range(n):
	stdio.write(str(fib(i)) + ' ')

stdio.writeln('\ndude bro that\'s sick bro')
