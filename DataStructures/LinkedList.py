class Node:
	def __init__(self, node_data):
		self.data = node_data
		self.next = None

class LinkedList:
	def __init__(self, node_data):
		self.head = Node(node_data)
		self.tail = self.head

	def append_node(self, node_data):
		new_node = Node(node_data)
		self.tail.next = new_node
		self.tail = new_node
	
	def prepend_node(self, node_data):
		new_node = Node(node_data)
		new_node.next = self.head
		self.head = new_node

	def get_head(self):
		return self.head
	
	def get_tail(self):
		return self.tail
	
	def print_list(self):
		current_node = self.head
		current_node_data = self.head.data

		while current_node != None:
			current_node_data = current_node.data
			print(current_node_data)
			current_node = current_node.next

	def recursive_print_list(self, node):
		if node is None:
			return

		print(node.data)
		self.recursive_print_list(node.next)

	def get_length(self):
		if self.head:
			current_node = self.head
			length = 0

			while current_node != None:
				length += 1
				current_node = current_node.next
			
			return length 
		else:
			return 0
		
	def insert_node(self, data, index):
		# Iterative eapproach
		if self.head:
			current_node = self.head
			pos = -1
			new_node = Node(data)

			if index == 0: # Handle case where node is inserted at front 
				self.prepend_node(data)
			
			if index == -1: # Handle case where node is added to end 
				self.append_node(data)

			while current_node != None:
				pos += 1 
				if pos == index:
					new_node.next = current_node.next
					current_node.next = new_node
					return True
			return False 

	def update_node(self, index, data):
		if self.head:
			current_node = self.head
			pos = -1

			while current_node != None:
				pos += 1 
				if pos == index:
					current_node.data = data
					return True
				current_node = current_node.next
			return False 

	def delete_node(self, index):
		if self.head:
			current_node = self.head
			pos = -1

			while current_node != None:
				if (pos + 1) == index:
					current_node.next = current_node.next.next
					return True
				pos += 1
				current_node = current_node.next
			return False 
		
	def reverse(self):
		# Reverse linked list w/ iterative approach
		prev = None
		curr = self.head

		while curr: # If curr is None, prev will be tail (prev always 1 behind curr)
			temp = curr.next # Store connection to remaining list
			curr.next = prev # Reverse the next pointer direction
			prev = curr
			curr = temp
		self.head = prev

	def reverse_recursive(self, head):
		if head is None or head.next is None:
			self.head = head
			return head
		
		remainder = self.reverse_recursive(head.next) # Continue to reverse the remaining nodes

		# Set the next value of the NEXT node to the current node
		# So if we are on node 1, .next is node 2, .next.next is the next pointer for node 2
		# Set this equal to head so that 2's pointer is flipped
		head.next.next = head 
		head.next = None # Set current node next to None; this sets it as the current tail 
		
		# This will return the new head
		# All the calls will just be returning what the base case returns
		return remainder 
	
def main():
	ll = LinkedList(1)
	ll.append_node(2)
	ll.append_node(3)
	ll.prepend_node(4)
	ll.append_node(5)
	ll.insert_node(6, 2)
	print("Iterative print: ")
	ll.print_list()
	print("Recursive print: ")
	ll.recursive_print_list(ll.head)
	print("================================")
	print("Reverse list iteratively...")
	ll.reverse()
	ll.print_list()
	print("================================")
	print("Reverse list recursively...")
	ll.reverse_recursive(ll.head)
	ll.print_list()
	print("================================")
	ll.update_node(2,"Updated")
	ll.delete_node(4)
	ll.print_list()
	print(f"List Length: {ll.get_length()}")
	print("================================")
	
main()

