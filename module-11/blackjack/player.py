#!/usr/bin/env python3

# =============================================================================
# player.py
#
# File containing the Player class. Meant to only be used as a module.
#
# Noah S. Roberts
# 04.22.2024
# Assignment 13
# for Module 11
# =============================================================================

# Player(name, balance)		# Create a player with a name, balance and hand
# p.print_hand()			# Prints player’s hand
# p.print_first()			# Prints only first card of player’s hand
# p.clear()					# Clears player’s hand
# p.deal_card(d)			# Adds a card to players hand from deck d
# p.print_balance()			# Prints the player’s balance
# p.get_balance()			# Returns the player’s balance
# p.bet(amount)				# Returns True and subtracts amount from player’s balance if player’s balance >= amount, Returns False otherwise
# p.win(amount)				# Adds amount to player’s balance
# p.blackjack_hand_value()	# Returns value of blackjack hand
# p.blackjack()				# Returns True if hand is a blackjack

import stdio, stdarray
from card import Card
from deck import Deck, initialize_empty_deck


# make an alias to avoid unnecessary calls to deck.py
initialize_empty_hand = initialize_empty_deck


# borrowed from a previous assignment
class Name:
	"""
	Name object
	
	Arguments
	---------
		first (str): first name
		last (str): last name
		middle (str; default ''): middle name or initial
	"""

	def __init__(self, first: str, last: str, middle=''):
		self.first = first
		self.last = last
		self._middle = middle

	
	def middle(self, initial=False):
		if self._middle == '':
			return ''
		elif len(self._middle) == 1 or initial == True:
			return f'{self._middle[0]}. '
		else:
			return f'{self._middle} '


	def fullName(self, useMiddleInitial=False):
		middle = self.middle(initial=useMiddleInitial)
		return f'{self.first} {middle}{self.last}'
	

	# special methods
	def __str__(self):
		return self.fullName()
	

	def __repr__(self):
		return f'Name(first={self.first}, last={self.last}, _middle={self._middle})'
	

class Player:
	def __init__(self, name: Name, balance: int):
		self.name = name
		self._balance = balance
		self._hand = initialize_empty_hand()


	def print_hand(self) -> None:
		"""
		Print the player's entire hand.
		"""
		if len(self._hand) == 0:
			stdio.writef("%s has no cards.\n", self.name.first)
		else:
			stdio.writef("%s's hand:\n", self.name.first)
			for i in range(len(self._hand)):
				if i != len(self._hand) - 1:
					stdio.writef("%s, ", self._hand[i])
				else:
					stdio.writef("%s\n", self._hand[i])


	def print_first(self) -> None:
		"""
		Print the player's top card.
		"""
		stdio.writeln(self._hand[0])


	def clear(self) -> None:
		"""
		Clear's the player's hand.
		"""
		# make sure _hand is good and gone before re-creating it
		del self._hand
		self._hand = initialize_empty_hand()


	def deal_card(self, deck: Deck) -> None:
		"""
		Deals one card from the deck using `Deck.deal_card()`.
		"""
		self._hand += [deck.deal_card()]


	def balance(self) -> int:
		"""
		Returns player's current balance.
		"""
		return self._balance
	

	def bet(self, amount: int) -> bool:
		"""
		Attempts to bet the specified amount.
		
		* If the player can afford the specified amount, the amount will be subtracted from the player's balance and will return True.
		* If the player *cannot* afford the specified amount, the player's balance will not change and will return False.

		Arguments
		---------
			amount (int): attempted bet amount

		Returns
		-------
			(bool) True if `_balance` >= `amount`, False if otherwise
		"""

		if amount >= self._balance:
			self._balance -= amount
			return True
		else:
			return False
		

	def win(self, pot: int):
		"""
		Adds specified pot value to player's balance for when they win.

		Arguments
		---------
			pot (int): value of the pot
		"""


	def hand_values(self) -> tuple[int, int]:
		"""
		Returns all possible current value(s) of the hand in an array of length 2^(count_aces).

		Returns
		-------
			(list[int]) all possible value(s) of the hand
		"""

		# grab the face names
		faces = [c.get_face() for c in self._hand]

		# calculate the total value of all cards that *are not* aces
		total_no_aces = sum([c.get_value() for c in self._hand if c.get_face() != 'Ace'])

		# count only the number of aces in the hand
		count_aces = len([f for f in faces if f == 'Ace'])

		possible_values: list[int] = stdarray.create1D(2^(count_aces), total_no_aces)


		# just hard-code it
		if count_aces == 0:
			# the total_no_aces is already in there, so just return it
			return possible_values
		
		elif count_aces == 1:
			possible_values = [
				total_no_aces + 1,
				total_no_aces + 11
			]
			return possible_values
		
		elif count_aces == 2:
			possible_values = [
				total_no_aces + 2,
				total_no_aces + 12,
				total_no_aces + 12,
				total_no_aces + 22
			]
			return possible_values
		
		elif count_aces > 2:
			raise NotImplementedError('AAH! Player has more than 2 aces! I don\'t know what to do with that yet!')
		
		else:
			# TODO: this error is... well, it can't be in the final code.
			raise Exception('Something done got fucky.')


	def is_blackjack(self) -> bool:
		"""
		Checks if the player's current hand is a natural Blackjack (two Aces).

		Returns
		-------
			(bool) True if player has two Aces, else False
		"""

		# count the number of Aces in the player's hand
		count_aces = len([f for c in self._hand if (f := c.get_face()) == 'Ace'])
		return True if count_aces == 2 else False

	
	def __repr__(self) -> str:
		return f"Player(name={self.name}, _balance={self._balance}, _hand={self._hand})"



def _tc():
	testDeck = Deck()
	p = Player(Name('Noah', 'Roberts'), 1000.0)
	p.deal_card(testDeck)
	p.deal_card(testDeck)
	p.print_hand()

	# manually add an Ace to check low/high card value func
	p._hand.append(Card('Spades', 'Ace'))
	# p.clear()
	p.print_hand()
	print(p.hand_values())
	print(p.is_blackjack())
	print(repr(p))

	p.clear()
	p._hand.append(Card('clubs', 'ace'))
	p._hand.append(Card('diAmondS', 'aCe'))
	print(p.hand_values())
	print(p.is_blackjack())
	

if __name__ == '__main__':
	_tc()