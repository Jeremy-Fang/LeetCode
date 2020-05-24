class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'], \
                '6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        
        def backtrack(arr, curr, i, s):
            if len(curr) == len(s):
                arr.append(curr)
                return arr
            
            for j in d[s[i]]:
                arr = backtrack(arr, curr + j, i + 1, s)
                
            return arr
        
        if not digits:
            return []
        return backtrack([], "", 0, digits)
