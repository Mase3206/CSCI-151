import sys, stdio


n = int(sys.argv[1])

product = 1
for i in range(1, n+1):
	product *= i

stdio.writeln(product)