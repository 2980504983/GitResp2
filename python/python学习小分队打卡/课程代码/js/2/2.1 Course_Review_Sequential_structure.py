"""
    js回顾:
        1.定义
        2 使用:
            元素的属性
            通过标签<script></script>内嵌
            外部引入 script src='文件路径'
        3 语法:
            1 定义一个变量
            2 var a = 1;
            3 数据类型:
                ...

        4 通过js操作元素的过程:
            1 获取这个元素对象
            2 给元素实现效果

        5 js函数:
            function a(){
                js代码块
            }

    流程控制:
        1 顺序结构:
            从上到下一次执行执行代码语句

        2 分支/选择结构:
            if else
            注: 空 undefined NaN null 0 都是false, 
                特殊写法,{}可以省略,省略后if就只控制后面的第一行代码

        3 switch语句:
            语法:
            switch(value){

                case 值1:
                // value与值1匹配全等时,执行代码段
                break; //结束匹配

                default:
                // 所有case匹配失败后执行的代码段
                break;
            }

            使用:
                switch语句用于值得匹配

    循环控制:
        分类:
            1 while循环(先判断,条件成立才执行):
                while(循环条件){
                }
            
            2 do-while(先执行,在判断循环条件):
                do{
                    循环体;
                    更新循环变量
                }while(循环条件);

            3 for循环
                for(定义循环变量;循环条件;更新循环变量){
                    循环体;
                }

            4 循环控制:
                1 break
                2 continue
                3 循环嵌套




        
"""