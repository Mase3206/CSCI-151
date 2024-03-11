#!/usr/bin/env python3

# =============================================================================
# sic.py
#
# Code used by helpful.py to do the actual string-enclosed list conversion/parsing
#
# Noah S. Roberts
# 03.10.2024
# Assignment 9
# for Module 6
# Book Excercise ???
# =============================================================================


import stdarray



class Dict():
	"""
	Parses a string-enclosed dictionary into a proper dictionary. Not intended to be initialized directly and may not work correctly if doing so.
	"""
	def __init__(self, a: list):
		self.a = a
		self.d = {}
		self.keys = stdarray.create1D(len(self.a))
		self.values = stdarray.create1D(len(self.a))
		self.convert()
		self.parsed = self.d

	def convert(self):
		# self.a[0] = self.a[0][1:]
		# self.a[-1] = self.a[0][:-1]
			
		pair = stdarray.create1D(2)

		for i in range(len(self.a)):
			pair = stdarray.create1D(2)
			pair = self.a[i].split(': ')
			
			pair[0] = string(pair[0])
			if (objType := canObjType(pair[1])) == int:
				pair[1] = int(float(pair[1]))
			elif objType == float:
				pair[1] = float(pair[1])
			elif objType == bool:
				pair[1] = boolean(pair[1])
			elif objType == str:
				pair[1] = string(pair[1])

			self.d[pair[0]] = pair[1]



class List():
	"""
	Object that parses a string-enclosed list (default format for stdin or sys.argv inputs) to a proper list. It also stores the type of each of the main list's elements.

	Argument
	--------
		a: str-enclosed list; i.e. `"[1, 3.2, [4, 5], 'a', {'b': 4, 'g': 4, 'c': 18.0}, True, (7, 'v')]"`

	Returns
	-------
		List.parsed: true Python list object; i.e. `[1, 3.2, [4, 5], 'a', {'b': 4, 'g': 4, 'c': 18}, True, (7, 'v')]`
		List.objTypes: type of each of the main list's elements
	"""
	
	def __init__(self, a: str):
		temp = stdarray.create1D(0, 0)		# []
		temp = a[1:-1]						# "1, 3.2, [4, 5], 'a', {'b': 4, 'c': 18.0}, True, (7, 'v')"
		try:
			temp = temp.split(', ')			# ['1', '3.2', '[4', '5]', "'a'", "{'b': 4", "'c': 18.0}", 'True', '(7', "'v')"]
		except AttributeError:
			temp = a
		self.length = len(temp)
		self.a = temp

		self.contentTypes = stdarray.create1D(self.length, None)
		self.objTypes = stdarray.create1D(self.length, None)

		self.parsed = stdarray.create1D(self.length, None)

		self.convert()



	def convert(self):
		for i in range(self.length):
			if len(self.a[i]) > 1:
				# find lists
				if self.a[i][0] == '[':
					self.contentTypes[i] = 'list_start'
					self.a[i] = self.a[i][1:]
				elif self.a[i][-1] == ']':
					self.contentTypes[i] = 'list_end'
					self.a[i] = self.a[i][:-1]

				# find dictionaries
				elif self.a[i][0] == '{':
					self.contentTypes[i] = 'dict_start'
					self.a[i] = self.a[i][1:]
				elif self.a[i][-1] == '}':
					self.contentTypes[i] = 'dict_end'
					self.a[i] = self.a[i][:-1]

				# find tuples
				elif self.a[i][0] == '(':
					self.contentTypes[i] = 'tuple_start'
					self.a[i] = self.a[i][1:]
				elif self.a[i][-1] == ')':
					self.contentTypes[i] = 'tuple_end'
					self.a[i] = self.a[i][:-1]
				
				# everything else can just be marked as "content" as a catch-all
				else:
					self.contentTypes[i] = 'content'
			else:
				self.contentTypes[i] = 'content'
		

		# self.objTypes index
		typeCounter = 0

		# loop index; may increment by more than 1 per loop
		i = 0
		while i < self.length:
			j = 0

			if self.contentTypes[i] == 'content':
				# if not a list, dict, or tuple, find what type it can be (int, float, bool, or str)
				self.objTypes[typeCounter] = canObjType(self.a[i])

				# this dense block of code stores the value in it's optimal type
				# i.e. 'True' could be int(1), but it should be bool(True)
				# i.e.  94.0 could be type(float), but it should be type(int)
				if self.objTypes[typeCounter] == int:
					self.parsed[typeCounter] = int(float(self.a[i]))
				elif self.objTypes[typeCounter] == float:
					self.parsed[typeCounter] = float(self.a[i])
				elif self.objTypes[typeCounter] == bool:
					self.parsed[typeCounter] = boolean(self.a[i])
				elif self.objTypes[typeCounter] == str:
					self.parsed[typeCounter] = string(self.a[i])


				typeCounter += 1
				i += 1

			elif self.contentTypes[i] == 'list_start':
				# find the start and end point of the sublist and initialize another List object with that range
				j += 1
				while True:
					if self.contentTypes[i + j] == 'list_end':
						break
					j += 1
				self.objTypes[typeCounter] = list

				self.parsed[typeCounter] = List(self.a[i:i+j+1]).parsed

				typeCounter += 1
				# don't iterate over the elements within the sublist
				i += j + 1

			elif self.contentTypes[i] == 'dict_start':
				# find the start and end point of the dict and initialize a Dict object with that range
				j += 1
				while True:
					if self.contentTypes[i + j] == 'dict_end':
						break
					j += 1
				self.objTypes[typeCounter] = dict

				self.parsed[typeCounter] = Dict(self.a[i:i+j+1]).parsed

				typeCounter += 1
				# don't iterate over the elements within the dict
				i += j + 1

			elif self.contentTypes[i] == 'tuple_start':
				# find the start and end point of the tuple and initialize a Tuple object with that range
				j += 1
				while True:
					if self.contentTypes[i + j] == 'tuple_end':
						break
					j += 1
				self.objTypes[typeCounter] = tuple

				self.parsed[typeCounter] = Tuple(self.a[i:i+j+1]).parsed

				typeCounter += 1
				# don't iterate over the elements within the tuple
				i += j + 1
			
			else:
				i += 1
		
		self.cleanup()
		return self.parsed
		
	
	def cleanup(self):
		# remove unused None fillers at the end of the arrays and overwrite them
		temp_parsed = stdarray.create1D(0)
		for v in self.parsed:
			if v != None:
				temp_parsed.append(v)
		self.parsed = temp_parsed

		temp_objTypes = stdarray.create1D(0)
		for t in self.objTypes:
			if t != None:
				temp_objTypes.append(t)
		self.objTypes = temp_objTypes



class Tuple(List):
	"""
	Parses a string-enclosed tuple into a proper tuple. Not intended to be initialized directly and may not work correctly if doing so.
	"""
	
	def convert(self):
		parsed_list = super().convert()
		self.parsed = tuple(parsed_list)
	




def string(val: str) -> str:
	return val[1:-1]



def canInt(val: str|float) -> bool:
	if type(val) == float:
		if int(val) == val:
			return True
		else:
			return False
	else:
		try:
			a = int(val)
			del a
			return True
		except ValueError:
			return False
	


def canFloat(val: str) -> bool:
	try:
		a = float(val)
		del a
		return True
	except ValueError:
		return False
	


def canObjType(val: str) -> type:
	if canFloat(val):
		if canInt(float(val)):
			return int
		else:
			return float
	else:
		if val == 'True' or val == 'False' or val == 'None':
			return bool
		else:
			return str
		


def number(val: str) -> float|int:
	if canFloat(val):
		if canInt(float(val)):
			return int(val)
		else:
			return float(val)
	else:
		return val



def boolean(val: str) -> bool:
	if val == 'True':
		return True
	elif val == 'False':
		return False
	elif val == None:
		return None
	else:
		raise TypeError(f'Given val {val} is not a boolean')
	


def string(val: str) -> str:
	return val[1:-1]



def _testClient():
	a = List("[1, 3.2, [4, 5], 'a', {'b': 4, 'g': 4, 'c': 18.0}, True, (7, 'v')]")
	print(a.parsed)
	print(a.objTypes)
	print(a.contentTypes)


if __name__ == '__main__':
	_testClient()



# =============================================================================
# EXAMPLE USAGE
# -----------------------------------------------------------------------------
# 
# $ python sic.py 
# 	[1, 3.2, [4, 5], 'a', {'b': 4, 'g': 4, 'c': 18}, True, (7, 'v')]
# 	[<class 'int'>, <class 'float'>, <class 'list'>, <class 'str'>, <class 'dict'>, <class 'bool'>, <class 'tuple'>]
# 	['content', 'content', 'list_start', 'list_end', 'content', 'dict_start', 'content', 'dict_end', 'content', 'tuple_start', 'tuple_end']
#
#
# -----------------------------------------------------------------------------
# THAT'S COOL... BUT WHY??
# -----------------------------------------------------------------------------
#
# Every once in a while, I end up needing to read a valid Python object from
# standard input or from a text file. However, there aren't any quick, easy,
# and *secure* methods to parse the raw input (often a string object) into a 
# valid Python object. The methods that do exist are either (1) verifiably
# insecure and can be exploited, (2) finicky, requiring a very specific set of
# conditions to work, or (3) don't work or are very limited.
#
# So I said, "screw it, I'm a programmer, why don't I program this?"
# 	
# So I programmed it. It may not be the prettiest, most fully featured, or
# efficient, but by golly it's mine.
#
# =============================================================================
