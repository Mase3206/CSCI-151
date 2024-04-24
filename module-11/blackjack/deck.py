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

# Deck()					# Create a shuffled deck of 52 cards
# d.print_deck()			# Method was added for test client
# d.deal()				# Returns and removes card from deck
# d.deck_size()			# Returns size of deck


from card import Card, suits, faces
import stdarray
import random
import stdio


def initialize_empty_deck() -> list[Card]:
	# the initialized Card object in this line helps with PyLance's type annotations
	return stdarray.create1D(0, Card('Hearts', 'Ace'))


class Deck:
	"""
	A shuffled deck of 52 standard cards. Does not include the two Joker cards.
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
		i_card = random.randint(1, len(self._deck)-1)
		value_card = self._deck[i_card]
		self._deck.pop(i_card)
		return value_card
	
	
	def size(self) -> int:
		"""
		Returns the current size of the deck.

		Returns
		-------
			(int) current length of the deck
		"""
		return len(self._deck)



def _tc():
	d = Deck()
	# d._print_deck()
	print(d.size())
	print(d.deal_card())
	print(d.size())


if __name__ == '__main__':
	_tc()
