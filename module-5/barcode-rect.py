#!/usr/bin/env python3

# =============================================================================
# barcocde.py
#
# Makes USPS barcode from 5+4 zip code and checksum.
#
# Noah S. Roberts
# 02/24/2024
# Assignment 8a
# for Module 5
# Book Excercise 2.1.34
# =============================================================================

import stdio, stddraw, stdarray


barWidth = .5


class LengthError(ValueError):
	pass

class FormatError(LengthError):
	pass


def drawLine(height:int, xPos:int):
	"""
	drawLine draws a half- or full-height line at the given `x` position using pygame via booksite `stddraw`

	Arguments
	---------
		`height`: int, where 0 = half-height and 1 = full-height; this is the denonminator.
		`xPos`: float where line should be drawn

	Returns
	-------
	none
	"""

	if height == 0 or height == 1:
		stddraw.filledRectangle(xPos, 0, barWidth, height + 1)
		# stddraw.show(1)
	else:
		raise ValueError('Height must be binary 0 or 1.')


def calcDigit(digit:int):
	"""
	Takes a number and returns its USPS line-code pseudo-binary equivalent

	Argument
	--------
		`digit`: int

	Returns
	-------
		str containing USPS line-code pseudo-binary (ex: '01001')
	"""
	digits = {
		1: '00011',
		2: '00101',
		3: '00110',
		4: '01001',
		5: '01010',
		6: '01100',
		7: '10001',
		8: '10010',
		9: '10100',
		0: '11000'
	}

	return digits[digit]


def drawDigit(uspsBinDigit:str, digitPos:int):
	"""
	Takes a string representation of a USPS line-code pseudo-binary digit and draws the lines

	Argument
	--------
		`uspsBinDigit`: str containing pseudo-binary USPS line-code digit (ex: '01001')
		`digitPos`: int of digit group position (must be divisible by 5)

	Returns
	-------
	none
	"""

	for i in range(5):
		drawLine(int(uspsBinDigit[i]), digitPos + i)


def convert(code:str|list):
	"""
	Converts the Zip code between a string and a list. If given a string in the proper format, it will convert it to a list of a proper length, raising a LengthError if not. If given a list of a proper length, it will convert it to a string in the proper format, raising a FormatError if not.

	Argument
	--------
		`code`: 
			string-type: Zip code in 5-digit format ('00000') or 5+4-digit format ('00000-0000') 
			OR list-type: Zip code with length 5 or 9

	Returns
	-------
		string-type: Zip code in 5-digit format ('00000') or 5+4-digit format ('00000-0000')
		OR list-type: Zip code with length 5 or 9

	Examples
	--------
		5-digit: '19274' <-> [1, 9, 2, 7, 4]
		5+4-digit: '19274-7635' <-> [1, 9, 2, 7, 4, 7, 6, 3, 5]
	"""

	if type(code) == str:
		# only convert if code string uses 5 or 5+4 format
		if len(code) == 5: 
			codeList = stdarray.create1D(5)
			codeList = [int(d) for d in code]
			return codeList
		
		if len(code) == 10:
			codeList = stdarray.create1D(9)
			codeList = [int(d) for d in code if d != '-']
			return codeList

		else:
			raise FormatError('Code str must have length of 5 or 10 (if using 5+4 format)')
	
	elif type(code) == list:
		# only convert if code string has 5 or 9 (5+4 format) elements
		if len(code) == 5:
			# returns the code in the '00000' format
			codeList = stdarray.create1D(5)
			codeList = [str(code[i]) for i in range(5)]
			return str(''.join(codeList))
		
		elif len(code) == 9:
			# returns the code in the '00000-0000' format
			prefix = stdarray.create1D(5)
			prefix = [str(code[i]) for i in range(0, 5)]

			suffix = stdarray.create1D(4)
			suffix = [str(code[i]) for i in range(5, 9)]

			return str(''.join(prefix) + '-' + ''.join(suffix))
		
		else:
			raise LengthError('Code list must have length of 5 or 9')
	
	else:
		raise TypeError('Zip code must be str or list.')


def displayUBC(zipCode:str, frametime=2000):
	"""
	drawUBC (USPS BarCode) takes a 5-digit or 5+4-digit Zip code and displays it using pygame via booksite `stddraw`

	Argument
	--------
		`zipCode`: str

	Output
	------
		pygame graphic
	"""

	# create a list of the zipCode digits as integers
	zipList = convert(zipCode)

	if len(zipList) != 5 and len(zipList) != 9:
		raise LengthError(f'Zip code must be use the 5 or 5+4 format. ex: "54018" or "23875-3992". Given: {zipCode}')

	# digit group width
	dgw = 5

	# startLine + (digits) + checksum + endLine
	totalWidth = 1 + (dgw * len(zipList)) + dgw + 1

	# calculate checksum
	checksum = sum(zipList) % 10

	# adjust window and pen dimensions
	# the `-1 + barWidth` ensures the window gap at each end is similar
	stddraw.setXscale(-1 + barWidth, totalWidth)
	stddraw.setYscale(0, 5)


	# draw start and end lines
	drawLine(1, 0)
	drawLine(1, totalWidth - 1)

	# draw digits
	for i in range(len(zipList)):
		digit = calcDigit(zipList[i])
		drawDigit(digit, i * dgw + 1)

	# draw checksum
	checkDigit = calcDigit(checksum)
	drawDigit(checkDigit, totalWidth - 1 - dgw)

	stddraw.show(frametime)
	stddraw.clear()


if __name__ == '__main__':
	displayUBC('59401')
	displayUBC('59401-3410')
	displayUBC('98765')