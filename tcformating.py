def section(text: str):
	"""
	Test client output section. Format example:
	```
————————————————————————————————————
 * Printing final account details * 
————————————————————————————————————
	```
	"""
	bar = ''.join(['—'] * (len(text) + 6))
	return f'\n\n{bar}\n * {text} * \n{bar}'



def subsection(text: str):
	"""
	Test client output sub-section. Format example:
	```

 * Testing valid transfer * 
————————————————————————————
	```
	"""
	bar = ''.join(['—'] * (len(text) + 6))
	return f'\n * {text} * \n{bar}'