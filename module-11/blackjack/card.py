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

import stdarray	# type: ignore


suits = stdarray.create1D(4, '')
suits = [
	'Hearts', 
	'Spades', 
	'Diamonds',
	'Clubs'
]

faces: dict[str, int] = {
	'Ace': 1,
	'Two': 2,
	'Three': 3,
	'Four': 4,
	'Five': 5,
	'Six': 6,
	'Seven': 7,
	'Eight': 8,
	'Nine': 9,
	'Ten': 10,
	'Jack': 10,
	'Queen': 10,
	'King': 10
}



class Card:
	"""
	Card object for use in card games, like Blackjack.

	Arguments
	---------
		suit (str): suit of the card. Must be plural; i.e. 'Hearts"
		face (str): face of the card
	"""

	def __init__(self, suit: str, face: str):
		if suit.title() in suits:
			self.suit = suit.title()
		else:
			raise ValueError(f'{suit} is not a valid suit name. Valid suits are {suits}.')
		
		self.set_value(face)
			
	
	def _from_face(self, face: str) -> int:
		"""
		Get str value from int value.

		Arguments
		---------
			face (str): string representation of the card's value; i.e. 'Ace', 'Three', or 'Jack' 

		Returns
		-------
			(int) numerical representation of the card's value; i.e. 1, 3, or 10
		"""

		# grab the value associated with the face
		return faces[face]
	

	def set_value(self, face: str) -> None:
		"""
		Set both int and str values of card from given numerical representation of the card's value.

		Arguments
		---------
			face (str): string representation of the card's value; i.e. 'Ace', 'Three', or 'Jack' 
		"""

		# verify that the given face is actually valid
		if face.title() in faces.keys():
			# make sure the set face value is in title case
			self.face = face.title()

			# find the card's value from the given face
			self.value = self._from_face(face.title())
		else:
			raise ValueError('Given face is not valid.')
		
	
	# special methods
	def __str__(self) -> str:
		return f'{self.face} of {self.suit}'
	
	def __repr__(self) -> str:
		return f"Card(suit='{self.suit}', _face='{self.face}', _value={self.value})"
	


def _tc():
	"""
	Test client; not part of API.
	"""
	a = Card('Spades', 'King')
	print(a)
	print(repr(a))


if __name__ == '__main__':
	_tc()