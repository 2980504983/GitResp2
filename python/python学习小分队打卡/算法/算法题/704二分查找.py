"""
    经典二分查找，在一个有序数组中寻找一个数
"""


class Solution:

    def search(self, nums, target):
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (r-l)//2+l
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid-1
            elif nums[mid] < target:
                l = mid+1
        return -1
