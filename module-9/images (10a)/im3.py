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

import stdio, stdarray, stddraw, stdstats, picture, sys, random, luminance, math, color


def redOnly(orig: picture.Picture) -> picture.Picture:
	dimX = orig.width()
	dimY = orig.height()

	new = picture.Picture(dimX, dimY)


	for x in range(dimX):
		for y in range(dimY):
			new.set(
				x, y,
				color.Color(orig.get(x, y).getRed(), 0, 0)
			)
	

	return new



def greenOnly(orig: picture.Picture) -> picture.Picture:
	dimX = orig.width()
	dimY = orig.height()

	new = picture.Picture(dimX, dimY)


	for x in range(dimX):
		for y in range(dimY):
			new.set(
				x, y,
				color.Color(0, orig.get(x, y).getGreen(), 0)
			)
	

	return new



def blueOnly(orig: picture.Picture) -> picture.Picture:
	dimX = orig.width()
	dimY = orig.height()

	new = picture.Picture(dimX, dimY)


	for x in range(dimX):
		for y in range(dimY):
			new.set(
				x, y,
				color.Color(0, 0, orig.get(x, y).getBlue())
			)
	

	return new



def sideBySide(orig: picture.Picture) -> picture.Picture:
	dimX = orig.width()
	dimY = orig.height()

	new = picture.Picture(dimX * 3, dimY)


	for x in range(dimX):
		for y in range(dimY):
			new.set(
				x + (dimX * 0),
				y + (dimY * 0),
				color.Color(orig.get(x, y).getRed(), 0, 0)
			)

	for x in range(dimX):
		for y in range(dimY):
			new.set(
				x + (dimX * 1),
				y,
				color.Color(0, orig.get(x, y).getGreen(), 0)
			)

	for x in range(dimX):
		for y in range(dimY):
			new.set(
				x + (dimX * 2),
				y,
				color.Color(0, 0, orig.get(x, y).getBlue())
			)


	return new





def _test():
	orig = picture.Picture('mandrill.jpg')

	stddraw.setCanvasSize(orig.width(), orig.height())

	stddraw.picture(redOnly(orig)); stddraw.show(2000)
	stddraw.picture(greenOnly(orig)); stddraw.show(2000)
	stddraw.picture(blueOnly(orig)); stddraw.show(2000)



def main(orig: picture.Picture) -> None:
	dimX = orig.width()
	dimY = orig.height()

	stddraw.setCanvasSize(dimX * 3, dimY)
	stddraw.setXscale(-(dimX // 2), (dimX // 2) * 5)
	stddraw.setYscale(-(dimY // 2), (dimY // 2))

	new = sideBySide(orig)
	new.save('im3-out.jpg')
	stddraw.picture(new)
	stddraw.show()
	



if __name__ == '__main__':
	main(picture.Picture(sys.argv[1]))
	# _test()