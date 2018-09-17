"""
	Implementation of deep search in a binary tree. In this search approch, we use a stack to organize the elements to be covered. 
	Therefore, we did not use a explicit stack, instead we use the implict function call stack.
"""

import numpy as np

# When the element is find, this var is set to 1, blocking new iterations and exiting the recursion
find = 0

## Each node is represented by a class
class node():
	def __init__(self, value=None):
		self.value = value
		self.visited = 0

		self.left = None
		self.right = None

def deepSearch(list, element):
	print("oi :)")

# Show the entire tree if 'searched' == None (Walks in Root-Left-Right). If 'searched' != None, the walk stop when the current 
# node is equal to searched. The function call stack is the trick for deep seach
def showTree(tree, searched = None):
	global find

	print("Nodo: " + tree.value)
	if searched != None and tree.value == searched:
		print("Element finded. Exiting...")
		find = 1

	if tree.left != None and find == 0:
		showTree(tree.left, searched = searched)
	if tree.right != None and find == 0:
		showTree(tree.right, searched = searched)


# Define our tree as linked objects. Then, put some edges
def makeTree(graph):
	
	nodeA = node("A")
	head = nodeA

	nodeB = node("B")
	nodeI = node("I")
	head.left = nodeB
	head.right = nodeI

	nodeC = node("C")
	nodeD = node("D")
	nodeB.left = nodeC
	nodeB.right = nodeD

	nodeE = node("E")
	nodeF = node("F")
	nodeC.left = nodeE
	nodeC.right = nodeF

	nodeG = node("G")
	nodeH = node("H")
	nodeD.left = nodeG
	nodeD.right = nodeH	

	nodeJ = node("J")
	nodeK = node("K")
	nodeI.left = nodeJ
	nodeI.right = nodeK

	nodeL = node("L")
	nodeM = node("M")
	nodeJ.left = nodeL
	nodeJ.right = nodeM

	nodeN = node("N")
	nodeO = node("O")
	nodeK.left = nodeN
	nodeK.right = nodeO

	return head


def main():
	graph = 0

	# We use a linked list to represent our tree
	graph = makeTree(graph)
	#showTree(graph)

	# Let's search some value
	showTree(graph, searched = "D")


if __name__ == "__main__":
    main()


