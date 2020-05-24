class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(' ')
        
        for word in range(len(words)):
            if searchWord in words[word]:
                found = True
                for i in range(len(searchWord)):
                    if searchWord[i] != words[word][i]:
                        found = False
                if found:
                    return word + 1
                
        return -1
