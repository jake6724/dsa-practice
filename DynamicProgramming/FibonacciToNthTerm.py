# Function to find nth fibonacci number recursively
"""
- Remember that n is the nth num in the fib seq; n is not a value but an index essentially
- ex. n = 10 would have the value of 55
- So when we call fib(n - 1), we're really saying recursively find the value for the previous index
- This function is O(2^n) (expodential) which is horrible
"""
def fib(n):
	# Base case. If the value is 1 or less, there is no further subdivision of the problem to be done
	if (n <= 1):
		# No further subdivision means we can just return n (even tho it is usually an index)
		# The 1th index has value 1; 0 also have value 0
		return n 

	# Find the values of the 2 previous fib nums; this is useful because a fib num
	# is equal to the sum of the previous 2 nums
	x = fib(n - 1) 
	y = fib(n - 2) 

	return x + y

# Runner code 
print(f"Basic fib: {fib(10)}")


"""
- To improve this we will use dynamic programming and memoization
- Memoization is the process of storing calculated data for later.
	- In this case we will be storing the output of each recursive call
	- This will prevent us from computing the same value of n multiple times
- New implementation is O(n), because we only need to calc each num once
- There are further optimizations here: https://www.geeksforgeeks.org/introduction-to-dynamic-programming-data-structures-and-algorithm-tutorials/
"""

# We need a helper so that the main code can store data and not be called recursively
# This function we be called recursively instead, and started by the main function
def improved_fib_helper(n, ans):
	if (n <= 1):
		return n 

	# Check if this value has already been computed
	if (ans[n] != -1): 
		return ans[n] # If it has, use that value instead of re-computing

	# Else, compute for the first time
	x = fib(n - 1) 
	y = fib(n - 2) 

	# Save for future use
	ans[n] = x + y

	return ans[n]

def improved_fib(n):
	ans = [-1]*(n+1)

	return improved_fib_helper(n, ans)

# Runner code
print(f"Improved fib: {improved_fib(50)}")