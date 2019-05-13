import os
import shutil


def clear(path):
    # 删除文件夹
    shutil.rmtree(r"automationdemo.github.io\Android\batfile\data")
    # 删除文件
    # os.remove()

    file = open(path, 'w')
    file.truncate()


if __name__=="__main__":
    path = r"automationdemo.github.io\Android\batfile\file.bat"
    clear(path)