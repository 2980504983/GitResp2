"""
    背景属性:
        背景图片加载相较于img是更加快的
        1 背景颜色:
            background-color: red;

        2 背景图片:
        (用多张图片元素也就是img来显示图片效率并不高,因为每有一个img浏览器就要进行查找解析下载渲染操作,所以img一多
        非常浪费时间并且网速要求很高,因此可以采用将多张图片先合成一张,在设置到背景中来提升效率):
            1 设置背景图片:
                background-image: url("路径"),如果路径中出现中文或空格需要加引号

            2 设置背景图片的重复方式:
                默认背景图片从元素的左上角显示, 如果图片尺寸与元素尺寸不匹配时,就会出现以下情况:
                    1 如果元素尺寸大于图片尺寸,会自动重复平铺,直至铺满整个元素
                    2 如果元素储存小于图片尺寸,图片默认存元素左上角开始显示,超出部分不可见

                    backgound-repeat:repeat/repeat-x/repeat-y/no-repeat
            3 取值:
                repeat: 默认值 沿水平和垂直方向重复平铺
                repeat-x: 沿x轴重复平铺
                repeat-y: 沿y轴重复平铺
                no-repeat: 不重复平铺

        3 设置背景图片的显示位置:
            默认显示在元素左上角
            background-position: x y;

            取值方式:
                1 像素值:
                    设置背景图片的在元素坐标系中的起点坐标

                2 方位值:
                    水平: left/center/right
                    垂直: top/center/bottom
                    注: 如果只设置某一个方向的方位值,另外一个方向默认为center

        4 精灵图技术:
            为了减少网络请求, 可以将所有的小图标拼接在一张图片上,一次网络请求全部得到,借助于background-position进行背景图片位置的调整,实现
            显示不同的图标

        5 设置背景图片的尺寸:
            background-size:width height;
            
            取值方式:
                1 像素值
                2 百分比

    背景属性简写:
        backgroud:color url("") repeat position;


"""