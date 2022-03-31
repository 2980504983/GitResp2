class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        def do_it(left, right):
            if left > right:
                return

            mid = (right - left) // 2 + left

            root = TreeNode(nums[mid])
            x = root.val
            # 左子树二分
            root.left = do_it(left, mid - 1)
            # 右子树二分
            root.right = do_it(mid + 1, right)
            return root

        return do_it(0, len(nums) - 1)


nums = [-10,-3,0,5,9]
s = Solution()
s.sortedArrayToBST(nums)
