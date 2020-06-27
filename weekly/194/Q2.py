class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        used = set()
        mn = {}
        res = []
        
        if len(names) == 1:
            return names
        
        for i, name in enumerate(names):
            if name not in mn and name not in used:
                # base has not been used and the base name is not the suffix of something else
                used.add(name)
                res.append(name)
                mn[name] = 1
            else:
                if name not in mn:
                    mn[name] = 1
                    
                while name + "(" + str(mn[name]) + ")" in used:
                    mn[name] += 1
                    
                cand = name + "(" + str(mn[name]) + ")"
                used.add(cand)
                res.append(cand)
                mn[name] += 1
                
        return res
                
