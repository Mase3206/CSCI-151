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



def rotatep90(orig: picture.Picture, theta: float) -> picture.Picture:
	dimXorig = orig.width()
	dimYorig = orig.height()

	# dimXnew = int(abs(dimXorig * math.cos(theta)) + abs(dimYorig * math.sin(theta))) + 1
	# dimYnew = int(abs(dimYorig * math.cos(theta)) + abs(dimXorig * math.sin(theta))) + 1
 
	dimXnew = dimYorig
	dimYnew = dimXorig

	print(dimXorig, dimYorig)
	print(dimXnew, dimYnew)

	new = picture.Picture(dimXnew, dimYnew)

	for x in range(dimXorig):
		for y in range(dimYorig):
			print(x, (dimYorig - y-1))
			new.set(
				x=(dimYorig - y-1),
				y=x,
				c=orig.get(
					x=x,
					y=y
				)
			)

	return new





# def shearTransform(orig: picture.Picture, theta: float):
	# dimXorig = orig.width()
	# dimYorig = orig.height()

	# dimXnew = int(abs(dimXorig * math.cos(theta)) + abs(dimYorig * math.sin(theta))) + 1
	# dimYnew = int(abs(dimYorig * math.cos(theta)) + abs(dimXorig * math.sin(theta))) + 1

	# new = picture.Picture(dimXnew, dimYnew)


# 	for y in range(dimYorig):
# 		for x in range(dimXorig):
# 			xNew = int(math.cos(theta) * x + math.sin(theta) * y)
# 			yNew = int(-math.sin(theta) * x + math.cos(theta) * y)
# 			print(xNew, yNew)

# 			new.set(
# 				x=xNew,
# 				y=yNew,
# 				c=orig.get(x, y)
# 			)

# 			print(orig.get(x, y), new.get(xNew, yNew))
	
# 	stddraw.picture(new)
# 	stddraw.show()
# 	return new



def main(pic: picture.Picture, angle: float) -> None:
	theta = math.radians(angle)

	dimX = pic.width()
	dimY = pic.height()

	dimYnew = int(abs(dimY * math.cos(theta)) + abs(dimX * math.sin(theta))) + 1
	dimXnew = int(abs(dimX * math.cos(theta)) + abs(dimY * math.sin(theta))) + 1

	stddraw.picture(pic)
	stddraw.show(2000)

	# asdfasdf = shearTransform(orig=pic, theta=theta)

	# stddraw.picture(asdfasdf)
	# stddraw.show()
 
	new = rotatep90(pic, theta)
	stddraw.picture(new)
	stddraw.show()


	# step1 = shearX(pic, theta)
	# stddraw.picture(step1)
	# stddraw.show(2000)
	
	# step2 = shearY(step1, theta)
	# stddraw.picture(step2)
	# stddraw.show(2000)

	# step3 = shearX(step2, theta)
	# stddraw.picture(step3)
	# stddraw.show()



if __name__ == '__main__':
	main(picture.Picture(sys.argv[1]), float(sys.argv[2]))