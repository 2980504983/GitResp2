"""
    验证码:
        1 图片验证码:
            1 什么是图片验证码:
                区分用户是计算机还是人的全自动程序
            2 验证码的作用:
                防止恶意破解密码，刷票，论坛灌水，刷页
            3 图片验证码在爬虫中的使用场景:
                注册，登录，频繁发送请求时，服务器弹出验证码进行验证
            4 图片验证码的处理方案:
                手动输入，使用图像识别引擎进行解析，打码平台(爬虫常用的验证码解决方案)

        2 图片识别引擎(ocr):
            是指使用扫描仪或数码相机对文本资料进行扫描成图像文件，并对图像文件进行分析，自动
            识别获取文字及版面信息的软件

            1 什么是tesseract:
                 tesseract 一个开源支持多种语言的ocr
                 地址: https://github.com/tesseract-ocr/tesseract

            2 图像识别引擎的安装:
                1 引擎的安装:
                    windows: 在github中wiki中找到exe下载，完成后记得将tesseract执行文件
                             的目录加入PATH中，方便后续调用
                    linux: sudo apt-get install tesseract-ocr

                2 python库的安装:
                    pip3 install pillow 用于打开图片文件
                    pip3 install pytesseract 用于从图片中解析数据

            3 图像识别引擎的使用:
                github项目的readme中有

            4 图片识别引擎的使用扩展:
                如果数据都是中文，可以尝试中国的ocr，对中文的支持会更好

        3 打码平台:
            1 常见打码平台:
                云打码，极速打码
            2 云打码官方接口:
                1 indetify:传入图片的响应二进制数即可
                2 indetufy_by_filepath:传入图片的路径即可识别
                其中字节需要配置的地方是:
                    username = ''  用户名
                    password = ''  密码
                    appid = 可以不用设置
                    appkey = 可以不用设置
                    codetype = 验证码类型

            3 常见验证码种类:
                1 url地址不变，验证码不变:
                    将图片下载下来，通过打码平台即可解决
                2 url地址不变，验证码变化:
                    这种验证码的思路一般是通过cookie来实现的，在提交验证码时保持cookie的一致性
                    ，对此可以使用requests.session来解决
                    也可以用selenium截屏在通过打码平台实现，这种方法虽然写的多，思路简单

"""