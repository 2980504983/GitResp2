"""
    寻找第一个错误版本
"""


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l <= r:
            mid = (r-l)//2+l
            if isBadVersion(mid):
                r = mid-1
            else:
                l = mid+1
        return l