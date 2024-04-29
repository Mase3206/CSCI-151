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
import pickle

import stdarray  # type: ignore
import stdio  # type: ignore
from deck import Deck
from player import Name, Player


# global constants, Rust-style
PLAYER_DATA_FILE = 'player.dat'



def winCheck(player: Player, dealer: Player) -> bool:
	"""
	Check if player wins round by checking player and dealer hand values. 

	1. If natural blackjack, player automatically wins. 
	2. If player over 21, dealer wins.
	3. If dealer over 21, player wins.
	4. If both over 21, neither wins (tie, a.k.a. "push")
	"""

	playerValues = player.hand_values()
	dealerValues = dealer.hand_values()
	# playerUnder = stdarray.create1D(0)
	# dealerUnder = stdarray.create1D(0)

	if player.is_blackjack():
		return 'player'
	else:
		playerUnder = [v for v in playerValues if v <= 21]
		dealerUnder = [v for v in dealerValues if v <= 21]

		if len(playerUnder) == 0 and len(dealerUnder) == 0:
			return 'push'
		elif len(playerUnder) > len(dealerUnder):
			return 'player'
		elif len(playerUnder) < len(dealerUnder):
			return 'dealer'
		elif len(playerUnder) == len(dealerUnder):
			return 'no winner'
		else:
			raise Exception('This should never run!')





def round(player: Player, dealer: Player, deck: Deck):
	"""
	Single round. 

	Stand
	-----
	1. Draw card
	2. Check hand value. 
	3. If natural blackjack, automatically win. 
	4. If over 21, go to WIN_CHECK.
	 
	Call
	----
	1. Run winCheck().
	"""

	player.deal_card(deck)
	player.deal_card(deck)
	player.print_hand()

	dealer.deal_card(deck)
	dealer.deal_card(deck)
	dealer.print_first()


	choice = input('(1) stand, (2) call, or (q) quit? ')

	if choice.lower() == 'q':
		return 'user_exit'
	elif choice == '1':
		"stand"
	elif choice == '2':
		"call"
	



def game():
	"""
	Main game loop.
	"""
	return



def loadPlayer():
	"""
	Load Player object. 

	It will first try to load an existing Player from PLAYER_DATA_FILE. If the file is not found, it will prompt the user to enter their first and last name to initialize the Player. It then returns either the existing or new Player object.

	Returns
	-------
		(Player) player object 
	"""

	try:
		with open(PLAYER_DATA_FILE, 'rb') as f:
			# try to load existing data
			existingData: Player = pickle.load(f)
			useExisting = input('Found existing player data. Would you like to use it? [Y/n] ')
			if useExisting.lower() == 'y' or useExisting == '':
				player = existingData
				player.clear()
	
	except FileNotFoundError:
		# create new dat file
		open(PLAYER_DATA_FILE, 'a').close()

		# get the new player's data
		stdio.writeln('Existing player data not found.')
		playerName = Name(
			first=input("What's your first name? "),
			last=input("What's your last name? ")
		)
		stdio.writeln('Creating new player with default balance of $1000.')
		player = Player(playerName, 1000)

		# save that data
		savePlayer(player)
	
	return player



def savePlayer(player: Player):
	"""
	Save the Player object to PLAYER_DATA_FILE.

	Arguments
	---------
		player (Player): player object to save
	"""

	# this'll only work if the file already exists (which it should)
	with open(PLAYER_DATA_FILE, 'wb') as f:
		pickle.dump(player, f)



def main():
	# load player data
	deck = Deck()
	player = loadPlayer()
	dealer = Player(Name('Francis', 'McDealson'), math.inf)

	while True:
		round(player, dealer, deck)



# def _tc():
# 	stdio.writeln('Success!')

# if __name__ == '__main__':
# 	_tc()


main()
