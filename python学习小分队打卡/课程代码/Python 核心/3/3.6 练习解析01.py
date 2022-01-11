"""
    练习：定义MyRange类，实现下列功能
    for item in range(10):
        print(item)
"""


class DigitalIterator:
    def __init__(self, target):
        self.target = target
        self.number = self.target

    def __next__(self):
        if self.number <= 0:
            raise StopIteration
        temp = self.target - self.number
        self.number -= 1
        return temp


class DigitalGeneration:
    def __init__(self, number):
        self.number = number

    def __iter__(self):
        return DigitalIterator(self.number)


# digital = DigitalGeneration(5)
# iterator = digital.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except StopIteration:
#         break

# next一次，计算一次，返回一次。所以即使数很大，也不会很占内存
for item in DigitalGeneration(999999999999999999):
    print(item)
