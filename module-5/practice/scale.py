import stdio, stdarray


def rescale(a:list[float]) -> list[float]:
	scale = (min(a) + 1) / max(a)

	return [v * scale for v in a ]


def histogram(b:list[int], m:int) -> list[int]:
	freq = stdarray.create1D(m, 0)

	for val in b:
		freq[val] += 1
	
	return freq


def main():
	a1 = [0.0, 1.5, 6.0, 4.3]
	stdio.writef('a1: %s\n', rescale(a1))

	a2 = [0.1, 0.002, 0.4, 0.99]
	stdio.writef('a2: %s\n', rescale(a2))


	b1 = [6, 4, 5, 2, 6, 8, 4, 9, 6, 7, 3, 2, 2, 0, 8, 8, 5, 0, 9, 5, 8, 4, 5, 4, 2, 3, 0, 0, 9, 9, 7, 7, 7, 2, 5, 6, 8, 6, 5, 0, 8, 6, 9, 3, 5, 3, 0, 1, 6, 8, 6, 1, 4, 3, 6, 1, 6, 7, 2, 2, 6, 6, 0, 5, 4, 2, 4, 6, 3, 4, 7, 4, 5, 2, 6, 7, 5, 5, 1, 6, 9, 5, 3, 6, 1, 3, 4, 4, 5, 8, 5, 0, 8, 9, 6, 6, 8, 6, 7, 8]
	stdio.writef('b1: %s\n', histogram(b1, 10))

	b2 = [0, 9, 6, 1, 5, 9, 3, 6, 4, 9, 2, 5, 4, 7, 7, 5, 7, 8, 6, 0, 5, 6, 7, 1, 7, 0, 8, 2, 7, 8, 3, 9, 8, 1, 1, 3, 6, 0, 4, 0, 4, 9, 4, 1, 2, 4, 5, 4, 3, 3, 8, 3, 4, 7, 3, 0, 8, 6, 0, 5, 7, 9, 4, 1, 0, 2, 6, 4, 2, 8, 3, 7, 9, 2, 4, 2, 0, 3, 8, 1, 4, 0, 1, 4, 0, 1, 4, 8, 8, 0, 1, 3, 1, 8, 2, 6, 4, 0, 9, 6]
	stdio.writef('b2: %s\n', histogram(b2, 10))


if __name__ == '__main__':
	main()