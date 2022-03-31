"""
    BOM:
        1 介绍:
            浏览器对象模型,浏览器的核心对象是window,而文档对象的核心对象是document

        2 window对象常用方法:
            1 网页弹框:
                window.alert()  //弹框
                window.prompt()  //带输入框的弹框
                confirm()  //确认框

            2 窗口的打开和关闭:
                window.open('url')  //新建窗口访问指定的url (这个现在用的比较少,因为这个可以被浏览器拦截)
                window.close()  //关闭当前窗口

            3 定时器方法:
                1 间歇调用(周期性定时器):
                    每隔一段时间就执行一次代码,直到被关闭
                    开启定时器:
                        var timerID = setInterval(function,interval);
                        function: 需要执行的代码
                        interval: 间隔时间,单位是毫秒
                        返回值: 定时器id

                    关闭定时器:
                        clearInterval(timerID);

                2 超时调用(一次性定时器)
                    等待多久之后执行一次代码
                    开启超时调用:
                        var timerId = setTimeout(function, timeout);
                    关闭超时调用:
                        clearTimeout(timerId);

        3 window对象常用属性:
            window的大部分属性是对象类型

            history:
                保存当前窗口访问过的url
                属性:
                    length表示当前窗口访问过的url数量

                方法:
                    back() 对应浏览器窗口的后退按钮,访问前一个url
                    forward() 对应前进按钮,访问记录中下一个url
                    go(n) 参数为number值,翻阅几条历史记录,正值表示前进,负值表示后退

            location:
                保存当前窗口地址栏的信息(url)
                属性:
                    href设置或读取当前窗口的地址栏信息
                方法:
                    reload(param) 刷新(重载页面)
                    参数为boolean, 默认false表示从缓存中加载,true强制服务器根目录加载

    
    DOM节点操作:
        文档对象模型,提供操作HTMl文档的方法
        1 节点对象:
            js对html文档中的元素,属性,文本内容甚至注释进行封装,称为节点对象,提供相关属性和方法

        2 常用节点对象:
            1 元素节点(操作标签)
            2 属性节点(操作标签属性)
            3 文本节点(操作标签的文本内容)

        3 获取元素节点:
            elems = document.getElementsById('');
            ...BytagName
            ...Byclass
            ...Byname

        4 操作元素内容:
            innerTHML: 读取或设置元素文本内容,可识别标签语法
            innerText: 设置元素文本内容,不能识别标签语法
            value: 用于读取或设置表单控件的值

        5 操作元素属性:
            elem.getAttribute('atrname');
            elem.setAttribute('attrname', 'value');
            elem.removeAttribute('attrname');

            注: h1.className = 'c1 c2 c3';

        6 操作元素样式:
            p.style.color = 'red';
            

            



            


        




"""