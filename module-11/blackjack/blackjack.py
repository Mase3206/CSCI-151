#!/usr/bin/env python3

# =============================================================================
# blackjack.py
#
# Blackjack game.
#
# Noah S. Roberts
# 04.22.2024
# Assignment 13
# for Module 11
# =============================================================================

import math

import stdio	# type: ignore
import stdarray	# type: ignore

from card import Card
from deck import Deck
from player import (
	Player,
	Dealer,
	Name,
	load as playerLoad,
	save as playerSave
)



def initRoot() -> tuple[Deck, Player, Dealer]:
	"""
	Initializes the root of the program:
	* Creates the deck
	* Creates the dealer Player object
	* Loads the player Player object via player.load()

	Returns
	-------
		tuple: deck, player, dealer
	
	"""
	deck = Deck()
	dealer = Dealer()
	player = playerLoad()

	return deck, player, dealer



def reset(player: Player, dealer: Dealer) -> tuple[Deck, Player, Dealer]:
	"""
	Reset the deck, dealer's hand, and player's hand for the next game.
	"""

	deck = Deck()
	dealer.clear()
	player.clear()

	return deck, player, dealer



def game(
		deck: Deck, 
		player: Player, 
		dealer: Dealer
	):
	"""
	Main gameloop.	
	"""

	player.clear()
	dealer.clear()

	# bet
	pot = player.bet() * 2

	# deal cards
	player.deal_card(deck)
	player.deal_card(deck)
	dealer.deal_card(deck)
	dealer.deal_card(deck)

	player.print_hand()
	stdio.writef('Best value: %i\n', player.best_hand_value())

	dealer.print_first()
	stdio.writef('Known value: %i', dealer.value_first())


	deck, player, dealer = round(deck, player, dealer)
	p = player.best_hand_value()
	d = dealer.best_hand_value()

	if player.is_blackjack():
		# win: natural blackjack
		player.win(int(pot * 1.5))
		stdio.writef("\n%s wins with a natural Blackjack!\n", player.name)
		return deck, player, dealer

	elif p > 21:
		# lose: player over 21
		stdio.writef("\n%s loses from going over 21!\n", player.name)
		return deck, player, dealer

	elif d > 21:
		# win: dealer over 21
		player.win(pot)
		stdio.writef("\n%s wins from the dealer's hand going over 21!\n", player.name)
		return deck, player, dealer

	elif p > d:
		# win: player greater than dealer
		player.win(pot)
		stdio.writef("\n%s wins with a hand less than 21 and greater than the dealer's!\n", player.name)
		return deck, player, dealer

	elif p < d:
		# lose: player less than dealer
		stdio.writef("\n%s loses with a hand less than 21 but less than the dealer's!\n", player.name)
		return deck, player, dealer

	elif p == d:
		# bust: player equal to dealer
		stdio.writef("\n%s busts with a hand equal to the dealer's!\n", player.name)
		player.win(pot // 2)
		return deck, player, dealer

	


	


def round(
		deck: Deck,
		player: Player,
		dealer: Dealer
	):
	"""
	One round of Blackjack. In each round, the player can choose to Hit or Stand.
	"""


	choice = input("\n(h) Hit or (s) Stand? ")
	# stand
	if choice.lower() == 's':
		while True:
			if dealer.best_hand_value() > 17:
				break
			dealer.deal_card(deck)
		return deck, player, dealer

	# hit
	elif choice.lower() == 'h':
		player.deal_card(deck)
		player.print_hand()
		hv = player.best_hand_value()
		# if player's hand value is over 21
		if hv > 21:
			return deck, player, dealer
		else:
			stdio.writef('Best value with new card: %i\n', hv)

			dealer.print_first()
			stdio.writef('Known value: %i', dealer.value_first())

			# it's all done recursively
			return round(deck, player, dealer)


def main():
	deck, player, dealer = initRoot()

	while True:
		# we can initialize and start the game on one line by unpacking the output of initRoot()
		deck, player, dealer = game(deck, player, dealer)

		cont = input('\nWould you like to play another game? [Y/n] ').lower()
		if cont == 'y' or cont == '':
			continue
		else:
			save = input('Would you like to save your balance to be used later? This will create a `player.dat` file in your current directory. [Y/n] ').lower()
			if save == 'y' or save == '':
				stdio.writeln('Saving...')
				playerSave(player)
				exit(0)
			else:
				exit(0)


try:
	main()
except KeyboardInterrupt:
	stdio.writeln('\nForce quit!')
	exit(1)
