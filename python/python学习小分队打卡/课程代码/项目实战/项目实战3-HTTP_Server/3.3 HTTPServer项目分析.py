"""
    http_server项目分析:
        功能:
            http_server部分(http协议是基于应用层的tcp协议的):
                获取http请求
                解析http请求
                将请求发送给WebFrame
                从WebFrame接收反馈数据
                将数据组织为Response格式发送给客户端

            WebFrame部分(后端应用程序，后端工程师做的，http_server(web_server)一般有现成的不用我们自己写，一般有nginx, apache)：
                从http_server接收具体请求
                根据请求进行逻辑处理和数据处理
                将需要的数据反馈给http_server

        特点:
            采用http_server 和 应用处理分离的模式，大大降低耦合度
            采用了用户配置文件的思路 (我们不能替用户决定的部分可以传参，但如果参数太多，就可以采用另一种方法，也就是配置文件)
            WebFrame部分采用模拟后端框架的处理方法

        技术点:
            http_server 部分需要与两端建立通信
            WebFrame部分采用多路复用接收并发请求
            数据传递使用json接收

        交互数据格式协议:
            httpserver -> webframe {method:'get', info:'/'} (请求类型，请求内容)
            webframe -> httpserver {status:'200', data:'ccc'}  (响应情况， 数据)

        HTTPServer项目结构图.jpg



"""