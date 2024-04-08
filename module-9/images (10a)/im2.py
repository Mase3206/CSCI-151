#!/usr/bin/env python3

# =============================================================================
# im2.py
#
# Takes the name of a picture file as a command-line argument and flips the 
# image horizontally. 
#
# Noah S. Roberts
# 04.03.2024
# Assignment 10a
# for Module 9
# Book Excercise 3.1.5
# =============================================================================

import stdio, stdarray, stddraw, stdstats, picture, sys, random, luminance, math


# unused
def shearX(pic: picture.Picture, angle: float) -> picture.Picture:
	stdio.writeln('\nX shear')
	skew = -math.tan(angle / 2)
	stdio.writef('Angle: %d, skew: %.4f\n', angle, skew)

	dimX = pic.width()
	dimY = pic.height()

	picNew = picture.Picture(dimX, dimY)

	for y in range(dimY):
		shift = int(skew * y)
		for x in range(dimX):
			xNew = (x - shift) #% dimX
			picNew.set(xNew, y, pic.get(x, y))
		# stdio.writef('Shift: %d, x_orig: %d, x_new: %d\n', shift, x, xNew)
		
	return picNew


# unused
def shearY(pic: picture.Picture, angle: float) -> picture.Picture:
	stdio.writeln('\nY shear')
	skew = math.sin(angle/2)
	stdio.writef('Angle: %d, skew: %.4f\n', angle, skew)

	dimX = pic.width()
	dimY = pic.height()

	picNew = picture.Picture(dimX, dimY)

	for x in range(dimX):
		shift = int(skew * x)
		for y in range(dimY):
			yNew = (y - shift) #% dimY
			picNew.set(x, yNew, pic.get(x, y))

	return picNew



def rotatep90(orig: picture.Picture) -> picture.Picture:
	dimXorig = orig.width()
	dimYorig = orig.height()

	dimXnew = dimYorig
	dimYnew = dimXorig

	new = picture.Picture(dimXnew, dimYnew)

	for x in range(dimXorig):
		for y in range(dimYorig):
			new.set(
				x=(dimYorig - y-1),
				y=x,
				c=orig.get(
					x=x,
					y=y
				)
			)

	return new



def main(pic: picture.Picture) -> None: 
	new = rotatep90(pic)
	new.save('im2-pic.jpg')


	dimX = new.width()
	dimY = new.height()

	stddraw.setCanvasSize(dimX, dimY)
	stddraw.setXscale(-(dimX // 2), (dimX // 2))
	stddraw.setYscale(-(dimY // 2), (dimY // 2))

	stddraw.picture(new)
	stddraw.show()



if __name__ == '__main__':
	main(picture.Picture(sys.argv[1]))