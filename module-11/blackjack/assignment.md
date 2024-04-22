---
due: 26-04-2024 21:59:00.00 -6
---

# Assignment #13 - Blackjack


## Problem Statement

Create your own version of the popular game "Blackjack".  

### Assignment Details

- There will only be one player and the dealer
- Create a Card, Deck and Player data-type (PURPOSE OF THIS ASSIGNMENT!!!!)
- Provide documentation strings (or docstrings) for your Card, Deck and Player data-types.  
- Cards must be reshuffled if deck size is less than 20
- Aces can be either 1 or 11 points
- A tie is a push – nobody wins or loses
- Dealer stands on soft 17
- Winnings
	- Your score beats dealer’s score – 1:1 payout ratio. (100% increase of your initial bet)
	- Dealer’s score beats your score – 1:1 loss ratio. (100% decrease of your initial bet)
	- Natural Blackjack (A in two. Auto Win unless dealer has a blackjack, then a push) – 3:2 payout ratio. (150% increase of your initial bet.)


## How to play Blackjack

### Object of the Game

Each participant attempts to beat the dealer by getting a count as close to 21 as possible, without going over 21.

### Card Values/Scoring

It is up to each individual player if an ace is worth 1 or 11. Face cards are 10 and any other card is its pip value.

### Betting

Before the deal begins, each player places a bet, in chips, in front of him in the designated area.

### The Deal

When all the players have placed their bets, the dealer gives one card face up to each player in rotation clockwise, and then one card face up to himself. Another round of cards is then dealt face up to each player, but the dealer takes his second card face down. Thus, each player except the dealer receives two cards face up, and the dealer receives one card face up and one card face down.

### Naturals

If a player's first two cards are an ace and a "ten-card" (a picture card or 10), giving him a count of 21 in two cards, this is a natural or "blackjack." If any player has a natural and the dealer does not, the dealer immediately pays that player one and a half times the amount of his bet. If the dealer has a natural, he immediately collects the bets of all players who do not have naturals, (but no additional amount). If the dealer and another player both have naturals, the bet of that player is a stand-off (a tie), and the player takes back his chips.

If the dealer's face-up card is a ten-card or an ace, he looks at his face-down card to see if the two cards make a natural. If the face-up card is not a ten-card or an ace, he does not look at the face-down card until it is the dealer's turn to play.

### The Play

The player to the left goes first and must decide whether to "stand" (not ask for another card) or "hit" (ask for another card in an attempt to get closer to a count of 21, or even hit 21 exactly). Thus, a player may stand on the two cards originally dealt him, or he may ask the dealer for additional cards, one at a time, until he either decides to stand on the total (if it is 21 or under), or goes "bust" (if it is over 21). In the latter case, the player loses and the dealer collects the bet wagered. The dealer then turns to the next player to his left and serves him in the same manner.

The combination of an ace with a card other than a ten-card is known as a "soft hand," because the player can count the ace as a 1 or 11, and either draw cards or not. For example with a "soft 17" (an ace and a 6), the total is 7 or 17. While a count of 17 is a good hand, the player may wish to draw for a higher total. If the draw creates a bust hand by counting the ace as an 11, the player simply counts the ace as a 1 and continues playing by standing or "hitting" (asking the dealer for additional cards, one at a time).

### The Dealer's Play

When the dealer has served every player, his face-down card is turned up. If the total is 17 or more, he must stand. If the total is 16 or under, he must take a card. He must continue to take cards until the total is 17 or more, at which point the dealer must stand. If the dealer has an ace, and counting it as 11 would bring his total to 17 or more (but not over 21), he must count the ace as 11 and stand. The dealer's decisions, then, are automatic on all plays, whereas the player always has the option of taking one or more cards.

### Settlement

A bet once paid and collected is never returned. Thus, one key advantage to the dealer is that the player goes first. If the player goes bust, he has already lost his wager, even if the dealer goes bust as well. If the dealer goes over 21, he pays each player who has stood the amount of that player's bet. If the dealer stands at 21 or less, he pays the bet of any player having a higher total (not exceeding 21) and collects the bet of any player having a lower total. If there is a stand-off (a player having the same total as the dealer), no chips are paid out or collected.

[24.7 BLACKJACK](https://www.247blackjack.com/) seems to be a good site to get some practice playing the game!


## Suggested APIs


```python
Card(suit, face, value)	# Create a card
c.get_value()			# Returns an integer indicating value of card
c.set_value(v)			# Sets the value of card to v
str(c)					# Example:  Two of Hearts

Deck()					# Create a shuffled deck of 52 cards
d.print_deck()			# Method was added for test client
d.deal()				# Returns and removes card from deck
d.deck_size()			# Returns size of deck

Player(name, balance)	# Create a player with a name, balance and hand
p.print_hand()			# Prints player’s hand
p.print_first()			# Prints only first card of player’s hand
p.clear()				# Clears player’s hand
p.deal_card(d)			# Adds a card to players hand from deck d
p.print_balance()		# Prints the player’s balance
p.get_balance()			# Returns the player’s balance
p.bet(amount)			# Returns True and subtracts amount from player’s balance if player’s balance >= amount, Returns False otherwise
p.win(amount)			# Adds amount to player’s balance
p.blackjack_hand_value()	# Returns value of blackjack hand
p.blackjack()			# Returns True if hand is a blackjack
```


## Programming Concepts

- Designing Data Types
- Creating Data Types


## Discussion of Topic

This assignment focuses on developing APIs as a critical step in the development of any program. We need to consider various alternatives, understand their impact on both client programs and implementations, and refine the design to strike an appropriate balance between the needs of clients and the possible implementation strategies.


## Directions

- Write your program in IDLE
- Save your programs as blackjack.py, card.py, deck.py and player.py
- Create a header
- Make appropriate comments 
- Create variables with descriptive names
- Create test clients in card.py, deck.py and player.py 
- Provide appropriate help documentation
- You will arrange to do a live demo with Trish/TA during the week of April 29th, 2024

