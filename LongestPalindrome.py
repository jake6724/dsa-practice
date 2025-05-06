from collections import defaultdict

class Solution:
	def isPalindrome(self, s: str) -> bool:
		# This is not needed for 'longestPalindrome'
		# Use 2-pointer
		l, r = 0, len(s) - 1
		while l < r:
			if s[l] != s[r]:
				return False
			l += 1
			r -= 1
		return True 

	def longestPalindrome(self, s: str) -> int:
		h = defaultdict(int)
		r = ""
		middle_char = None

		for c in s:
			h[c] += 1
        
		for c in h:
			if h[c] % 2 == 0:
				n = h[c] // 2
				r = (c * n) + r + (c * n)
			else:
				n = (h[c] - 1) // 2
				r = (c * n) + r + (c * n)
				if not middle_char:
					middle_char = c
        
		midpoint = len(r) // 2
		r = r[:midpoint] + middle_char + r[midpoint:]
		print(r)
		return len(r)

# Runner code 
S = Solution()
s = "tacocat"
r = S.longestPalindrome(s)
print(f"Longest palindrome of {s}: \n{r}")
print(f"Is this a palindrome: {S.isPalindrome(r)}")