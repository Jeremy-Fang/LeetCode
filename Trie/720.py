class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        class Trie:
            
            class TrieNode:
                
                def __init__(self):
                    self.rec = 0
                    self.childs = {}
                    
            def __init__(self):
                self.root = self.TrieNode()
                
            def insert(self, word):
                trav = self.root
                
                for c in word:
                    if c not in trav.childs:
                        trav.childs[c] = self.TrieNode()
                    trav = trav.childs[c]
                    
                trav.rec += 1
                
            def searchBuilt(self, word):
                trav = self.root
                
                for i, c in enumerate(word):
                    if c not in trav.childs or (i != 0 and trav.rec < 1):
                        return False
                    
                    trav = trav.childs[c]
                    
                return trav.rec > 0
            
        dic = Trie()
        mx = ""
        
        words.sort()
        
        for word in words:
            dic.insert(word)
            
        for word in words:
            if dic.searchBuilt(word) and len(word) > len(mx):
                mx = word
                
        return mx
