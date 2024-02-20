#!/usr/bin/env python3

import circle, sys

for i in range(20):
	p = i / 20
	circle.main(16, p, frametime=200)