"""
    js的命名规则一般是小驼峰:

    
    二维数组:
        同python
    string对象:
        创建string对象:
            1 var str='我是一个字符串';
            2 var str2= new String('我也是一个字符串');
        也有下标
        属性:
            lenth
        方法:
            装换字母大小写:
                toUpperCase()转大写字母
                toLowerCase()转小写字母
                转换后的字符串,不影响原来的字符串

            获取字符或字符编码:
                charAt(index) 获取指定下标的字符
                charCodeAt(index) 获取指定下标的字符编码

            获取指定字符的下标:
                indexOf(str, fromindex)
                    获取指定字符的下标,从前向后查询,找到就返回
                    fromindex表示起始下标默认为0
                    查找失败返回-1
                
                lastIndexOf(str,fromindex)
                    同上面一样,只不过是从后向前查找

                substring(start, end)
                    截取字符,不包含end

                substr(start,len)
                    开始下标,长度

                split(param)
                    分割字符串,将字符串按照指定字符进行分割,以数组形式返回分割结果
                    param分割符

            匹配:
                正则表达式对象 RegExp
                    1 语法:
                        var reg1 = /正则表达式主体/修饰符(可选);
                        var reg2 = new RegExp('匹配模式','修饰符');

                    2 属性:
                        lastIndex:
                            可读可写,表示下一次匹配的起始索引
                        注:
                            1 默认情况下, 正则表达式对象不能重复调用方法,如果重复调用,会报错
                            2 由于 lastIndex 保存再一次匹配的起始下标,重复调用时,不能保证每次都从下标0开始验证,可以手动调整lastIndex为0
                            3 只有正则对象设置全局匹配g,lastIndex属性才起作用

                        方法:
                            test(str) 验证字符串中是否存在满足正则匹配模式的内容,存在则返回true
                            不存在返回false, 参数为要验证的字符串



                


                

                

"""