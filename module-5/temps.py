#!/usr/bin/env python3

# =============================================================================
# temps.py
#
# Has two functions to convert between celsius and fahrenheit. Runs a test
# client if ran directly.
#
# Noah S. Roberts
# 02/23/2024
# In-class practice
# for Module 5
# Book Excercise ???
# =============================================================================

import stdio


def farh_to_celsius(farh:float):
	return (5/9) * (farh - 32)


def celsius_to_farh(celsius:float):
	return ((9/5) * celsius) + 32


def main():
	stdio.writeln('Testing F -> C:')
	stdio.writef('\t32°F is %.1f°C.\n', farh_to_celsius(32))		# 0c
	stdio.writef('\t5423°F is %.1f°C.\n', farh_to_celsius(5423))	# 2995c

	stdio.writeln('\nTesting C -> F:')
	stdio.writef('\t-23°C is %.1f°F.\n', celsius_to_farh(-23))		# -9.4f
	stdio.writef('\t4312°C is %.1f°F.\n', celsius_to_farh(4312))	# 7793.6


if __name__ == '__main__':
	main()


# =============================================================================
# EXAMPLE USAGE
# -----------------------------------------------------------------------------
#
# $ python temps.py
# 	Testing F -> C:
#       32°F is 0.0°C.
# 		5423°F is 2995.0°C.
#
# 	Testing C -> F:
# 		-23°C is -9.4°F.
# 		4312°C is 7793.6°F.
#
# =============================================================================
