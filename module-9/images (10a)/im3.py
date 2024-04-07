#!/usr/bin/env python3

# =============================================================================
# im3.py
#
# Takes the name of a picture file as a command-line input, and creates three 
# images:     
# 	- one with only the red components
#	- one with only the green components
#	- and one with only the blue components
# 
# Noah S. Roberts
# 04.03.2024
# Assignment 10a
# for Module 9
# Book Excercise 3.1.5
# =============================================================================

import stdio, stdarray, stddraw, stdstats, picture, sys, random, luminance, math



def shearX(pic: picture.Picture, angle: float) -> picture.Picture:
	skew = -math.tan(angle / 2)

	for y in range(pic.height):
		for x in range(pic.width):
			xNew = x + int(skew * y)
			pic.set(xNew, y, pic.get(x, y))
		
	return pic



def shearY(pic: picture.Picture, angle: float) -> picture.Picture:
	skew = math.sin(angle)

	for x in range(pic.width):
		for y in range(pic.height):
			yNew = y + int(skew * x)
			pic.set(x, yNew, pic.get(x, y))

	return pic




def main(pic: picture.Picture) -> None:
	step1 = shearX(pic, 90)
	step2 = shearY(step1, 90)
	step3 = shearX(step2, 90)
	stddraw.picture(step3)



if __name__ == '__main__':
	main(picture.Picture(sys.argv[1]))