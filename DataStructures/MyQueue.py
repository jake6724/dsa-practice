"""
General Notes
- Linear data structure
- Follows FIFO (First in First out)
- KEY: All additions are made at the back, and all deletions are made from the front
"""
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class Queue:
	def __init__(self):
		self.front = None
		self.rear = None
	
	def is_empty(self):
		return self.front is None and self.rear is None
	
	def print_queue(self):
		print("[", end=' ')
		cn = self.front
		while cn is not None:
			print(f"{cn.data}", end=' ')
			cn = cn.next
		print("]")
	
	def enqueue(self, data): # Add new data to the queue. This assumes raw data and still needs to be put in node form
		new_node = Node(data)
		if self.rear is None: # If rear is empty, this node is the front and rear since nodes enter thru the rear
			self.front = self.rear = new_node
			return 

		# Add the new node at the end, change rear pointer
		self.rear.next = new_node
		self.rear = new_node

	def dequeue(self): # Remove from front of queue (return that value as well)
		if self.is_empty():
			print("Queue is empty")
			
		data = self.front.data
		self.front = self.front.next

		# If front becomes None, set rear equal to None as well because the queue is now empty 
		if self.front is None:
			self.rear = None
		return data
	
	def peak_front(self): # Currently, this returns the Node data. Could return the node obj instead if needed
		if self.is_empty():
			print("Queue is empty")
			return 
		return self.front.data
	
	def peak_rear(self):
		if self.is_empty():
			print("Queue is empty")
			return
		return self.rear.data

# # Runner code
# Q = Queue()
# print(f"Is queue empty: {Q.is_empty()}")
# Q.print_queue()
# Q.enqueue(1)
# Q.enqueue(2)
# Q.enqueue(3)
# Q.enqueue(4)
# Q.print_queue()
# Q.dequeue()
# Q.print_queue()
# Q.dequeue()
# Q.print_queue()
# print(f"Front of Q: {Q.peak_front()}")
# print(f"Rear of Q: {Q.peak_rear()}")

