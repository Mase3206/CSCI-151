#!/usr/bin/env python3

# =============================================================================
# im3.py
#
# Takes the name of a picture file as a command-line input and splits it into
# three images: one for each of the three primary colors.
#
# Noah S. Roberts
# 04.03.2024
# Assignment 10a
# for Module 9
# Book Excercise 3.1.5
# =============================================================================

import sys

import color
import picture
import stddraw
import stdio



def sideBySide(orig: picture.Picture) -> picture.Picture:
	"""
	Grabs the red, green, and blue channels of the original image and draws them side-by-side.
	"""
	dimX = orig.width()
	dimY = orig.height()

	new = picture.Picture(dimX * 3, dimY)


	# RED
	stdio.write('Creating red component... ')
	for x in range(dimX):
		for y in range(dimY):
			new.set(
				x + (dimX * 0),
				y + (dimY * 0),
				color.Color(orig.get(x, y).getRed(), 0, 0)
			)
	stdio.write('done.\n')

	# GREEN
	stdio.write('Creating green component... ')
	for x in range(dimX):
		for y in range(dimY):
			new.set(
				x + (dimX * 1),
				y,
				color.Color(0, orig.get(x, y).getGreen(), 0)
			)
	stdio.write('done.\n')

	# BLUE
	stdio.write('Creating blue component... ')
	for x in range(dimX):
		for y in range(dimY):
			new.set(
				x + (dimX * 2),
				y,
				color.Color(0, 0, orig.get(x, y).getBlue())
			)
	stdio.write('done.\n')


	return new



def main(orig: picture.Picture) -> None:
	dimX = orig.width()
	dimY = orig.height()

	stddraw.setCanvasSize(dimX * 3, dimY)
	stddraw.setXscale(-(dimX // 2), (dimX // 2) * 5)
	stddraw.setYscale(-(dimY // 2), (dimY // 2))

	new = sideBySide(orig)
	stdio.write('Saving side-by-side image as im3-pic.jpg... ')
	new.save('im3-pic.jpg')
	stdio.write('done.\n')
	stddraw.picture(new)
	stddraw.show()




if __name__ == '__main__':
	main(picture.Picture(sys.argv[1]))



# =============================================================================
# EXAMPLE USAGE
# -----------------------------------------------------------------------------
#
# $ python im3.py mandrill.py
#	[pygame hello]
#	Creating red component... done.
#	Creating green component... done.
#	Creating blue component... done.
#	Saving side-by-side image as im3-pic.jpg...  done.
#	(image split into its color components - pygame output)
#
# =============================================================================
