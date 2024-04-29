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
	Name,
	load as playerLoad,
	save as playerSave
)



def initRoot() -> tuple[Deck, Player, Player]:
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
	dealer = Player(Name('Francis', 'McDealson'), math.inf)
	player = playerLoad()

	return deck, player, dealer



def game(deck: Deck, player: Player, dealer: Player):
	player.clear()
	dealer.clear()

	# bet
	player.bet()