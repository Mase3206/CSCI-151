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

import math
import sys

import picture
import stddraw
import stdio


# The following two functions are unused from an attempt at a shear rotation.
# That attempt failed.
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
		# stdio.writef('Shift: %d, y_orig: %d, y_new: %d\n', shift, y, yNew)

	return picNew



def rotateR90(orig: picture.Picture) -> picture.Picture:
	"""
	Rotates the picture to the right 90 degrees.
	"""
	dimXorig = orig.width()
	dimYorig = orig.height()
	
	# x=y, y=x
	dimXnew = dimYorig
	dimYnew = dimXorig

	# do not modify the existing picture. it will not work.
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
	stdio.write('Rotating the image 90 degrees to the right via a "pixel swap"... ')
	new = rotateR90(pic)
	stdio.write("done.\n")

	stdio.write('Saving rotated image as im2-pic.jpg... ')
	new.save('im2-pic.jpg')
	stdio.write('done.\n')


	dimX = new.width()
	dimY = new.height()

	stddraw.setCanvasSize(dimX, dimY)
	stddraw.setXscale(-(dimX // 2), (dimX // 2))
	stddraw.setYscale(-(dimY // 2), (dimY // 2))

	stddraw.picture(new)
	stddraw.show()



if __name__ == '__main__':
	main(picture.Picture(sys.argv[1]))


# =============================================================================
# EXAMPLE USAGE
# -----------------------------------------------------------------------------
# 
# $ python im2.py mandrill.py
#	[pygame hello]
#	Rotating the image 90 degrees to the right via a "pixel swap"... done.
#	Saving rotated image as im2-pic.jpg... done.
#	(rotated picture - pygame output)
#
# -----------------------------------------------------------------------------
# EXTRA NOTES
# -----------------------------------------------------------------------------
#
# 1. I wasn't able to figure out skew rotation. I'm not sure what was making it 
#	 break, but you saw what it spit out in my attempts.
#
# =============================================================================
