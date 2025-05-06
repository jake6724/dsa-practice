from MyQueue import Queue

class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

# A binary tree does not need an actual data structure to maintain it
# Simply connecting nodes in the binary tree pattern will suffice 
# I'll make a class just to contain everything and cause I want to

class BinaryTree:
	def __init__(self, data):
		self.root = Node(data)

	"""
	General notes for depth-first traversal algorithms:
	These algos are all recursion based and follow a simple pattern:
		1. Check if the current node is None. If so, you're done and can return (Just an empty return statement)
		2. Recurse and print in the order you want to check all the nodes
			- If you want to go left, root, right then do that here
			ex. 
			recursive_func(node.left)
			print(node.data)
			recursive_func(node.right) 
			
			- This will go through all the left nodes on the left side of the tree and as they return they will print 
			their data. After their done, they will print their right sides

			- After this, the root will print. 

			- Then the right side will follow the same process as left
	"""

	def height(self, node) -> int:
		if not node: # When the node doesn't exist, height is 0
			return 0
		left = self.height(node.left)
		right = self.height(node.right)
		return max(left, right) + 1 # Height is the tallest subtree + 1 (for the current node)

	# Pre-order traversal starts at root, goes thru left, then goes thru right for the tree and each sub-tree
	def print_preorder_traversal(self, node):
		if node is None:
			return 
		print(node.data, end=' ')
		self.print_preorder_traversal(node.left)
		self.print_preorder_traversal(node.right)
	
	# Inorder traversal will print from left to right, starting at the left-most leaf node. 
	def print_inorder_traversal(self, node):
		if node is None:
			return 
		self.print_inorder_traversal(node.left)
		print(node.data, end=' ')
		self.print_inorder_traversal(node.right)

	# Post-order traversal visits left, then right, then root
	def print_postorder_traversal(self, node):
		if node is None:
			return 
		self.print_postorder_traversal(node.left)
		self.print_postorder_traversal(node.right)
		print(node.data, end=' ')

	"""
	General notes for Breadth-first traversal algorithms:
	The queue approach for BFS is simpler than it seems. By using a queue, we can add the children of the current node each
	time, but still ensure all the nodes are printed in the values they were accessed e.i., parents all accessed before 
	their children. This will allow us to traverse 1 level at a time. 
	"""

	def print_levelorder_traversal(self, node): # Breadth-first traversal (BFS)
		# Base case; nothing to do if empty tree
		if node is None:
			return 
		# Create the queue (just a basic list really that we are treating like a queue)
		# Start it with the root (or any node to start with)
		queue = []
		queue.append(node)

		while (len(queue) > 0):
			# Continuously grab the next in line and print its value. 
			print(queue[0].data, end=" ") 
			current_node = queue.pop(0)
			
			# Take the current node and add its 2 children. It will only add these 2 (and a node should never have more)
			if current_node.left is not None:
				queue.append(current_node.left)
			if current_node.right is not None:
				queue.append(current_node.right)

	# def get_rightmost_node(self, root):
	# 	last_node = None
	# 	last_parent = None 
	# 	queue = []
	# 	queue.append(root)
	# 	queue.append(None)

	# 	while queue:
	# 		curr = queue.pop(0)
	# 		parent = queue.pop(0)
	# 		last_node = curr
	# 		last_parent = parent



	# Binary trees are unordered. Conventionally, we would just insert the node at the first available, leftmost position
	# We could compare values of the trees and insert based on that (Only insert data under a leaf it is less than for ex.)
	def insert_node(self, node, data):
		# If the tree is empty, then the whole tree is just the new node
		if node is None:
			return Node(data)
		
		# Again, use just a simple list and treat it as a queue 
		queue = []
		queue.append(node)

		while (len(queue) > 0):
			# Using level-order traversal, for each node check if it has children (starting with left)
			# If so, thats the insertion target. If not, throw its children in the queue and move on
			current_node = queue.pop(0)
			
			if current_node.left is None:
				current_node.left = Node(data)
				break 
			else:
				queue.append(current_node.left)
			if current_node.right is None:
				current_node.right = Node(data)
				break
			else:
				queue.append(current_node.right)

		return node
	
	# def delete_node(self, node, data):
	# 	if node is None:
	# 		return None

# Runner code 
bt = BinaryTree("root")
bt.root.left = Node(1)
bt.root.left.left = Node(2)
bt.root.left.right = Node(3)
bt.root.right = Node(4)
bt.root.right.left = Node(5)
bt.root.right.right = Node(6)
# bt.insert_node(bt.root, "inserted_node")

print("\n================Pre-order Traversal================")
bt.print_preorder_traversal(bt.root)
print("\n================In-order Traversal================")
bt.print_inorder_traversal(bt.root)
print("\n================Post-order Traversal================")
bt.print_postorder_traversal(bt.root)
print("\n================Level-order Traversal================")
bt.print_levelorder_traversal(bt.root)
print("\n================Find Height of BT================")
print(f"BT Height: {bt.height(bt.root)}")