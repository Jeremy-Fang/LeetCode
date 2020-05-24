class Solution:
    def numSubarraysWithSum(self, A, S):
        res = 0
        ones = [-1] + [i for i in range(len(A)) if A[i] == 1] + [len(A)]
        
        print(ones)
        
        if S == 0:
            for i in range(1, len(ones)):
                z = ones[i] - ones[i-1] - 1
                res += z*(z+1)/2
        else:
            for i in range(1, len(ones)-S):
                l = ones[i] - ones[i-1] - 1
                r = ones[i+S] - ones[i+S-1] - 1
                res += (l+1) * (r+1)
            
        return int(res)
