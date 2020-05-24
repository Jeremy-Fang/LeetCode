class Solution:
    def firstUniqChar(self, s: str) -> int:
        order = []
        d = set()
        
        for c in range(len(s)):
            if s[c] not in d:
                d.add(s[c])
                order.append(s[c])
            else:
                if s[c] in order:
                    order.remove(s[c])
                
        if len(order) == 0:
            return -1
        return s.index(order[0])
