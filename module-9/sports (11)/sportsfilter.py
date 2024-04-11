#!/usr/bin/env python3

# =============================================================================
# sportsfilter.py
#
# asdfadsf
#
# Noah S. Roberts
# 04.10.2024
# Assignment 11
# for Module 9
# Book Excercise ?????
# =============================================================================

from instream import InStream
from outstream import OutStream
import stdarray
from datetime import datetime as DateTime




def writeHeader():
	header = f"""
		Caitlin Clark Statistics - March Madness 2024

	{'Date':10s} {'Opp':20s} {'FG%':6s} {'3P':6s} {'3PA':6s} {'3P%':6.3s} {'AST':6s} {'PTS':6s}"""
	return header



class Game:
	"""
	Holds some stats about a specific player's performance from a specific basketball game.
	"""

	def __init__(self, gameData: dict[str, str | float | int]):
		self.date = str(gameData['Date'])
		self.opponent = str(gameData['Opp'])
		self.percent_FG = float(gameData['FG%'])
		self.count_3P = int(gameData['3P'])
		self.count_3PA = int(gameData['3PA'])
		self.percent_3P = float(gameData['3P%'])
		self.assists = int(gameData['AST'])
		self.points = int(gameData['PTS'])


	def formatLine(self) -> str:
		# return "%10s %20s %6.3f %6d %6d %6.3f %6d %6d"
		return f'\t{self.date:10s} {self.opponent:20s} {self.percent_FG:6.3f} {self.count_3P:6d} {self.count_3PA:6f} {self.percent_3P:6.3f} {self.assists:6d} {self.points:6d}'



def extractData(csvLine: str) -> Game:
	a = csvLine.split(',')
	data = {
		'Date': a[0],
		'Opp': a[2],
		'FG%': a[7],
		'3P': a[11],
		'3PA': a[12],
		'3P%': a[13],
		'AST': a[20],
		'PTS': a[25]
	}
	return Game(data)



def main(filename:str):
	data = InStream(filename)
	lineList: list[str] = data.readAllLines()[1:]

	output = OutStream() #('offense.txt')
	output.writeln(writeHeader())
	for line in lineList:
		output.writeln(extractData(line).formatLine())



if __name__ == '__main__':
	import sys
	main(sys.argv[1])