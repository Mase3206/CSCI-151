import stdio
import stddraw

x0 = stdio.readFloat()
y0 = stdio.readFloat()
x1 = stdio.readFloat()
y1 = stdio.readFloat()

stddraw.setXscale(x0, x1)
stddraw.setXscale(y0, y1)

stddraw.setPenRadius(0.0)

while not stdio.isEmpty():
	x = stdio.readFloat()
	y = stdio.readFloat()
	stddraw.point(x, y)

stddraw.show()