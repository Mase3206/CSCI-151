#!/usr/bin/env python3

import stdio, sys


# Strip the punctuation from the message
# Only called if palindrome is inexact
def stripPunct(message:list):
	punct = [',', '.', ':', ';', "'", '"', '!', '?', '/', '\\', ' ', '-', '–', '—']
	punctless = []

	for char in message:
		if char not in punct:
			punctless.append(char)

	return punctless
	

# Checks if the message is an inexact palindrome
def isInexactPalindrome(message:list):
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
