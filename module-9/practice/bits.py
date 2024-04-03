import stdio


x = 3 ** 3
stdio.writeln(x)

bits = x.bit_length()
stdio.writeln(bits)

s = bin(x)
stdio.writeln(s)

f = int(s, base=2)
stdio.writeln(f)