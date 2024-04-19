import stdarray
import stdio
from book import Book
from instream import InStream


class Library: 
	def __init__(self, fileName: str):
		lines = InStream(fileName).readAllLines()
		self._lib: list[Book] = stdarray.create1D(len(lines) // 4)

		for group in range(len(lines) // 4):
			self._lib[group] = Book(
				lines[(group * 4) + 0],
				lines[(group * 4) + 1],
				lines[(group * 4) + 2],
				lines[(group * 4) + 3]
			)

	
	def print(self):
		stdio.writef('The library has %i books:\n\n', len(self._lib))
		for a in self._lib:
			stdio.writef("%s\n\n", a)

	
	def booksBy(self, author):
		temp = stdarray.create1D(0)
		
		for b in self._lib:
			if b.author == author:
				temp.append(b)
		
		stdio.writef('%s has written %i books:\n\n', author, len(temp))
		for b in temp:
			stdio.writef('%s\n\n', b)


# lines = InStream('books.txt').readAllLines()
# library = Library(stdarray.create1D(len(lines) // 4))


# for group in range(len(lines) // 4):
# 	library[group] = Book(
# 		lines[(group * 4) + 0],
# 		lines[(group * 4) + 1],
# 		lines[(group * 4) + 2],
# 		lines[(group * 4) + 3]
# 	)


# stdio.writef('The library has %i books:\n\n', len(library))

# for a in library:
# 	stdio.writef("%s\n\n", a)


def _test():
	lib = Library('books.txt')
	lib.print()
	lib.booksBy('Trish Duce')


_test()
