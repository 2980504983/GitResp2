"""
    在selenium中用方法取数据，而不是直接用xpath取数据
        1 获取文本:
            element.text
        2 获取属性值:
            element.get_attribute('属性名')
        3 点击:
            能点击的元素才调用点击方法，如果不能点击的元素调用点击方法就会报错 el.click()
        4 send_key:
            能输入的元素才调用输入方法 el.send_key()
        5 清空输入框:
            el.clear()
"""