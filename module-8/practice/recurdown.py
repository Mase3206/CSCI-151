#!/usr/bin/env python3


import stdio, sys

def down(n:int) -> int|None:
	if n == 0:
		stdio.writeln("Go!")
	else:
		stdio.writeln(n)
		down(n-1)
	

down(int(sys.argv[1]))