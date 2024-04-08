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


import stdio, stdarray, stddraw, stdstats, picture, sys, random, luminance



def isAlreadyGrayscale(pic: picture.Picture) -> bool:
	randomX = stdarray.create1D(10, 0)
	randomY = stdarray.create1D(10, 0)

	for i in range(10):
		randomX.append(random.randint(0, pic.width()))

	for i in range(10):
		randomY.append(random.randint(0, pic.height()))

	
	for i in range(10):
		for j in range(10):
			same = stdarray.create1D(3, None)
			comparison = luminance.toGray(pic.get(i, j))

			same = [
				pic.get(randomX[i], randomY[j]).getRed() == comparison.getRed(),
				pic.get(randomX[i], randomY[j]).getGreen() == comparison.getGreen(),
				pic.get(randomX[i], randomY[j]).getBlue() == comparison.getBlue()
			]

			if same == [True, True, True]:
				return True
			else:
				return False
			
	

def toGrayscale(pic: picture.Picture) -> picture.Picture:
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
	values = stdarray.create1D(256, 0)

	for x in range(pic.width()):
		for y in range(pic.height()):
			values[pic.get(x, y).getBlue()] += 1

	return values

	

def plotGrayscale(values: list[int]) -> None:
	stddraw.setXscale(-1, 256 + 1)
	stddraw.setYscale(0, max(values) * 1.02)
	stddraw.setCanvasSize(1100, 400)
	for i in range(256):
		stddraw.filledRectangle(i, 0, 1.2, values[i])

	stddraw.save('im1-graph.png')
	stddraw.show()



def main(pic: picture.Picture) -> None:
	if not isAlreadyGrayscale(pic):
		pic = toGrayscale(pic)
	
	pic.save('im1-pic.jpg')
	values = countGrayscale(pic)
	plotGrayscale(values)



if __name__ == '__main__':
	main(picture.Picture(sys.argv[1]))
