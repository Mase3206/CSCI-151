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

import stdio	# type: ignore
import stdarray	# type: ignore

from card import Card
from deck import Deck, initialize_empty_deck

import pickle


# define saved player file name as a Rust-style constant
PLAYER_DATA_FILE = 'player.dat'



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
		"""
		Return middle name if given when initialized. If given is length 1 or Name.middle() is called with initial=True, returned value is an initial. If not, returned value is the full middle name

		Arguments
		---------
			initial (bool; default False): return middle name as initial. ex: "A. "
		
		Returns
		-------
			(str) middle name or initial
		"""

		if self._middle == '':
			return ''
		elif len(self._middle) == 1 or initial == True:
			return f'{self._middle[0]}. '
		else:
			return f'{self._middle} '


	def fullName(self, useMiddleInitial=False):
		"""
		Return the full name. 

		Arguments
		---------
			useMiddleInitial (bool; default False): interpret middle name as an initial

		Returns
		-------
			(str) full name, including first, middle (if present), and last
		"""

		middle = self.middle(initial=useMiddleInitial)
		return f'{self.first} {middle}{self.last}'
	

	# special methods
	def __str__(self):
		return self.first
	
	def __repr__(self):
		return f'Name(first={self.first}, last={self.last}, _middle={self._middle})'
	


class Player:
	"""
	Player class used for Blackjack. Depends on card.py and deck.py.

	Arguments
	---------
		name (Name): player's name in a Name class (also defined in this file).
		balance (int): player's starting balance.	
	"""

	def __init__(self, name: Name, balance: int):
		self.name = name
		self._balance = balance
		# this says it initializes a deck, but it just creates a list of length 0 with type list[Card], which is used by both the player's hand and the deck.
		self._hand = initialize_empty_deck()


	def print_hand(self) -> None:
		"""
		Print the player's entire hand.
		"""
		if len(self._hand) == 0:
			stdio.writef("\n%s has no cards.\n", self.name)
		else:
			stdio.writef("\n%s's hand:", self.name)
			for i in range(len(self._hand)):
				if i != len(self._hand) - 1:
					stdio.writef("%s, ", self._hand[i])
				else:
					stdio.writef("%s\n", self._hand[i])


	def print_first(self) -> Card:
		"""
		Prints and returns the player's top card.

		Returns
		-------
			(Card) the Player's top card
		"""
		
		stdio.writef("\n%s's top card: %s\n", self.name, self._hand[0])
		return self._hand[0]


	def clear(self) -> None:
		"""
		Clear's the player's hand. Used at the end of each game and before saving the user's name and balance.
		"""
		# make sure _hand is good and gone before re-creating it
		del self._hand
		self._hand = initialize_empty_deck()


	def deal_card(self, deck: Deck) -> None:
		"""
		Deals one card from the deck using `Deck.deal_card()`.

		Arguments
		---------
			deck (Deck): the deck to deal a card from
		"""
		self._hand.append(deck.deal_card())


	def balance(self) -> int:
		"""
		Returns player's current balance. It's a pointless method that could be eliminated, but I digress.

		Returns
		-------
			(int) Player's balance
		"""
		return self._balance
	

	def bet(self) -> int:
		"""
		Prompts the Player to enter their bet, then attempts attempts to bet the entered amount. If the Player's balance is not enough for the bet, they will automatically bet their entire balance (all in).

		Returns
		-------
			(int) amount bet, or the all-in amount
		"""
		
		stdio.writef("Current balance: %i\n", self.balance())
		bet = int(input('Bet amount: '))

		# if the player does not have the funds to bet the input amount, automatically make an "all in" bet and set their balance to zero.
		if (newBal := self.balance() - bet) < 0:
			a = self.balance()
			self._balance = 0
			return a
		
		# if the player does have the funds, subtract the input amount from their balance and return the bet amount.
		else:
			self._balance = newBal
			return bet
		
		
	def win(self, winnings: int):
		"""
		Adds specified pot value to player's balance for when they win.

		Arguments
		---------
			winnings (int): value of the winnings. This is either 100% (win) or 150% (natural blackjack) the value of the pot.
		"""

		self._balance += winnings


	def best_hand_value(self) -> int:
		"""
		Returns the best value of the hand. It will try to find the highest possible value, accounting for all Aces, reverting to lower values if one or more Aces is present.

		Returns
		-------
			(int) best total value of the hand
		"""

		# count the number of aces in the hand
		qty_aces = len([c.face for c in self._hand if c.face == 'Ace'])

		# get the total of the hand without Aces (even if none are present)
		total_no_aces = sum([c.value for c in self._hand if c.face != 'Ace'])

		if qty_aces == 0:
			return total_no_aces
		
		elif self.is_blackjack():
			return 21

		elif qty_aces == 1:
			a = stdarray.create1D(2, 0)
			a = [
				total_no_aces + 1,
				total_no_aces + 11
			]

			for v in a:
				if v > 21:
					a.remove(v)
			
			# if an empty list is passed to max(), a ValueError will be thrown, so return lowest losing value
			if a == []:
				return total_no_aces + 1
			else:
				return max(a)
		
		elif qty_aces == 2:
			a = stdarray.create1D(3, 0)
			a = [
				total_no_aces + 2,
				total_no_aces + 12,
				total_no_aces + 22
			]

			for v in a:
				if v > 21:
					a.remove(v)
			
			# if an empty list is passed to max(), a ValueError will be thrown, so return lowest losing value
			if a == []:
				return total_no_aces + 2
			else:
				return max(a)
		
		else:
			raise NotImplementedError('I haven\'t written the code to deal with 3 or more Aces in a hand.')


	def is_blackjack(self) -> bool:
		"""
		Checks if the player's current hand is a natural Blackjack: first two cards are an Ace and a 10.

		Returns
		-------
			(bool)
		"""

		# account for both permutations
		if self._hand[0].face == 'Ace' and self._hand[1].face == 'Ten':
			return True
		elif self._hand[0].face == 'Ten' and self._hand[1].face == 'Ace':
			return True
		else:
			return False


	# special methods
	def __repr__(self) -> str:
		return f"Player(name={self.name}, _balance={self._balance}, _hand={self._hand})"



class Dealer(Player):
	"""
	Dealer class with base class Player. It has no arguments. It does have a few modified methods:

	Modified methods
	----------------
		print_first(): The `name` field is automatically filled in as "Dealer".
	"""

	# all methods that aren't defined here are inherited from Player

	def __init__(self):
		self._hand = initialize_empty_deck()
		self.name = Name('Francis', 'McDealson')
		self.balance = float('inf')


	def print_first(self) -> Card:
		"""
		Prints and returns the player's top card.
		"""

		# changes this method to print "Dealer" instead of f"{str(self.name)}
		stdio.writef("\nDealer's top card: %s\n", self._hand[0])
		return self._hand[0]
	
	
	def value_first(self) -> int:
		"""
		Simple method to return the value of the Dealer's top card.
		"""
		return self._hand[0].value
	

	# special methods
	def __repr__(self) -> str:
		return f"Player(name={repr(self.name)}, _balance={self._balance}, _hand={self._hand})"
	


def load() -> Player:
	"""
	Load the Player object: try loading from file (if exists) and return it; if not, create Player and return it.

	Returns
	-------
		(Player) new or previously-saved Player object
	"""
	try:
		with open(PLAYER_DATA_FILE, 'rb') as f:
			stdio.writeln('Found existing player data. Loading...\n')
			return pickle.load(f)

	except FileNotFoundError:
		stdio.writeln('Existing player data not found. Creating a new player...')
		return Player(
			name=Name(
				input('First name: '),
				input('Last name: ')
			),
			balance=1000
		)
	


def save(player: Player):
	"""
	Save the Player in the PLAYER_DATA_FILE global constant specified in player.py (should be 'player.dat'), creating the file if not present.

	Arguments
	---------
		player (Player): Player object to save
	"""
	
	try:
		# does it exist?
		open(PLAYER_DATA_FILE, 'rb').close()

		# if exist, write to it
		with open(PLAYER_DATA_FILE, 'wb') as f:
			player.clear()
			pickle.dump(player, f)
		
	# if no exist, make it
	except FileNotFoundError:
		# make file
		open(PLAYER_DATA_FILE, 'wb').close()
		
		# write to file
		with open(PLAYER_DATA_FILE, 'wb') as f:
			player.clear()
			pickle.dump(player, f)



def _tc():
	"""
	Test client; not part of API.
	"""
	testDeck = Deck()
	p = Player(Name('Noah', 'Roberts'), 1000.0)
	p._hand.append(Card('Spades', 'Ten'))
	p._hand.append(Card('Spades', 'Ace'))
	print(p.is_blackjack())

	p.clear()
	p._hand.append(Card('Spades', 'Five'))
	p._hand.append(Card('Spades', 'Ace'))
	print(p.best_hand_value())

	p._hand.append(Card('Spades', 'Ace'))
	print(p.is_blackjack())
	print(p.best_hand_value())
	

if __name__ == '__main__':
	_tc()
