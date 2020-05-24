class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def backtrack(arr, curr, open, closed, max):
            if len(curr) == max * 2:
                arr.append(curr)
            
            if open < max:
                arr = backtrack(arr, curr + "(", open + 1, closed, max)
            if closed < open:
                arr = backtrack(arr, curr + ")", open, closed + 1, max)
                
            return arr
            
        return backtrack([], "", 0, 0, n)
                
        
