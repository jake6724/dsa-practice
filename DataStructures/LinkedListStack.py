"""
- Implementation of stack using Linked List
- Stack follows LIFO (Last in first out)
"""

class Node:
	def __init__(self, node_data):
		self.data = node_data
		self.next = None

class LinkedListStack:
	def __init__(self):
		self.head = None
		self.tail = None
	
	def is_empty(self):
		if self.head is None:
			return True
		else:
			return False
	
	# Size of linked list containing stack node data 
	def size(self):
		curr = self.head
		s = 0
		while curr is not None:
			s += 1 
			curr = curr.next
		return s
	
	# Print data from each node in stack, top to bottom
	def print_stack(self):
		if self.head is None:
			print("[]")
			return
		curr = self.head
		while curr is not None:
			# Check if tail to make printing all one line, with newline on last print
			if curr == self.tail:
				print(curr.data)
			else:
				print(curr.data, end=' ') 
			curr = curr.next
		

	# Add node to top of stack
	def push(self, data):
		new_node = Node(data)
		
		# If list is empty, set head and tail vars and stop
		if self.is_empty():
			self.head = new_node
			self.tail = new_node
			return
		else:
			new_node.next = self.head
			self.head = new_node
	
	# Return and remove node from top of stack
	def pop(self):
		# If empty, return None and don't update stack any further
		if self.is_empty():
			return None
		
		# Update head pointer, remove current head
		r = self.head
		self.head = self.head.next

		# If this update made the list empty, reset pointers
		if self.is_empty():
			self.head = None
			self.tail = None

		return r.data
	
	# Return node from top of stack, do not remove it
	def peek(self):
		return self.head

# Runner code 
s = LinkedListStack()
s.print_stack()
print(f"Stack is empty: {s.is_empty()}")
print("Popping 1 from stack...")
r = s.pop()
print(f"Pop return: {r}")
print("Pushing to stack")
s.push(1)
s.push(2)
s.push(3)
s.print_stack()
print(f"Stack size: {s.size()}")
print("Popping 1 from stack...")
r = s.pop()
print(f"Pop return: {r}")
print("Popping 3 more times...")
r = s.pop()
print(f"Pop return: {r}")
r = s.pop()
print(f"Pop return: {r}")
r = s.pop()
print(f"Pop return: {r}")
s.print_stack()
print(f"Stack is empty: {s.is_empty()}")
print(f"Stack size: {s.size()}")