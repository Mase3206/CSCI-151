
import picture, luminance, stdarray, random



def isAlreadyGrayscale(pic: picture.Picture) -> bool:
	randomX = stdarray.create1D(10, 0)
	randomY = stdarray.create1D(10, 0)

	for i in range(10):
		randomX.append(random.randint(0, pic.width))

	for i in range(10):
		randomY.append(random.randint(0, pic.height))

	
	for i in range(10):
		for j in range(10):
			same = stdarray.create1D(3, 0)
			comp = luminance.toGray(pic)

			same = [
				pic.get(randomX[i], randomY[j]).r == comp.get(randomX[i], randomY[j]).r,
				pic.get(randomX[i], randomY[j]).g == comp.get(randomX[i], randomY[j]).g,
				pic.get(randomX[i], randomY[j]).b == comp.get(randomX[i], randomY[j]).b
			]

			if same == [True, True, True]:
				return True
			else:
				return False
			
	

def toGrayscale(pic: picture.Picture) -> picture.Picture:
	for i in range(pic.width):
		for j in range(pic.height):
			pic.set(
				x=i,
				y=j,
				c=luminance.toGray(pic.get(
					x=i, y=j
				))
			)

	return pic

