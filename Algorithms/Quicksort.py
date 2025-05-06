"""
Notes:
- Recursive

- Avg. Time complexity: O(nlogn)
- Worst Time complexity: O(n ^ 2). This occurs when the list is already sorted
- Space complexity: O(1) because we sort the list in place

- Select a pivot; partition all numbers higher than and lower than this pivot to their respective sides 
	- After this, the pivot will be in its correct position in the final sorted aray
- Choosing the pivot is very important, as a well chosen pivot will help divide the work up between partitions and recursive calls
- When choosing pivot, we can use median-of-3
	- Look at first, middle, and last element of the array
	- Sort them (Edit the list in place), and choose the middle item as our pivot

- In the below example, use the last element of a list as the pivot 
"""

def partition(array, left, right):
	pivot = array[right]			# Select the right-most element as pivot  
	i = left - 1					# Pointer for greater element

	for j in range(left, right): 	# Traverse all elements in sublist and compare with pivot
		if array[j] <= pivot:		# If element smaller than pivot, swap it with greater value 
			i += 1
			array[i], array[j] = array[j], array[i]

	array[i + 1], array[right] = array[right], array[i + 1] 	# Swap pivot element with greater element
	return i + 1 												# Return the position from where the partition is done

def quickSort(array, left, right):
	if left < right:
		p = partition(array, left, right) 	# Find pivot such that, elements smaller than pivot on left, larger on right

		quickSort(array, left, p - 1)		# Recursive call left of pivot
		quickSort(array, p + 1, right)		# Recursive call right of pivot 

# Runner code:
data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)
size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)