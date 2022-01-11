# 第十三周
# 第一题：字符串转换整数
# 第二题：回文数
# 第三题：正则表达式匹配
# 第四题：盛最多水的容器
# 第五题：整数转罗马数字
# 第六题：罗马数字转整数
# 第七题：最长公共前缀


# 第一题：字符串转换整数
# 自己写的解法，但是超出时间限制了
# class Solution:
#     def myAtoi(self, s: str) -> int:
#         c=0
#         b=0
#         a=''
#         flag = True
#         while b<=len(s)-1 and flag:
#             if s[b] in ('1','2','3','4','4','5','6','7','8','9'):
#                 a+=s[b]
#                 b+=1
#             elif s[b] in (' ', '0'):
#                 b+=1
#             elif s[b] == '-' or '+':
#                 if s[b+1] in ('-', "+"):
#                     flag = False
#                 elif s[b] == '-':
#                     c=1
#                     b+=1
#             else:
#                 flag = False
#         if a and c==1 and -int(a)>=-2**31:
#             return -int(a)
#         elif a and int(a)<=2**31:
#             return int(a)
#         elif a and -int(a)<=-2**31:
#             return -2**31
#         elif a and int(a)>=2**31:
#             return 2**31
#         else:
#             return 0


# -----------------------------------------------------------------


# 第二题：回文数
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if -2 ** 31 <= x <= 2 ** 31 - 1:
#             a = str(x)
#             b = a[::-1]
#             if a == b:
#                 return True
#             else:
#                 return False


# ---------------------------------------------------------------


# 第三题：正则表达式匹配
# 这题写的超痛苦，看了答案，感觉没看懂


# ----------------------------------------------------------------


# 第四题：盛最多水的容器
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         ans = 0
#         cur1 = len(height)-1
#         cur2 = 0
#         while cur1 > cur2:
#             if height[cur2] >= height[cur1]:
#                 s = (cur1 - cur2) * height[cur1]
#                 cur1 -= 1
#             else:
#                 s = (cur1 - cur2) * height[cur2]
#                 cur2 += 1
#             if s > ans:
#                 ans = s
#         return ans


# -----------------------------------------------------------


# 第五题：整数转罗马数字
# 这题的思路挺好的
# class Solution:
#     def intToRoman(self, num: int) -> str:
#         thousands = ['MMM', 'MM', 'M', '']
#         hundred = ['CM', 'DCCC', 'DCC', 'DC', 'D', 'CD', 'CCC', 'CC', 'C', '']
#         tens = ['XC', 'LXXX', 'LXX', 'LX', 'L', 'XL', 'XXX', 'XX', 'X', '']
#         ones = ['IX', 'VIII', 'VII', 'VI', 'V', 'IV', 'III', 'II', 'I', '']
#
#         return thousands[3-(num // 1000)] + \
#             hundred[9-(num % 1000 // 100)] + \
#             tens[9-(num % 100 // 10)] + \
#             ones[9-(num % 10)]


# ----------------------------------------------------------------


# 第六题：罗马数字转整数
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         dic = {'I': 1,
#            'V': 5,
#            'X': 10,
#            'L': 50,
#            'C': 100,
#            'D': 500,
#            'M': 1000,
#            }
#
#         ans = 0
#         item = len(s)-1
#
#         while item >= 0:
#             if dic[s[item]] > dic[s[item-1]] and item >= 1:
#                 ans += (dic[s[item]] - dic[s[item-1]])
#                 item -= 2
#             else:
#                 ans += dic[s[item]]
#                 item -= 1
#         return ans


# ------------------------------------------------------------------


# 第七题：最长公共前缀
# 这里用了一个any()函数，判断迭代对象的布尔值，一真全真
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ''
#
#         l = len(strs[0])
#         c = len(strs)
#
#         for i in range(l):
#             s = strs[0][i]
#             if any(i == len(strs[j]) or strs[j][i] != s for j in range(c)):
#                 return strs[0][:i]
#
#         return strs[0]
