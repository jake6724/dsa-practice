"""
- Stack implementation using the list data structure 
- Stack follows LIFO (Last in first out)
"""

class ListStack:
	def __init__(self):
		self.stack = []

	def is_empty(self):
		# If length is 0, then empty. So we want the opposite because 0 would cast to False
		return not bool(len(self.stack))
	
	def size(self):
		return len(self.stack)
	
	def print_stack(self):
		print(self.stack)

	def push(self, data):
		self.stack.append(data)
	
	def pop(self):
		# Don't try to check the -1 index if the list is empty
		if self.is_empty() is True:
			return None
		else:
			r = self.stack[-1]
			del self.stack[-1]
			return r 
		
	def peek(self):
		if self.is_empty is True:
			return None
		else:
			return self.stack[-1]

# Runner code 
s = ListStack()
s.print_stack()
print(f"Is stack empty: {s.is_empty()}")
print("Pushing items to stack...")
s.push(1)
s.push(2)
s.push(3)
s.print_stack()
print("Popping stack...")
r = s.pop()
print(f"Return of pop: {r}")
s.print_stack()
print(f"Is stack empty: {s.is_empty()}")
print(f"Stack size: {s.size()}")

print("===========================================================")
print("Running corner cases")
s = ListStack()
s.print_stack()
print("Popping stack...")
s.pop()
s.print_stack()