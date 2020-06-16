class Trie:
    
    class TrieNode:
        def __init__(self):
            self.rec = 0
            self.child = [None] * 26
            
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = [None] * 26

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        trav = None
        for index, char in enumerate(word):
            if index == 0:
                # get root node
                if self.words[ord(char) - ord('a')] == None:
                    self.words[ord(char) - ord('a')] = self.TrieNode()
                trav = self.words[ord(char) - ord('a')]
            else:
                if trav.child[ord(char) - ord('a')] == None:
                    trav.child[ord(char) - ord('a')] = self.TrieNode()
                trav = trav.child[ord(char) - ord('a')]
                
        trav.rec += 1
            
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        for index, char in enumerate(word):
            if index == 0:
                #get root node
                if self.words[ord(char) - ord('a')] == None:
                    return False
                trav = self.words[ord(char) - ord('a')]
            else:
                if trav.child[ord(char) - ord('a')] == None:
                    return False
                trav = trav.child[ord(char) - ord('a')]
                
        return trav.rec > 0
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        for index, char in enumerate(prefix):
            if index == 0:
                #get root node
                if self.words[ord(char) - ord('a')] == None:
                    return False
                trav = self.words[ord(char) - ord('a')]
            else:
                if trav.child[ord(char) - ord('a')] == None:
                    return False
                trav = trav.child[ord(char) - ord('a')]
                
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
