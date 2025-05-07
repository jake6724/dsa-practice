"""
Reference: https://www.geeksforgeeks.org/introduction-to-min-heap-data-structure/
find parent: arr[(i - 1) // 2]
find left child: (i * 2) + 1
find right child: (i * 2) + 2 
"""

# HEAPYIFY AND BUILD HEAP ARE STILL BROKEN.

class minHeap():
	def __init__(self, a=[]):
		self.heap = a
		self.heap_size = len(self.heap) - 1

	def __str__(self):
		return str(self.heap)

	# def min_heapify(self, index): 
	# 	"""Create a heap from an unsorted array. Goal is to maintain the heap invariant. \n
	# 	Index represents the current parent node"""
	# 	smallest = index
	# 	child_left_index = self.get_child_left(index)
	# 	child_right_index = self.get_child_right(index)

	# 	# Compare for each child, but only check that child if its index is inbounds (if not it doesn't really exist)
	# 	if (child_left_index < self.heap_size) and (self.heap[child_left_index] < smallest):
	# 		smallest = child_left_index

	# 	elif (child_right_index < self.heap_size) and (self.heap[child_right_index] < smallest):
	# 		smallest = child_right_index
		
	# 	if smallest != index: # This means that a child has a smaller value and parent should move down
	# 		self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
	# 		self.min_heapify(smallest) # Recurse up to where the smallest was just moved and rerun

	def pop(self):
		# Return None if heap is empty
		if not self.heap:
			return None
		
		# Swap root with the last item and pop
		self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
		r = self.heap.pop()
		self.heap_size -= 1

		index = 0
		# Move the new root down through its children to its correct position
		while True:
			smallest = index
			child_left_index = self.get_child_left(index)
			child_right_index = self.get_child_right(index)

			# Compare for each child, but only check that child if its index is inbounds (if not it doesn't really exist)
			if (child_left_index < self.heap_size) and (self.heap[index] > self.heap[child_left_index]):
				smallest = child_left_index

			elif (child_right_index < self.heap_size) and self.heap[index] > self.heap[child_right_index]:
				smallest = child_right_index
			
			if smallest != index: # This means that a child has a smaller value and parent should move down
				self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
			else: # Parent was not smaller and shouldn't move down, so we're DONE. This is key
				break

			index = smallest

		return r

	def push(self, val):
		# Append to heap and update member vars
		self.heap.append(val)
		self.heap_size += 1 

		# Get indexes
		val_index = self.heap_size
		parent_index = self.get_parent(val_index)

		# Compare and swap until in correct position
		while (val_index > 0) and (self.heap[val_index] < self.heap[parent_index]):
			self.heap[val_index], self.heap[parent_index] = self.heap[parent_index], self.heap[val_index]
			val_index = parent_index
			parent_index = self.get_parent(val_index)

	def get_parent(self, index):
		"""Return the index of the parent of the node at passed index"""
		return (index - 1) // 2
	
	def get_child_left(self, index):
		"""Return the index of the left child of node at passed index"""
		return (index * 2) + 1
	
	def get_child_right(self, index):
		"""Return the index of the right child of node at passed index"""
		return (index * 2) + 2
	
# These 2 functions exist outside of the Heap class, and are used to heapify an unsorted, non-heap array
def min_heapify(arr, heap_size, index):
		"""Create a heap from an unsorted array. Goal is to maintain the heap invariant. \n
		Index represents the current parent node"""
		smallest = index
		child_left_index = (index * 2) + 1
		child_right_index = (index * 2) + 2

		# Compare for each child, but only check that child if its index is inbounds (if not it doesn't really exist)
		if child_left_index < heap_size and arr[child_left_index] < arr[smallest]:
			smallest = child_left_index

		if (child_right_index < heap_size) and (arr[child_right_index] < arr[smallest]):
			smallest = child_right_index
		
		if smallest != index: # This means that a child has a smaller value and parent should move down
			arr[index], arr[smallest] = arr[smallest], arr[index]
			min_heapify(arr, heap_size, smallest) # Recurse up to where the smallest was just moved and rerun

def build_min_heap(arr):
	#               *
	# [4, 7, 32, 8, 0, 5, 2, 5, 8, -1]
	start_index = (len(arr) // 2) - 1 # 4
	for i in range(start_index, -1, -1):
		print("i:", i)
		min_heapify(arr, len(arr), i)

# Runner code
def main():

	print("1. Build heap and heapify test: ")
	a = [5,7,3,8,2,1,0,99,7,4,4,2,1]
	print("starting array: ", a)
	min_heap = minHeap(a)
	print("After create heap with array as input: ", min_heap)

	min_heap = minHeap([1,2,3,4,5,6])
	print("2. Push Test")
	print("Start: ", min_heap)
	min_heap.push(0)
	print("After pushing 0: ", min_heap)

	print("3. Pop Test")
	print("Start: ", min_heap)
	r = min_heap.pop()
	print("After popping: ", min_heap)
	print("Pop return: ", r)
	print("Popping 5 more times")
	min_heap.pop()
	print("popped once: ", min_heap)
	min_heap.pop()
	print("popped twice", min_heap)
	min_heap.pop()
	print("popped thrice", min_heap)
	min_heap.pop()
	print("popped qice", min_heap)
	min_heap.pop()
	print("popped fice", min_heap)
	print("After popping 5 times: ", min_heap)
	min_heap.pop()
	print("Another pop!", min_heap)
	min_heap.pop()
	print("Another pop!", min_heap)

	print("4. Test build heapify/heapify ")
	a = [4,7,32,8,0,5,2,5,8,-1]
	print("Starting arr: ", a)
	build_min_heap(a)
	print("After build_min_heap(a): ", a)

main()