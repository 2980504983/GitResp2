class Solution:
    def searchInsert(self, nums, target):
        l, r = 0, len(nums)-1

        # l<=r才循环说明，返回结果的前一次，一定是这样的情况 r l,所以返回l就是要插入的位置了
        while l <= r:
            mid = (r-l)//2+l
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid-1
            elif nums[mid] < target:
                l = mid+1
        return l
