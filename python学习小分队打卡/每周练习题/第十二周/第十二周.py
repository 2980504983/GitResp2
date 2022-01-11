# 题目一
# 两数之和

# 思路是遍历数组的索引值两次，如果，两个索引值对应的数值之和为目标值，且这两个索引值不相等，就返回
# 这两个索引
def twoSum(nums, tar):
    for item in range(len(nums)):
        for item1 in range(len(nums)):
            if tar == nums[item] + nums[item1] and item != item1:
                return [item, item1]


# --------------------------------------------------------------------------


# 题目二
# 两数相加

# 这一题要对链表有一定的了解
# 这是链表节点的类，最重要的特点是可以根据这个节点找到下一个节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:

    # 创建一个头节点，和一个指针
    # 这两个其实指的是同一个节点，因为链表不可逆的特性，所以必须要留一个变量存储头节点，不然链表
    # 就回不来了
    result = curr = ListNode()
    # 进位项
    remainder = 0

    # 如果两个链表有一个没有走完就继续循环
    while l1 or l2:
        # 将链表当前节点的值赋给x和y，没了就补零
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0

        # 计算两个节点和前两个节点进位项的和
        total = x + y + remainder

        # 创建一个节点记录数据，除以10取余
        curr.next = ListNode(total % 10)
        # 记录进位项
        remainder = total//10

        # 如果链表没走完，就走向下一个节点
        if l1: l1 = l1.next
        if l2: l2 = l2.next
        # 链表走向下一个节点
        curr = curr.next

    # 如果最后两个节点有进位，就在创建一个节点记录数据
    if remainder: curr.next = ListNode(remainder)

    # 这里就体现了头节点的作用，前面的指针cur已经走到了最后一个节点，回不来了，要从头读取数据
    # 只能通过头节点来再次遍历
    return result.next


# -----------------------------------------------------------------------

# 题目三
# 无重复字符的最长子串

# 我这题的思路是，设置一个头和尾，遍历字符串，每追加一个无重复字符，尾就加一
# 当遍历的字符与前面的字符重复了，就记录头和尾的差，记录当前无重复字符的长度，并将尾的值赋给头
# 便于下一次的记录，最后将所有无重复字符的长度都放在一个列表中，通过max()函数取出最大值就行了

# 就相当于一个长度不定的窗口当下一个字符在窗口中没有，就加进来，有了就将尾赋给头，清空窗口，在进行
# 之前的操作

def lengthOfLongestSubstring(s: str) -> int:
    # 用于记录无重复字符的长度
    list_l = []
    # 记录无重复的字符
    list_s = []
    head = tail = 0
    if s:
        for i in s:
            if i not in list_s:
                list_s.append(i)
                tail += 1
                if tail == len(s):
                    list_l.append(tail-head)
            else:
                list_l.append(tail-head)
                del list_s[0:list_s.index(i)+1]
                list_s.append(i)
                head = tail-list_s.index(i)
                tail += 1
        return max(list_l)
    else:
        return 0


# ----------------------------------------------------------------------


# 题目四
# 寻找两个正序数组的中位数

# 思路：
# 将两个列表合并成一个列表，并通过sort()排序，如果列表长度是奇数就返回中间值，偶数就返回中间两个
# 值得平均值
def findMedianSortedArrays(nums1: [int], nums2: [int]) -> float:
    nums3 = nums1+nums2
    nums3.sort()
    if len(nums3) % 2 == 0:
        a = len(nums3)
        return (nums3[int(a/2-1)]+nums3[int(a/2)])/2
    else:
        return nums3[int((len(nums3)-1)/2)]


# ----------------------------------------------------------------------


# 题目五
# 最长回文子串

# 这题写的脑瓜疼，大致的思路和过程都写完了，但是后面好多bug，写了两遍，都没写好


# -----------------------------------------------------------------------


# 题目六
# z 字形变换

# 思路：将排列后，相同行数的元素放在同一个列表中，最后按行数顺序取出就行了
def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    # 根据行数在创建一个与行数有相同数量元素的列表
    res = ['' for i in range(numRows)]

    # 标记遍历字符串的行数 和 方向
    l, f = 0, 1
    # 遍历字符串
    for item in s:
        # 根据行数将字符串放入对应的列表元素中
        res[l] += item
        l += f
        # 当行数没达到最大时，递增了，达到了递减
        if l == numRows - 1 or l == 0:
            # 改变方向
            f = -f
    return "".join(res)


# -----------------------------------------------------------------


# 题目七
# 整数反转

# 思路：将int 转成str 在用reversed()方法反转，在转成int输出

def reverse(x: int) -> int:
    if x < 0:
        s = str(abs(x))
        a = "".join(reversed(s))

        if -int(a) >= -2**31:
            return -int(a)
        else:
            return 0

    else:
        s = str(abs(x))
        a = "".join(reversed(s))
        if int(a) <= 2**31:
            return int(a)
        else:
            return 0

# --------------------------------             gogo

