import stdio

class Book:
	def __init__(self, title='', author='', publisher='', copyright=''):
		self.title = title
		self.author = author
		self.publisher = publisher
		self.copyright = copyright

	def __str__(self):
		return f'''\
Title: {self.title}
Author: {self.author}
Publisher: {self.publisher}
Copyright: {self.copyright}\
		'''
	

def main():
	b1 = Book('Hello', 'Trish', 'Publisher', '2002')
	stdio.writeln(b1)
	stdio.writeln()

	b2 = Book()
	stdio.writeln(b2)
	stdio.writeln()


if __name__ == '__main__':
	main()
