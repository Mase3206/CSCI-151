#!/usr/bin/env python3

class Color:
	def __init__(self, r: int, g: int, b: int):
		self.r = r
		self.g = g
		self.b = b

		self.luminance = 0.299*r + 0.587*g + 0.114*b


	def __str__(self) -> str:
		return f'r = {self.r}, g = {self.g}, b = {self.b}'


	def __add__(self, other):
		rNew = min(self.r + other.r, 255)
		gNew = min(self.g + other.g, 255)
		bNew = min(self.b + other.b, 255)

		return Color(rNew, gNew, bNew)



	def toGrey(self):
		self.r = self.luminance
		self.g = self.luminance
		self.b = self.luminance

		return self.luminance


def isCompatible(c1: Color, c2: Color) -> True:
	compVal = abs(c1.toGrey() - c2.toGrey())

	if compVal >= 128:
		return True
	else:
		return False
	


RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)

YELLOW = Color(255, 255, 0)
TEAL = Color(0, 255, 255)
MAGENTA = Color(255, 0, 255)

BLACK = Color(0, 0, 0)
GREY = Color(127, 127, 127)
WHITE = Color(255, 255, 255)


# colors = [RED, GREEN, BLUE, YELLOW, TEAL, MAGENTA, BLACK, GREY, WHITE]
# for a in colors:
# 	for b in colors:
# 		print(f'{a} : {b} = {isCompatible(a, b)}')

wot = YELLOW + TEAL

print(wot)