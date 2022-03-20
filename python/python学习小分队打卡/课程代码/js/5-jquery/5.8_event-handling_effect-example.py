"""
    11 jQuery事件处理:
        1 文档加载完毕:
            原生js方法: window.onload
            jQuery:
                1 $(document).ready(function(){
                    //文档加载完毕后执行
                })

                2 $().ready(function(){
                    //文档加载完毕后执行
                })

                3 $(function(){
                    //文档加载完毕后执行
                })
            区别:
                文档加载完毕,原生的只能出现一次,如果有两个后面的会覆盖前面的.
                而jq中的不会,可以出现多次,不会覆盖

        2 事件绑定方式:
            1 on('事件名称', function),最新版本
            2 bind('事件名称', function)
            3 .事件名称(function)

        3 this:
            表示事件的触发的对象,在jquery中可以使用,注意类型转换,原生中直接用this就行了
            但是在jq中要先用 $(this) 将this转化成jq对象
"""