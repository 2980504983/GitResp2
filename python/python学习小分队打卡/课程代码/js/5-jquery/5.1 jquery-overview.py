"""
    jQuery简介:
        1 介绍:
            jQuery是js的工具库,对原生js中的DOM操作,事件处理,包括数据处理等进行封装

        2 使用:
            1 引入:
                先引入jquery文件,才能使用jquery语法

            2 工厂函数() - $():
                $() 函数用于获取元素节点，创建

        3 原生js对象与jQuery对象:
            原生js对象与jquery对象的属性和方法不能混用,可以根据需要,相互转换:
                1 原生js对象转换成jq对象:
                    $(原生js对象) 返回jq对象

                2 jq对象转js对象(jq对象是一个类似数组的类型,他里面是包含js对象的,且一般下标位置都是0):
                    1 根据标取元素,取出即为原生对象
                        var div = $("div")[0];

                    2 使用jq的get(index)方法获取原生对象
                        var div2 = $("div").get(0);

                3 导入jq后就不要在使用原生了,没有必要转来转去,除非需要用到document中的方法

        4 jq获取元素:
            $(选择器)
                1 基础选择器:
                    id:
                        $(#id)
                    标签:
                        $("div")
                    类选择器:
                        $(".c1")
                    群组选择器:
                        $("body,p,h1)

                2 层级选择器:
                    后代选择器:
                        $("div .c1") 注意空格表示后代
                    子代选择器:
                        $("div>span")
                    相邻兄弟选择器:
                        $("h1+p")  匹配选择器1后的第一个兄弟选择器,同时要求兄弟元素满足选择器2
                    通用兄弟选择器:
                        $("h1~h2")  匹配选择器1后所有满足选择器2的兄弟选择器

                3 过滤选择器:
                    需要结合其它选择器使用

                    :first
                        匹配第一个元素:
                            $("p:first")

                    :last
                        最后一个

                    :odd
                        奇数下标对应元素

                    :even
                        偶数下标对应元素

                    :eq(index)
                        匹配指定下标的元素

                    :lt(index)
                        匹配下标小于index的元素

                    :gt(index)
                        匹配下标大于index的元素

                    :not(选择器)
                        除()中选择器外,其它元素

                4 属性选择器:

                    [attrName]:
                        匹配包含指定属性的元素

                    [attrName=value]/[attrName=""value]:
                        匹配某一个属性值为value的元素

                    [attrName^=value]:
                        匹配属性值以指定元素开头的元素

                    [attrName$=value]:
                        匹配属性值以指定元素结尾的元素

                    [attrName*=value]
                        匹配属性值包含指定字符的元素

                5 子元素过滤选择器:
                    :first-child
                        匹配第一个子元素
                    :last-child

                    :nth-child(n)
                        匹配第n个子元素,n从1开始

        5 操作元素内容:
            html()  等价于原生innerHtML
            text()  innerText
            val()   value

        6 操作元素属性:
            一个参数表示读取,两个参数表示设置
            1 attr('attrName', 'value')
                设置或读取标签属性

            2 prop('attrName', 'value')
                设置或读取标签属性,平时基本没区别,但在读取或设置表单元素选中状态checked时,必须用prop方法获取状态,
                attr()不会监听按钮选中状态的改变,只看标签属性checked是否书写

            3 removeAttr('attrName', 'value')
                移除指定属性

        7 操作标签样式:
            1 为元素添加id/class属性,对应选择器样式
            2 针对类选择器,提供操作class属性值的方法
                addClass('className')  添加指定的类名
                removeClass('className')  移除指定类型,如果参数省略表示清空class属性值
                toggleClass('className')  如果元素存在指定类名并移除,不存在则添加

            3 操作行内样式:
                css('属性名', '属性值')  设置一个行内样式
                css(json对象)  设置一组行内样式

        8 根据层级结构获取元素:
            1 parent()
                返回父元素
            2 parents('selector')
                返回满足选择器的祖先元素
            3 children()/children('selector')
                返回所有子元素/返回所有满足选择器的子元素
            4 find('seletor')
                返回所有的后代元素
            5 next()/next('selector')
                返回下一个兄弟元素/返回下一个兄弟元素,必须满足选择器
            6 prev()/prev('selector')
                返回前一个兄弟元素/返回前一个兄弟元素,必须满足选择器
            7 siblings()/siblings('selector')
                返回所有的兄弟元素/返回所有满足选择器的兄弟元素

        9 元素的创建,添加,删除:
            1 创建:
                $('标签语法') 返回创建好的元素
            var div = $("<div></div>");  //创建元素

            2 添加至页面:
                1 作为子元素添加:
                    $obj.append(newobj);  //在$obj的末尾添加子元素newobj,也就是作为最后一个子元素添加
                    $obj.prepend(newobj);  //作为第一个子元素添加至$obj中

                2 作为兄弟元素添加:
                    $obj.after(newobj);  //在$obj的后面添加兄弟元素
                    $obj.before(newobj);  //在$obj的前面添加兄弟元素

                3 移除元素:
                    $obj.remove(); 移除$obj

        10 操作元素



                    



                    
"""