class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        delta = [0] * 26
        
        if len(s1) > len(s2):
            return False
        
        for c in s1:
            delta[ord(c) - ord('a')] += 1
            
        
        for end in range(len(s2)):
            delta[ord(s2[end]) - ord('a')] -= 1
            
            if end >= len(s1):
                delta[ord(s2[end - len(s1)]) - ord('a')] += 1
                
            if end + 1 >= len(s1):
                for c in delta:
                    if c != 0:
                        break
                else:
                    return True
                
        return False
