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
		self.types = stdarray.create1D(0, None)

	
	def prep(self):
		for i in range(self.length):
			if len(self.a[i]) > 1:
				# find lists
				if self.a[i][0] == '[':
					self.types[i] = 'list_start'
				elif self.a[i][-1] == ']':
					self.types[i] = 'list_end'

				# find dictionaries
				elif self.a[i][0] == '{':
					self.types[i] = 'dict_start'
				elif self.a[i][-1] == '}':
					self.types[i] = 'dict_end'

				# find tuples
				elif self.a[i][0] == '(':
					self.types[i] = 'tuple_start'
				elif self.a[i][-1] == ')':
					self.types[i] = 'tuple_end'
				
				# everything else can just be marked as "content", as only 
				else:
					self.types[i] = 'content'
			else:
				self.types[i] = 'content'

	
	# def recurse(self):


	
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
