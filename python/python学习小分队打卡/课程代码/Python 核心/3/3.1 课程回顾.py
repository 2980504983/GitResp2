"""
    复习
        包
            定义:包含__init__.py文件的文件夹
            作用:团队分工，结构清晰
            导入: import 包.模块 as 变量
                 from 包.模块 import 成员
                 from 包.模块 import *
            原理: import sys
                 sys.path + from 的路径可以正确的定位到文件，导包才成功。
        异常处理
            异常: 运行时遇到错误,后续代码不在执行，返回个调用者
            处理: 将异常流程(向上翻)转为正常流程(向后走)
            语法:
                 try:
                    可能出错的语句
                except 错误类型1:
                    处理逻辑
                except 错误类型2:

                else:
                    不错后执行的代码
                finally:
                    无论错不错都执行

"""