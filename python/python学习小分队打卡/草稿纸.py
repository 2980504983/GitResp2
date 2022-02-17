def findMin(nums):
    if nums[0] <= nums[-1]:
        return nums[0]

    left, right = 0, len(nums) - 1

    while left < right:
        mid = (right - left) // 2 + left
        if nums[mid] >= nums[0]:
            left = mid + 1
        elif nums[mid] < nums[right]:
            right = mid - 1
    return nums[left]


print(findMin([4,5,6,7,0,1,2]))