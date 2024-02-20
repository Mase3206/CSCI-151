# -----------------------------------------------------------------------------
# userargument-simple.py
#
# This is the simpler version that is much easier to understand at a quick
# glance.
#
# Noah S. Roberts
# 01/22/2024
# Assignment 0
# for Week 2
# Excercise 1.1.6
# -----------------------------------------------------------------------------

import stdio, sys

# Take three names as CLI arguments and return them in a sentence in reverse order
messageList = ['Hello, ', sys.argv[3], ', ', sys.argv[2], ', and ', sys.argv[1], '. How are you?']
stdio.writeln(''.join(messageList))
