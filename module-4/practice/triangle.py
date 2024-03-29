import stddraw, math


# draw a triangle and a point in the middle of the triangle
t = math.sqrt(3.0) / 2.0

stddraw.line(0.0, 0.0, 1.0, 0.0)
stddraw.line(1.0, 0.0, 0.5, t)
stddraw.line(0.5, t, 0.0, 0.0)
stddraw.point(0.5, t/3.0)
stddraw.show()