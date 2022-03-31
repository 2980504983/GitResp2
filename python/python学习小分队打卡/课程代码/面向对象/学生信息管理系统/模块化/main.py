"""
    入口模块

    python第一次运行程序时，会把代码转换成字节码并储存，但是并不会储存第一个执行的文件，也就是
    不会生成 main.pyc文件，所以为了性能考虑，最好不要再main中放大段代码
"""
import ui


view = ui.StudentManagerView()
view.main()
