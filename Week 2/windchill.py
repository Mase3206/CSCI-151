#!/usr/bin/env python3

# =============================================================================
# windchill.py
#
# A simple program to calculate the windchill given a temperature and wind speed
#
# Noah S. Roberts
# 01/24/2024
# Assignment 2
# for Week 2
# Book Excercise 1.2.22
# =============================================================================

import stdio, argparse

class RangeError(Exception):
	pass



def wc(temperature, velocity):
	# if the temperature or velocity is out of range, raise an exception
	if velocity > 50:
		raise RangeError('Velocity is out of range. velocity.range = [0, 50]')
	if not 3 < temperature < 120:
		raise RangeError('Temperature is out of range. temperature.range = [3, 120]')
	
	# do the actual math and return it
	return 35.74 + (0.6215 * temperature) + (0.4275 * temperature - 35.75) * (velocity ** 0.16)


# only deal with command line arguments if called directly; avoids errors when importing as a module
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='A simple wind chill calculator written in Python 3')
	parser.add_argument('-v', '--version', action='version', version='%(prog)s v0.1')

	# add the command line arguments
	parser.add_argument(
		'temperature', type=float, 
		help='Base temperature in Fahrenheit')
	parser.add_argument(
		'velocity', type=float,
		help='Wind speed in miles per hour')
	
	# parse and bundle of all the user's inputed args
	args = parser.parse_args()

	# get the RealFeel(tm)
	realFeel = wc(args.temperature, args.velocity)

	# display all the info all pretty like
	stdio.writeln('Temperature  : %.1f' % args.temperature)
	stdio.writeln('Wind speed   : %.1f' % args.velocity)
	stdio.writeln('RealFeel(tm) : %.1f' % realFeel)
	stdio.writeln()



# This is here simply to commenting at the end of the code not be completely 
# janky, as VS Code now knows for sure that there is code at the 0-indent
# level.
pass

# =============================================================================
# EXAMPLE USAGE
# -------------
#
# $ python windchill.py -h
# 	(displays helpful information)
#
# $ python windchill.py 37.4 16
# 	Temperature  : 37.4
#   Wind speed   : 16.0
#   RealFeel(tm) :
#
# 
# Q: Why use argparse instead of sys.argv?
# A: While sys.argv is much simpler, it is much more limited. sys.argv displays
#    the raw python exceptions to the user, which is handy for debugging but is
#    not user-friendly, and doesn't provide any explanation for what the
#    required and optional arguments are. argparse does all of that.
