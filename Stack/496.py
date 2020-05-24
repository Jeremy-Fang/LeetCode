class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        M = len(nums1)
        N = len(nums2)
        d = {}
        res = [-1] * M
        
        for i in range(N):
            while stack and nums2[stack[-1]] < nums2[i]:
                top = stack.pop()
                d[nums2[top]] = nums2[i]
            stack.append(i)
        
        for i in range(M):
            if nums1[i] not in d:
                res[i] = -1
            else:
                res[i] = d[nums1[i]]
            
        return res
