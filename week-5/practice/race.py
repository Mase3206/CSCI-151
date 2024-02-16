import stddraw, random, stdio



frameTime = 0.1  # in ms

# set race rules
laps = 3
baseSpeed = 0.01
variance = 0.1  # percent difference between base speed and random variation speed

# set car properties
carRadius = 0.1

car1_color = stddraw.BLUE
car2_color = stddraw.RED

car1_xloc = -2
car2_xloc = -2

car1_yloc = 1 - (2 / 3)
car2_yloc = -1 + (2 / 3)


stddraw.setXscale(-1, 1)
stddraw.setYscale(-1, 1)

car1_i = 0
car2_i = 0
while True:
	stddraw.clear()

	# draw car1
	stddraw.setPenColor(car1_color)
	stddraw.filledCircle(car1_xloc, car1_yloc, carRadius)

	# draw car2
	stddraw.setPenColor(car2_color)
	stddraw.filledCircle(car2_xloc, car2_yloc, carRadius)

	# show frame
	stddraw.show(frameTime)


	# set new location with a bit of randomness in its speed
	car1_xloc = car1_xloc + (random.random() * variance) + baseSpeed
	car2_xloc = car2_xloc + (random.random() * variance) + baseSpeed

	# if car1 is at the right edge of the screen, snap it to the left and increment its lap counter
	if car1_xloc + carRadius > 1:
		car1_xloc = -1 - carRadius
		car1_i += 1

		# if car1 finishes first, break.
		if car1_i >= laps:
			break

	# if car2 is at the right edge of the screen, snap it to the left and increment its lap counter
	if car2_xloc + carRadius > 1:
		car2_xloc = -1 - carRadius
		car2_i += 1

		# if car2 finishes first, break.
		if car2_i >= laps:
			break


if car1_i > car2_i:
	stdio.writeln("Car 1 wins!")
elif car1_i < car2_i:
	stdio.writeln("Car 2 wins!")
else:
	stdio.writeln("Tie!")