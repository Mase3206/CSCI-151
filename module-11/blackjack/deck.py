#!/usr/bin/env python3

# =============================================================================
# deck.py
#
# File containing the Deck class. Meant to be used only as a module.
#
# Noah S. Roberts
# 04.22.2024
# Assignment 13
# for Module 11
# =============================================================================

from card import Card, suits, faces
import stdarray	# type: ignore
import random
import stdio	# type: ignore



def initialize_empty_deck() -> list[Card]:
	"""
	Return a list of type list[Card] of length zero. Helps with Pylance's linting.
	"""

	return stdarray.create1D(0, Card('Hearts', 'Ace'))



class Deck:
	"""
	A shuffled deck of 52 standard cards. Does not include the two Joker cards. Depends on card.py.
	"""

	def __init__(self):
		self._deck = initialize_empty_deck()
		for s in suits:
			for f in faces.keys():
				self._deck += [Card(s, f)]

		# super shuffle!
		random.shuffle(self._deck)
		random.shuffle(self._deck)
		random.shuffle(self._deck)

	
	def _print(self) -> None:
		"""
		Prints repr of each Card object in the Deck on a new line. Used by test client.
		"""
		for c in self._deck:
			stdio.writef("%s\n", repr(c))
	

	def deal_card(self) -> Card:
		"""
		Selects a random card from the deck, then removes it from the deck and returns it.

		Returns
		-------
			(Card) randomly-selected card
		"""

		i_card = random.randint(0, max(len(self._deck)-1, 1))

		# try to grab that card from the deck
		# I was having an issue where it wouldn't find the card, so this try-except block helps return a more helpful error
		try:
			value_card = self._deck[i_card]
		except IndexError:
			raise IndexError(f'Index {i_card} is not in self._deck (len={len(self._deck)}, max index={len(self._deck)-1})')
		
		self._deck.pop(i_card)
		return value_card
	
	
	# special methods
	def __len__(self) -> int:
		return len(self._deck)
	
	def __repr__(self) -> str:
		return f"Deck({self._deck})"
	
	def __str__(self) -> str:
		return f'This deck contains {len(self)} cards.'



def _tc():
	"""
	Test client; not part of API.
	"""
	d = Deck()
	# d._print_deck()
	print(len(d))
	print(d.deal_card())
	# print(len(d))
	print(repr(d))
	print(str(d))


if __name__ == '__main__':
	_tc()
