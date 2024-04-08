import barcode, random


count = 100
ft = 50

for i in range(count):
	if random.randint(0, 1):
		barcode.drawUBC(f'{random.randint(0, 99999)}', frametime=ft)
	else:
		barcode.drawUBC(f'{random.randint(0, 99999)}-{random.randint(0, 9999)}', frametime=ft)