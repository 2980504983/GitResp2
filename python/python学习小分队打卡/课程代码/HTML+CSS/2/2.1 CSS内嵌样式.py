"""
    CSS基础使用:
        CSS介绍:
            css全称为层叠样式表,与html相辅相成,实现网页排版布局与样式美化,
            css主要格式: select选择器{property属性:值},如果没有写在元素里,就要指定元素,
            如果写在标签里了,就不用选择了

        css使用方法(不用选择器):
            1 行内样式/内联样式(不推荐):
                借助于style标签属性,为当前的元素添加样式声明
                <标签名 style="样式声明">

                css样式声明:
                    style="属性":值;"属性":值

                常用css属性:
                    设置文本颜色(color: red;)
                    设置背景颜色(background-color:green;)
                    设置字体大小(font-size:32px;)

            2 内嵌样式(需要选择器,少量页面中使用):
                借助于style标签,在html文档中嵌入css样式代码,可以实线css样式与html标签之间
                的分离,同时借助css选择器到html中匹配元素并应用样式

                具体做法:
                    #id{属性:值},这种方法就是在头部中创建样式,并描述body中的元素


            3 外联样式表(外部引入,项目中使用):
                为样式单独创建一个文件或文件夹,用的时候直接导入,文件后缀名是.css
                <link rel="stylesheet" href="样式文件url或路径" type="text/css">
                好处:
                    1 样式与页面完全分离,内嵌样式只能算是半分离,行内样式最糟糕一般应该不会这么写
                    2 多个页面可以导入相同的样式文件,可以作用与多个页面,
                    3 可以离线
                有多个页面,就用外部引入,一个页面的话内嵌样式就行了,行内样式不推荐

        样式表特征:
            1 层叠性:
                多组样式可以共同作用与一个元素

            2 继承性:
                后代元素可以继承祖先元素中的某些样式,被包裹的元素是子,大部分文本属性都
                是可以被继承的

            3 样式表的优先级:
                优先级用来解决样式冲突问题,同一元素同一样式,在不同地方进行设置,最终选用哪一种,
                样式,最终由样式表的优先级来决定

                1 离元素最近的样式优先级最高(就近原则)
                2 文档内嵌与外链样式表,优先级一致,同样就近
                3 浏览器默认样式和继承样式优先级较低

        css选择器:
            1 作用:
                匹配文档中某些元素作为应用样式

            2 分类:
                1 标签选择器(效率低,比较慢,全局性比较重可以用):
                    根据标签名匹配文档中所有元素,  标签名{属性:值}
                2 id选择器:
                    根据id属性值匹配文档中的唯一元素,  #id属性值{属性:值}
                    id可以由数字,字母,下划线组成,不能以数字开头
                3 class选择器/类选择器(复用):
                    根据元素的class属性值匹配相应的元素,class属性值可以重复使用,实现样式的复用
                    .class的属性值{},
                    需要在每个元素内声明输入某个class,也就是加上class='class的属性值'
                    class的属性值相当于一个共性的名字,多个元素取相同的class属性值,可以在.class
                    的属性值{}中一起修改样式

                    特殊用法:
                        1 类选择器与其它选择器结合使用(标签与类选择器结合式,标签在前,类选择器在后)
                            例如: a.c1{}  就表示a标签下,所有类属性值为c1的标签
                        2 class属性值可写多个,共同应用类选择器的样式
                            例如:
                                .c1{}
                                .c2{}
                                这两个可以作用于同一元素

                4 群组选择器:
                    为一组元素统一设置样式,类似class选择器,class可以理解为自己创建一个组,让元素加进去,然后一起修改,
                    而群组选择器,则是直接根据多种不同的标签直接修改,感觉有点像复数版的标签选择器
                    selector1(标签1),selector2(标签2)...{}

                5 后代选择器:
                    分组用逗号,空格表后代
                    匹配满足选择器的所有后代元素(包含子元素和孙子元素)
                    selector1 selector2...{}  匹配selector1中所有满足selector2的后代元素

                6 子代选择器:
                    匹配满足选择器的所有直接子元素:
                    selector1>selector2{}

                7 伪类选择器:
                    为元素的不同状态分别设置样式,必须与基础选择器结合使用
                    分类:
                        :link 超链接访问前的状态
                        :visited 超链接访问后的状态
                        :hover 鼠标滑过的状态
                        : active 鼠标第安安不抬起时的状态(激活)
                        : focus 焦点状态(文本框被编辑时就称为获取焦点)
                    使用:
                        a:hover{},如果要将link,visited,hover,active,都作用与一个超级链接,必须按照前面的顺序书写,不然不起作用

            3 选择器的优先级:
                数值越大,优先级越高,获取元素速度越快,效率越高,但是仍然不推荐用行内样式,因为它把页面与样式混在一起了,这点相当致命,因此整合考量,id选择器最推荐
                标签选择器, 1
                伪类选择器, 10
                id选择器, 100
                行内样式, 1000
                    




"""