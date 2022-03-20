"""
    1 JavaScript概述:
        简称js, 是浏览器解释型语言, 嵌套在html文件中交给浏览器解释执行,主要用来实现网页的动态效果
        ,用户交互及前后端的数据传输等

    2 javascript组成:
        1 核心语法 -ES5 规范了javascript的基本语法
        2 浏览器对象模型 -BOM 提供了一系列操作浏览器的方法
        3 文档对象模型 -DOM 提供了一系列操作文档的放法

    3 使用方法:
        1 元素绑定事件:
            1 事件: 指用户的行为
            2 事件处理:
            3 常用事件:
            4 语法:
            实现点击按钮在控制台输出:
                <button onclick="console.log('Hello world');">点击</button>

        2 文档内嵌:
            <script type="text/javascript">
                alert("网页警告框");
            </scrit>
            注意:
                 <script></script>标签可以书写在文档任意位置,书写多次,一旦加载到script标签就会立即执行内部的javascript代码,
                 因此不同的位置回影响代码最终的执行效果

        3 外部连接:
            创建外部的JavaScript文件xx.javascript,在html文档中使用<script src=""></script>引入
            注意:
                <script></script>既可以实现内嵌js代码,也可以实现引入外部的js文件,是只能二选一

    4 javascript常用输入输出语句:
        alert(""); 普通网页弹框
        prompt(""); 接收用户输入弹框,返回用户输入内容
        consele.log(); 控制台输出,多用于代码调试
        document.write("<h1>Hello</h1>"); 实现在动态网页中写入内容
            1 可识别html标签,脚本代码可以在文档任何地方书写,如果是普通写入(不涉及时间),区分代码的书写位置插入
            2 文档渲染结束后,再次执行此方法,会重写网页内容(原理是文档渲染结束后,在执行document.write会重新创建一个文档流,并且覆盖
                                                        上一个文档流)
    
"""