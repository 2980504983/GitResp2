"""
    二分查找
"""


def search(list_, key):
    l, r = 0, len(list_)-1
    while l <= r:
        mid = (l+r)//2
        if list_[mid] == key:
            return mid
        elif list_[mid] < key:
            l = mid+1
        else:
            r = mid-1


print(search([1,2,4,8,9,], 9))
