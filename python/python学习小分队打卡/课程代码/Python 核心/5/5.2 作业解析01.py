"""
    生成器(惰性操作)
        优势：
            节省内存
        缺点：
            获取结果不灵活(不能使用索引/切片访问)
        解决：
            惰性操作 -> 立即操作
            list_result = list(generator_result)
"""

