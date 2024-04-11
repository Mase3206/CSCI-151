from outstream import OutStream

columnIndex = [0, 2, 7, 11, 12, 13, 20, 25]
columnWidth = [10, 20, 8, 8, 8, 8, 8, 8]

out = OutStream()

data = [
	'4/1/2024,Iowa,Louisiana State,W 94-87,40,13,29,0.448,4,9,0.444,9,20,0.45,6,7,0.857,2,5,7,12,2,1,5,2,41', 
	'3/30/2024,Iowa,Colorado,W 89-68,36,13,22,0.591,10,11,0.909,3,11,0.273,0,0,,0,6,6,15,1,1,2,3,29', 
	'3/25/2024,Iowa,West Virginia,W 64-54,40,8,22,0.364,3,8,0.375,5,14,0.357,11,12,0.917,0,8,8,3,2,0,6,1,32', 
	'3/23/2024,Iowa,Holy Cross,W 91-65,32,8,19,0.421,5,10,0.5,3,9,0.333,8,9,0.889,1,7,8,10,3,1,6,3,27', 
	'3/10/2024,Iowa,Nebraska,W 94-89 (OT),44,12,29,0.414,7,12,0.583,5,17,0.294,5,6,0.833,2,5,7,12,3,0,7,3,34'
]

newData = []
for d in data:
	asd = d.split(',')

	for i in range(len(columnIndex)):
		b = asd[columnIndex[i]]
		out.write(f'{b:>{columnWidth[i]}s}')

	print()
