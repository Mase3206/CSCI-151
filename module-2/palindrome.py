#!/usr/bin/env python3

# =============================================================================
# palindrome.py
#
# Give it a word, phrase, or sentence, and it will determine if it is a 
# palindrome and what kind it is.
#
# Noah S. Roberts
# 01/29/2024
# Section 1
# for Week 3
# Book Excercise ?
# =============================================================================

import stdio, sys


# Strip the punctuation from the message
# Only called if palindrome is inexact
def stripPunct(message:list):
	"""
	Strip punctuation
	=================
	Strips the punctuation characters from the given message list

	Argument
	--------
		`message` : list of characters that may contain punctuation

	Return
	------
		list of only non-punctuation characters
	"""
	punct = [',', '.', ':', ';', "'", '"', '!', '?', '/', '\\', ' ', '-', '–', '—']
	punctless = []

	for char in message:
		if char not in punct:
			punctless.append(char)

	return punctless
	

# Checks if the message is an inexact palindrome
def isInexactPalindrome(message:list):
	"""
	Test - Inexact Palindrome
	=========================
	Tests if the message list is an inexact palindrome by stripping the punctuation characters and comparing its reverse. If any character is different in the reverse, it returns False. If all are identical in the reverse, it returns True.

	Argument
	--------
		`message` : list of characters

	Return
	------
		bool : True if all `messagePunctless[i]` and `reversedPunctless[i]` are identical
	"""
	punctless = stripPunct(message)
	reverse = list(reversed(punctless))

	for i in range(len(punctless)):
		if punctless[i] != reverse[i]:
			return False
	
	# this should only execute if punctless[i] != reverse[i] is never True
	return True


# Checks if the message is an exact palindrome
# If not, it passes the message off to isInexactPalindrome()
def isExact(message:list):
	"""
	Test - Exact Palindrome
	=======================
	Tests if the message list is an exact palindrome by iterating through the reverse of the message, including the punctuation. If any character is different in the reverse, it marks return dict key "isExact" False and passes the message off to `isInexactPalindrome(message)`. If all characters are identical in the reverse, both keys in the return dict are True.
	
	Argument
	--------
		`message` : list of characters

	Return
	------
		dict : key[0] = return of `isInexactPalindrome(message)` or False; key[1] = True if all `message[i]` and `reversed[i]` are identical
	"""
	reverse = list(reversed(message))

	for i in range(len(message)):
		if message[i] != reverse[i]:
			return {
				"isPalindrome": isInexactPalindrome(message),
				"isExact": False
			}

	return {
		"isPalindrome": True,
		"isExact": True
	}
	

# Can be called via import or directly via CLI from if __name__ == '__main__'
def test(messageStr:str):
	messageList = list(messageStr.lower())

	return isExact(messageList)




if __name__ == '__main__':
	testString = sys.argv[1]
	palindromeType = test(testString)

	if palindromeType["isPalindrome"]:
		if palindromeType["isExact"]:
			stdio.writeln('This is a palindrome.')
		else:
			stdio.writeln('This is an inexact palindrome.')
	else:
		stdio.writeln('Sorry, this is not a palindrome.')
