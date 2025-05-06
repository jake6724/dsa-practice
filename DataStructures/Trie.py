class TrieNode:
	def __init__(self):
		self.children = {}
		self.endOfWord = False

class Trie:
	def __init__(self):
		self.root = TrieNode()

	def insert(self, word: str) -> None:
		curr = self.root
		for c in word: 							# The main loop is just iterating through the chars in the word
			if c not in curr.children:			# If the char isn't in the current level, add it
				curr.children[c] = TrieNode()   
			curr = curr.children[c]             # Either ways, update current node to the char we just checked's node
		curr.endOfWord = True					# Once loop ends, we're pointing at last node. Set EOW true now

	def search(self, word: str) -> bool:
		curr = self.root 

		for c in word:					  	    # Check each char. If any don't exist, return False
			if c not in curr.children:
				return False
			curr = curr.children[c]
		return curr.endOfWord            	    # If all chars exist, endOfWords will say if word exists

	def startsWith(self, word: str) -> bool: 
		curr = self.root 						# This func is the same as search, but we dont care about endOfWord 
		for c in word:							# If we make it through the char loop, we can just return True
			if c not in curr.children:
				return False
			curr = curr.children[c]
		return True  						
	
# Runner code 
T = Trie()
