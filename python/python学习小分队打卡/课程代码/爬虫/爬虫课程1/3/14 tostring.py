"""
    etree.HTML()能够自动补全html的缺失标签
    lxml.etree.tostring 函数可以将转换的elements对象在转换回html字符串
    爬虫如果使用lxml来提取数据，应该以lxml.etree.tostring 的返回结果作为提取数据的依据
"""