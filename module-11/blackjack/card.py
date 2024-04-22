#!/usr/bin/env python3

# =============================================================================
# card.py
#
# File containing the Card class. Meant to be used only as a module.
#
# Noah S. Roberts
# 04.22.2024
# Assignment 13
# for Module 11
# =============================================================================

# Card(suit, face, value)	# Create a card
# c.get_value()			# Returns an integer indicating value of card
# c.set_value(v)			# Sets the value of card to v
# str(c)					# Example:  Two of Hearts


import stdarray

suits = [
	'Hearts', 
	'Spades', 
	'Diamonds',
	'Clubs'
]

strValues = [
	'Ace',
	'Two',
	'Three',
	'Four',
	'Five',
	'Six',
	'Seven',
	'Eight', 
	'Nine',
	'Ten',
	'Jack',
	'Queen',
	'King'
]


class Card:
	def __init__(self, suit: str, value: int):
		if suit in suits:
			self.suit = suit.title()
		else:
			raise ValueError(f'{suit} is not a valid suit name. Valid suits are {suits}.')
		
		self.set_value(value)


	def _from_face(self, faceValue: str) -> int:
		for i in range(len(strValues)):
			if faceValue == strValues[i]:
				return i + 1
			
	
	def _from_numerical(self, value: int) -> str:
		return strValues[value - 1]
	
	
	def get_value(self) -> str:
		return self._value
	

	def set_value(self, value: int) -> None:
		if value in range(1, 14):
			self._face = self._from_numerical(value)
			self._value = value
		else:
			raise ValueError('Given value is not a valid card.')
		
	
	def __str__(self) -> str:
		return f'{self._face} of {self.suit}'
	

def _tc():
	a = Card('Spades', value=1)
	print(a)

if __name__ == '__main__':
	_tc()