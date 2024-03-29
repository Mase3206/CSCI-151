import sys


def fib(n: int):
	if n <= 1:
		return n
	else:
		return fib(n - 1) + fib(n - 2)


n = int(sys.argv[1])
# n = 3

print('dude bro it\'s Fib bro')
for i in range(n):
	sys.stdout.write(str(fib(i)) + ' ')
	sys.stdout.flush()

print('\ndude bro that\'s sick bro')
