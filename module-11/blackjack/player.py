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

# Player(name, balance)	# Create a player with a name, balance and hand
# p.print_hand()			# Prints player’s hand
# p.print_first()			# Prints only first card of player’s hand
# p.clear()				# Clears player’s hand
# p.deal_card(d)			# Adds a card to players hand from deck d
# p.print_balance()		# Prints the player’s balance
# p.get_balance()			# Returns the player’s balance
# p.bet(amount)			# Returns True and subtracts amount from player’s balance if player’s balance >= amount, Returns False otherwise
# p.win(amount)			# Adds amount to player’s balance
# p.blackjack_hand_value()	# Returns value of blackjack hand
# p.blackjack()			# Returns True if hand is a blackjack