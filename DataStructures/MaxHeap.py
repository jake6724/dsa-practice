# MinHeap implementation using an array
# https://www.youtube.com/watch?v=pAU21g-jBiE&t=157s

class MaxHeap:
	def max_heapify(self, a, heap_size, i):
		l = 2*i + 1 
		r = 2*i + 2
		largest = i

		# Check that were in range 
		# Check if either child is larger
		# If largest is not the index of i (a child was larger),
		# swap the item at the current index with the item at the largest index
		# recursively call with the same array and heap size, but pass largest
		# this works because largest is an index, and it is where our node floated down to after swapping

		if l < heap_size and a[l] > a[i]:
			largest = l
		
		if r < heap_size and a[r] > a[i]:
			largest = r
		
		if largest != i:
			a[i], a[largest] = a[largest], a[i]
			self.max_heapify(a, heap_size, largest)

	def build_max_heap(self, a):
		heap_size = len(a)
		for i in range(heap_size - 1):
			self.max_heapify(a, heap_size, i)
	
def main():
	a = [0,1,2,3,4,5,6,7,8]
	max_heap = MaxHeap()
	max_heap.build_max_heap(a)
	print(a)



main()

