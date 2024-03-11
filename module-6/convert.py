#!/usr/bin/env python3

import stdarray



class stdinDict():
	def __init__(self, a: list):
		self.a = a



class stdinTuple():
	def __init__(self, a: list):
		self.a = a



class stdinList():
	def __init__(self, a: str):
		temp = stdarray.create1D(0, 0)		# []
		temp = a[1:-1]						# "1, 3.2, [4, 5], 'a', {'b': 4, 'c': 18.0}, True, (7, 'v')"
		temp = temp.split(', ')				# ['1', '3.2', '[4', '5]', "'a'", "{'b': 4", "'c': 18.0}", 'True', '(7', "'v')"]
		self.length = len(temp)
		self.a = temp
		self.contentTypes = stdarray.create1D(self.length, None)
		self.objTypes = stdarray.create1D(self.length, None)

		self.prep()



	def prep(self):
		for i in range(self.length):
			if len(self.a[i]) > 1:
				# find lists
				if self.a[i][0] == '[':
					self.contentTypes[i] = 'list_start'
				elif self.a[i][-1] == ']':
					self.contentTypes[i] = 'list_end'

				# find dictionaries
				elif self.a[i][0] == '{':
					self.contentTypes[i] = 'dict_start'
				elif self.a[i][-1] == '}':
					self.contentTypes[i] = 'dict_end'

				# find tuples
				elif self.a[i][0] == '(':
					self.contentTypes[i] = 'tuple_start'
				elif self.a[i][-1] == ')':
					self.contentTypes[i] = 'tuple_end'
				
				# everything else can just be marked as "content"
				# grab the content's type here too; fewer lines of code
				else:
					self.contentTypes[i] = 'content'
					# self.objTypes = canObjType(self.a[i])
			else:
				self.contentTypes[i] = 'content'
				# self.objTypes[i] = canObjType(self.a[i])
		

		typeCounter = 0
		i = 0
		while i < self.length:
			j = 0

			if self.contentTypes[i] == 'content':
				self.objTypes[typeCounter] = canObjType(self.a[i])
				typeCounter += 1
				i += 1

			elif self.contentTypes[i] == 'list_start':
				j += 1
				while True:
					if self.contentTypes[i + j] == 'list_end':
						break
					j += 1
				self.objTypes[typeCounter] = list
				typeCounter += 1
				i += j + 1

			elif self.contentTypes[i] == 'dict_start':
				j += 1
				while True:
					if self.contentTypes[i + j] == 'dict_end':
						break
					j += 1
				self.objTypes[typeCounter] = dict
				typeCounter += 1
				i += j 

			elif self.contentTypes[i] == 'tuple_start':
				j += 1
				while True:
					if self.contentTypes[i + j] == 'tuple_end':
						break
					j += 1
				self.objTypes[typeCounter] = tuple
				typeCounter += 1
				i += j
			
			else:
				# self.objTypes[typeCounter] = 'what'
				# typeCounter += 1
				i += 1
		return



	def recurse(self):
		raise NotImplementedError()


	def convert(self) -> list:

		# Try converting to a number first
		for i in range(self.length):
			self.a[i] = self.number(self.a[i])

		# Find lists and record their indeces
		
		return
		





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



if __name__ == '__main__':
	a = stdinList("[1, 3.2, [4, 5], 'a', {'b': 4, 'c': 18.0}, True, (7, 'v')]")
	a.convert()
