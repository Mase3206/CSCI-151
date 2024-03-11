#!/usr/bin/env python3

import stdarray



class Dict():
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
	Converts a string-enclosed list (default format for stdin or sys.argv inputs) to a proper list

	Argument
	--------
		a: str-enclosed list; i.e. `"[1, 3.2, [4, 5], 'a', {'b': 4}, "true", (7, 'v')]"`

	Returns
	-------
		true Python list object; i.e. `[1, 3.2, [4, 5], 'a', {'b': 4}, True, (7, 'v')]`
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
				
				# everything else can just be marked as "content"
				# grab the content's type here too; fewer lines of code
				else:
					self.contentTypes[i] = 'content'
			else:
				self.contentTypes[i] = 'content'
		

		typeCounter = 0
		i = 0
		while i < self.length:
			j = 0

			if self.contentTypes[i] == 'content':
				self.objTypes[typeCounter] = canObjType(self.a[i])

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
				j += 1
				while True:
					if self.contentTypes[i + j] == 'list_end':
						break
					j += 1
				self.objTypes[typeCounter] = list

				self.parsed[typeCounter] = List(self.a[i:i+j+1]).parsed

				typeCounter += 1
				i += j + 1

			elif self.contentTypes[i] == 'dict_start':
				j += 1
				while True:
					if self.contentTypes[i + j] == 'dict_end':
						break
					j += 1
				self.objTypes[typeCounter] = dict

				self.parsed[typeCounter] = Dict(self.a[i:i+j+1]).parsed

				typeCounter += 1
				i += j + 1

			elif self.contentTypes[i] == 'tuple_start':
				j += 1
				while True:
					if self.contentTypes[i + j] == 'tuple_end':
						break
					j += 1
				self.objTypes[typeCounter] = tuple

				self.parsed[typeCounter] = Tuple(self.a[i:i+j+1]).parsed

				typeCounter += 1
				i += j + 1
			
			else:
				i += 1
		
		self.cleanup()
		
	
	def cleanup(self):
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





class Tuple():
	def __init__(self, a: str):
		self.parsed = tuple(List(a).parsed)




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



if __name__ == '__main__':
	a = List("[1, 3.2, [4, 5], 'a', {'b': 4, 'g': 4, 'c': 18.0}, True, (7, 'v')]")
	print(a.parsed)
	print(a.objTypes)
	print(a.contentTypes)
