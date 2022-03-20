"""
    文本属性:
        1 字体相关:
            1 设置字体大小:
                font-size: 20px;
            2 设置字体粗细程度:
                font-weight:normal; (normal 默认值等价于400 ; bold 加粗等价于700)
            3 设置斜体:
                font-style:italic;
            4 设置字体名称(类型):
                font-family:Arial,"黑体","宋体";
                取值:
                    1 可以指定多个字体名称作为备选字体,使用逗号隔开
                    2 如果字体名称为中文,或者名称中出现了空格,必须使用引号
            5 字体属性简写:
                font: style weight size family;

    文本样式:
        1 文本颜色:
            color:red;
        2 文本装饰线:
            text-decoration:none;
            取值：
                underline
                overline
                line-throught 删除线
                none 
        3 文本内容的水平对齐方式:
            text-align:center;
            取值:
                left
                center
                right
        4 行高:
            line-height:30px;
            文字在当前行中永远垂直居中,因此如果line-height等于外部其它元素的height,文字就也在外面元素中垂直居中了

            特殊:
                line-height可以采用无单位数值,代表当前字体大小的倍数,以此计算行高

"""