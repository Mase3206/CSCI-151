# -----------------------------------------------------------------------------
# userargument.py
#
# Noah S. Roberts
# 01/22/2024
# Assignment 0
# for Week 2
# Excercise 1.1.6
# -----------------------------------------------------------------------------

import stdio, sys


class Message:
	def __init__(self, name1:str, name2:str, name3:str):
		# create the emtpy list to be used in a moment; could be more efficient, I know
		self.names = ['', '', '']
		
		# add the elements to the list
		self.names[0] = name1
		self.names[1] = name2
		self.names[2] = name3
		

	def make(self):
		# make the message with the names in the order they were given
		messageList = ['Hi ', self.names[0], ', ', self.names[1], ', and ', self.names[2], '. How are you?']		
		return messageList



def msg(name1, name2, name3):
	# Take three names as function arguments and return them in a sentence in reverse order
	message = Message(name3, name2, name1)
	stdio.writeln(''.join(message.make()))


def main():
	# Take three names as CLI arguments and return them in a sentence in reverse order
	message = Message(sys.argv[3], sys.argv[2], sys.argv[1])
	stdio.writeln(''.join(message.make()))



if __name__ == '__main__':
	# if calling directly from the CLI, run the main() function
    main()
