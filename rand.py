import sys, random

a = []
for i in range(int(sys.argv[1])):
	a.append(random.randint(0,9))

print(a)
