"""
    梨视频爬取思路:
        1 将视频详情页的url解析到
        2 对视频详情页的url进行请求
        3 在视频详情页的页面源码中进行全局搜索,发现没有找到video标签
            1 视频是动态加载出来的
            2 动态加载数据的方式:
                1 ajax
                2 js
        4 在页面源码中搜索,定位到视频地址(存在于一组js代码中)
            用正则将视频地址解析出来(不能用xpath,xpath只能用于标签类数据也就是html数据)

    异步爬虫:
        实际开发中其实很少用到异步爬虫,因为如果数据量不是非常非常大,等一下下也是没关系的
        毕竟,如果你爬取的太快,对网站的负载还是很大的(应付面试)

        1 基于线程池的异步爬虫
        2 基于单线程+多任务的异步爬虫

        多线程多任务也行(但是大部分时候没必要,前面就很够了)
        ...

    Flask的基本使用:
        也是一个框架,这里用flask搭建一个简单的服务器
        1 环境安装:
            pip install flask
        2 创建一个py文件用于写服务器代码

    线程池:
        from multiprocessing.dummy import Pool
        pool = Pool(3)
        pool.map(callback, alist)


    单线程+多任务异步协程 pip install asyncio:
        特殊的函数：
            如果一个函数的定义被async修饰后,则该函数就成了一个特殊的函数
            特殊之处：
                该特殊的函数被调用后,函数内部的实现语句不会理解执行
                该特殊的函数被调用后，会返回一个协程对象(没有返回值也会返回协程对象)
        协程对象：
            对象,通过特殊函数的调用返回一个协程对象
            携程 == 特殊函数 == 一组指定的操作
            协程 == 一组指定的操作
        任务对象：
            任务对象就是一个高级的协程(任务对象就是对协程对象的进一步封装)
            任务 也是一组指定的操作,但是它的功能比协程对象多一些
            创建一个任务对象：
            任务对象的高级之处:
                可以给任务对象绑定回调：
                    回调函数的参数只可以有一个,表示的就是该回调函数的调用者(任务对象)
                    使用回调函数的参数调用result,返回的就是任务对象表示的特殊函数的返回值(return 内容)
                    回调函数的执行时机：
                        在该任务被执行完毕后,才可以调用回调函数


        事件循环对象：
            也是一个对象
            作用：
                可以将多个任务对象注册/装载到事件循环对象中
                如果开启了事件循环后,则其内部注册/装载的任务对象表示的指定操作就会被异步执行
            创建事件循环对象：
            注册且启动方式：
            
        wait方法的作用:
            让任务列表中的对象可被挂起,只有任务对象被赋予了可被挂起的权限后,该任务对象才可以被挂起
            挂起:
                将当前的任务对象交出cpu时间片
                
        注意事项(重要):
            在特殊函数内部不可以出现不支持异步模块的对应的代码,否则会中断整个异步效果,例如,你不能用time模块中的sleep,只能用asyncio提供的sleep
            (await asyncio.sleep())
            
        await关键字:
            在特殊函数内部,凡是阻塞操作,都要用await进行修饰,否则阻塞操作会被跳过
            
    
    aiohttp:
        因为requests不支持异步操作,要实现异步网络请求就可以用aiohttp
        aiohttp就是一个支持异步的网络请求模块
        pip3 install aiohttp
        使用代码:
            1 写出一个大致的架构:
                async def get_request(url):
                    # 实例化一个请求对象
                    async with aiohttp.ClientSession() as sess:
                        # 调用get发起请求,返回一个响应对象
                        # get/post(url, headers, params/data, proxy)
                        async with sess.get(url=url) as response:
                            # text()获取了字符串形式的响应数据
                            # read()获取了byte类型的响应数据
                            page_text = response.text()
                            return page_text
            2 补充细节
                在阻塞操作前加上await关键字
                在每一个with前加上async
                
            3 完整代码:
                async def get_request(url):
                
                    # 实例化一个请求对象
                    async with aiohttp.ClientSession() as sess:
                    
                        # 用asyncio内置的sleep暂停两秒查看异步效果
                        await asyncio.sleep(2)
                        
                        # 调用get发起请求,返回一个响应对象
                        # get/post(url, headers, params/data, proxy)
                        async with await sess.get(url=url) as response:
                        
                            # text()获取了字符串形式的响应数据
                            # read()获取byte类型的响应数据
                            page_text = await response.text()
                            return page_text
                            
    多任务爬虫的数据解析:
        1 一定要使用任务对象的回调函数实现数据解析
        2 因为多任务的架构中数据的爬取是封装在特殊函数中的,我们一定要保证数据请求结束后,在实现数据解析
        
    使用多任务的异步协程爬取数据实现套路:
        1 先试用requests模块将带请求数据对应的url封装到一个列表中 (同步的操作,先发起requests请求将需要的url都爬下来放到列表中)
        2 在使用aiohttp模式将列表中的url进行异步的请求和数据解析 (异步的操作,创建多个异步爬虫将列表中的url进行异步爬取)
                
            
        
        
        
        
    这里的实例在后面几页中,结合后面的例子看



"""
import asyncio


async def get_request(url):
    print(url)
    return 'bobo'


# 参数t就是回调函数的调用是也就是任务对象
def task_callback(t):
    # result返回的是特殊函数的返回值bobo
    print('t.result是', t.result)
    pass


if __name__ == '__main__':
    # 创建一个协程对象
    c = get_request('www')

    # 创建一个任务对象,任务对象就是对协程对象的进一步封装
    task = asyncio.ensure_future(c)

    # 给task绑定一个回调函数
    task.add_done_callback(task_callback)


    # 创建事件循环对象
    loop = asyncio.get_event_loop()

    # 将任务对象注册到事件循环中且开启事件循环
    loop.run_until_complete(task)
