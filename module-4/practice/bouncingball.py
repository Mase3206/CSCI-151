import stddraw

# ---
# Draw a bouncing ball to stddraw
# ---

radius = 0.05
dt = 30.0

stddraw.setXscale(-1, 1)
stddraw.setYscale(-1, 1)

# position of center point
rx = 0.480
ry = 0.860

# velocity
vx = 0.030
vy = 0.046


while True:
	# update ball position and draw it there

	if abs(rx + vx) + radius > 1:
		vx = -vx

	if abs(ry + vy) + radius > 1:
		vy = -vy

	rx = rx + vx
	ry = ry + vy

	stddraw.clear(stddraw.GRAY)
	stddraw.filledCircle(rx, ry, radius)
	stddraw.show(dt)