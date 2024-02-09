#!/usr/bin/env python3

# =============================================================================
# randomintseq.py
#
# Generates a sequence of random integers; for use with temperline.py
#
# Noah S. Roberts
# 02/09/2024
# Assignment 5
# for Week 4
# Book Excercise 1.5.10
# =============================================================================

import stdio, sys, random


count = sys.argv[1]
maxRand = sys.argv[2] - 1

for i in range(count):
	stdio.writeln(random.randint(0, maxRand))