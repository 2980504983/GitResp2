"""
    列表助手模块
    自己要做自己的工具箱，觉得那段代码好用方便就存进去，以后用到直接粘贴就好了
"""


class ListHelper:
    """
        列表助手类
    """

    @staticmethod
    def find_all(list_target, func_condition):
        """
            通用的查找某个条件所有元素的方法
        :param list_target: 需要查找的列表
        :param func_condition: 需要查找的条件，函数类型:
                函数名(参数) --> bool
        :return: 需要查找的元素，生成器类型
        """
        for item in list_target:
            if func_condition(item):
                yield item

    @staticmethod
    def find_single(list_target, func_condition):
        """
            通用的查找某个条件一个元素的方法
        :param list_target: 需要查找的列表
        :param func_condition: 需要查找的条件，函数类型:
                函数名(参数) --> bool
        :return: 需要查找的一个元素
        """
        for item in list_target:
            if func_condition(item):
                yield item

    @staticmethod
    def is_exists(list_target, func_condition):
        """
            通用的判断是否存在某个条件元素的方法
        :param list_target: 需要查找的列表
        :param func_condition: 需要查找的条件，函数类型:
                函数名(参数) --> bool
        :return: bool类型，True表示存在，False表示不存在
        """
        for item in list_target:
            if func_condition(item):
                return True
        return False

    @staticmethod
    def summation(list_target, func_handle):
        """
            通用的求和方法
        :param list_target: 需要求和的列表
        :param func_handle: 需要求和的处理逻辑，函数类型:
                函数名(参数) --> int/float
        :return: 和
        """
        result = 0
        for item in list_target:
            result += func_handle(item)
        return result

    @staticmethod
    def select(list_target, func_handle):
        """
            通用的筛选方法
        :param list_target: 需要筛选的列表
        :param func_handle: 需要筛选的处理逻辑，函数类型
                函数名(参数) --> 任意类型
        :return: 生成器
        """
        for item in list_target:
            yield func_handle(item)

    @staticmethod
    def get_max(list_target, func_handle):
        """
            通用的获取最大元素方法
        :param list_target: 需要搜索的列表
        :param func_handle: 需要搜索的处理逻辑，函数类型
                函数名(参数) --> str/int ...
        :return: 最大元素
        """
        max_value = list_target[0]
        for i in range(1, len(list_target)):
            if func_handle(max_value) < func_handle(list_target[i]):
                max_value = list_target[i]
        return max_value

    @staticmethod
    def order_by(list_target, func_obj):
        """
            通用的升序排列方法
        :param list_target: 需要排序的数据
        :param func_obj: 排序的逻辑
                函数(参数) --> int/float
        """
        for item in range(len(list_target) - 1):
            for item1 in range(item + 1, len(list_target)):
                if func_obj(list_target[item]) > func_obj(list_target[item1]):
                    list_target[item], list_target[item1] = list_target[item1],\
                                                            list_target[item]

