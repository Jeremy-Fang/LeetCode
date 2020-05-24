# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def binary_search(l, h):
            mid = (l+h)//2
            
            if not isBadVersion(mid) and isBadVersion(mid+1):
                return mid+1
            if isBadVersion(mid):
                return binary_search(l, mid-1)
            else:
                return binary_search(mid+1, h)
            
        return binary_search(0, n)
