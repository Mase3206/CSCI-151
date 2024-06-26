#!/usr/bin/env python3

# =============================================================================
# im1.py
#
# Takes the name of a grayscale picture file as a command-line argument and 
# uses stddraw to plot a histogram of the frequency of occurrence of each of 
# the 256 grayscale intensities.
#
# Noah S. Roberts
# 04.03.2024
# Assignment 10a
# for Module 9
# Book Excercise 3.1.4
# =============================================================================


import random
import sys

import luminance
import picture
import stdarray
import stdio
import stddraw


def isAlreadyGrayscale(pic: picture.Picture) -> bool:
	"""
	Samples 100 random pixels to check whether or not the image is grayscale.

	Argument
	--------
		pic (Picture): booksite Picture object

	Returns
	-------
		bool: true if all 100 trios of points are equal to each other, false if any one value in a trio is different
	"""

	randomX = stdarray.create1D(0, 0)
	randomY = stdarray.create1D(0, 0)

	# 10 random x locations
	for i in range(10):
		randomX.append(random.randint(0, pic.width()))

	# 10 random y locations
	for i in range(10):
		randomY.append(random.randint(0, pic.height()))

	
	# 100 random points
	for i in range(10):
		for j in range(10):
			same = stdarray.create1D(3, None)
			comparison = luminance.toGray(pic.get(randomX[i], randomY[j]))

			# compares actual red, green, and blue values to the point's luminance
			same = [
				pic.get(randomX[i], randomY[j]).getRed() == comparison.getRed(),
				pic.get(randomX[i], randomY[j]).getGreen() == comparison.getGreen(),
				pic.get(randomX[i], randomY[j]).getBlue() == comparison.getBlue()
			]

   
			# Be verbose in your findings!
			# if same != [True, True, True]:
			# 	stdio.write('Found difference: ')
				
			# 	if same[0] == False:
			# 		stdio.writef('red @ %dx%d = %d, expected %d', randomX[i], randomY[j], pic.get(randomX[i], randomY[j]).getRed(), comparison.getRed())
			# 	elif same[1] == False:
			# 		stdio.writef('green @ %dx%d = %d, expected %d', randomX[i], randomY[j], pic.get(randomX[i], randomY[j]).getGreen(), comparison.getGreen())
			# 	elif same[2] == False:
			# 		stdio.writef('blue @ %dx%d = %d, expected %d', randomX[i], randomY[j], pic.get(randomX[i], randomY[j]).getBlue(), comparison.getBlue())
			# 	else:
			# 		stdio.write('erronious ')

			# 	stdio.writeln()


			# if any comparison is not True, immediately return False
			if same != [True, True, True]:
				return False
			
	
	# if every single point passed, now return True
	return True
			
	

def toGrayscale(pic: picture.Picture) -> picture.Picture:
	"""
	Converts each pixel in the given picture to grayscale, then returns it.
	"""
	for i in range(pic.width()):
		for j in range(pic.height()):
			pic.set(
				x=i,
				y=j,
				c=luminance.toGray(pic.get(
					x=i, y=j
				))
			)

	return pic



def countGrayscale(pic: picture.Picture) -> list[int]:
	"""
	Counts the quantity of pixels with a given grayscale value (luminance). 

	Ex: at luminance = 24, found 13 pixels
	"""
	values = stdarray.create1D(256, 0)

	for x in range(pic.width()):
		for y in range(pic.height()):
			values[pic.get(x, y).getBlue()] += 1

	return values

	

def plotGrayscale(values: list[int]) -> None:
	"""
	Plots the distribution of grayscale pixels on a histogram.
	"""
	stddraw.setXscale(-1, 256 + 1)
	stddraw.setYscale(0, max(values) * 1.02)
	stddraw.setCanvasSize(1100, 400)

	for i in range(256):
		stddraw.filledRectangle(i, 0, 1.2, values[i])

	stdio.write('Saving histogram as im1-graph.jpg... ')
	stddraw.save('im1-graph.jpg')
	stdio.write('done.\n')

	stddraw.show()



def main(pic: picture.Picture) -> None:
	if not isAlreadyGrayscale(pic):
		stdio.write('Picture is not already grayscale; fixing... ')
		pic = toGrayscale(pic)
		stdio.write('done.\n')
	else:
		stdio.writeln('Picture is already grayscale')
	
	stdio.write('Saving grayscale image as im1-pic.jpg... ')
	pic.save('im1-pic.jpg')
	stdio.write('done.\n')

	stdio.write('Counting grayscale values... ')
	values = countGrayscale(pic)
	stdio.write('done.\n')

	plotGrayscale(values)



if __name__ == '__main__':
	main(picture.Picture(sys.argv[1]))



# =============================================================================
# EXAMPLE USAGE
# -----------------------------------------------------------------------------
# 
# $ python im1.py mandrill.py
# 	[pygame hello]
#	Picture is not already grayscale; fixing... done.
#	Saving grayscale image as im1-pic.jpg... done.
#	Counting grayscale values... done.
#	Saving histogram as im1-graph.jpg... done.
#	(histogram - pygame output)
# 
# 
# $ python im1.py im1-pic.jpg   # this is already grayscale
#	[pygame hello]
#	Picture is already grayscale
#	Saving grayscale image as im1-pic.jpg... done.
#	Counting grayscale values... done.
#	Saving histogram as im1-graph.jpg... done.
#	(histogram - pygame output)
#
# -----------------------------------------------------------------------------
# EXTRA NOTES
# -----------------------------------------------------------------------------
#
# 1. If you give it an image file that is not already grayscale, it will
#	 convert it automatically. If it detects that the image *is* already
#	 grayscale, it will not convert it at all.
#
# =============================================================================
