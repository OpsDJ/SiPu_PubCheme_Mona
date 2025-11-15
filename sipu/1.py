import sys
import os

def resource_path(relative_path):
    """获取资源文件的绝对路径，兼容打包后的 exe"""
    if getattr(sys, 'frozen', False):  # PyInstaller 打包后
        base_path = sys._MEIPASS
    else:  # 脚本运行时
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

# 动态路径
not_find_path = resource_path("not_find.png")
print(not_find_path)