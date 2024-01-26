#!/usr/bin/env python3

# =============================================================================
# compound.py
#
# Continuously compounded interest calculator; args: `t` years, `P` principal 
# investment, `r` annual interest rate
#
# Noah S. Roberts
# 01/24/2024
# Assignment 1
# for Week 2
# Book Excercise 1.2.21
# =============================================================================

import stdio, math, argparse


# The main function, named for the formula abbreviation
def pert(years, principal, interest):
	return round(principal * math.e ** (interest * years), 2)


# Only run this code block if running directly. This prevents "required 
# arguments" errors importing as a library.
if __name__ == '__main__':
	# initialize argparse
	parser = argparse.ArgumentParser(description='Simple continuously compounded interest calculator')
	# add code version
	parser.add_argument('-v', '--version', action='version', version='%(prog)s v0.1')

	# add the arguments for time, principal, and interest
	parser.add_argument(
		'years', type=int,
		help='Duration of investment in years')
	parser.add_argument(
		'principal', type=float,
		help='Principal (initial) investment')
	parser.add_argument('interest', type=float,
		help='Annual interest rate (float from 0.0 to 1.0)')
	
	# now parse and bundle of all the user's inputed args
	args = parser.parse_args()
	
	# call the pert() function with the parsed arguments, then call stdio.writeln() to send to stdout
	stdio.writeln(pert(args.years, args.principal, args.interest))
	


# This is here simply to commenting at the end of the code not be completely 
# janky, as VS Code now knows for sure that there is code at the 0-indent
# level.
pass

# =============================================================================
# EXAMPLE USAGE
# -------------
#
# $ python compound.py -h
# 	(displays helpful information)
#
# $ python compound.py 16 1000 .05
# 	2225.54
#
# 
# Q: Why use argparse instead of sys.argv?
# A: While sys.argv is much simpler, it is much more limited. sys.argv displays
#    the raw python exceptions to the user, which is handy for debugging but is
#    not user-friendly, and doesn't provide any explanation for what the
#    required and optional arguments are. argparse does all of that.
