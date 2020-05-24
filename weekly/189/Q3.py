class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        indexes = []
        res = []
        N = len(favoriteCompanies)
        
        for person in favoriteCompanies:
            indexes.append(set(person))
            
        
        for i in range(N):
            found = False
            for j in range(N):
                if found:
                    continue
                if i != j:
                    for k in indexes[i]:
                        if k not in indexes[j]:
                            break
                    else:
                        found = True
                            
            if not found:
                res.append(i)
                
        return res
