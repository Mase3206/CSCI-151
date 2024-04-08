#!/usr/bin/env python3

"""
Practice BST code
03/04/2024
"""


class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


class BST:
	def __init__(self, root):
		self.root = root
		self.brances = (None, None)

	


def insert(node, rootNode):
	"""
	node: node to insert
	rootNode: root node
	"""
	
	try:
		if node == root:
			print("node already exists")
	except NameError:
		print("root node does not exist, creating")
		root = 'new_node'
		root.val = node.val
	



if __name__ == '__main__':
	root = 50
	insert(20, root)