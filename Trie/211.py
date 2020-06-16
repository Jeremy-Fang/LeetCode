class WordDictionary:
    
    class Node:
        def __init__(self):
            self.rec = 0
            self.childs = {}
            
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.Node()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        trav = self.root
        
        for c in word:
            if c not in trav.childs:
                trav.childs[c] = self.Node()
            trav = trav.childs[c]
            
        trav.rec += 1

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        
        def helper(n, sub):
            if not sub:
                return n.rec > 0
            
            for i, c in enumerate(sub):
                if c == ".":
                    for l in n.childs:
                        if helper(n.childs[l], sub[i+1:]):
                            return True
                    return False
                else:
                    if c not in n.childs:
                        return False
                    n = n.childs[c]
                    
            return n.rec > 0
                        
        trav = self.root
        
        for i, c in enumerate(word):
            if c == ".":
                for l in trav.childs:
                    if helper(trav.childs[l], word[i+1:]):
                        return True
                return False
            else:
                if c not in trav.childs:
                    return False
                trav = trav.childs[c]
            
        return trav.rec > 0  


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
