class Solution:
    '''
    [73, 74, 75, 71, 69, 72, 76, 73]
    [73] 0
    [73,76] 0 
    [73,76,72] 1
    [73,76,72,69] 1
    [73,76,72,69,71] 2
    
    '''
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        r = []
        N = len(T)
        
        for i in range(N - 1, - 1, -1):
            res = 1
            while stack and stack[-1][0] <= T[i]:
                res += stack.pop()[1]
            if not stack:
                stack.append((T[i], 0))
                r.append(0)
            else:
                stack.append((T[i], res))
                r.append(res)
            
        return r[::-1]
