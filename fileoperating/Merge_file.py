import sys

import os
import os.path
import time
time1=time.time()
##########################合并同一个文件夹下多个txt################
def MergeTxt(filepath,outfile):
    k = open(filepath+outfile, 'a+')
    for parent, dirnames, filenames in os.walk(filepath):
        for filepath in filenames:
            txtPath = os.path.join(parent, filepath)  # txtpath就是所有文件夹的路径
            f = open(txtPath)
            ##########换行写入##################
            # k.write(f.read()+"\n")
            k.write(f.read())
    k.close()

    print("finished")


if __name__ == '__main__':
    filepath="E:/Test/文件合并/"
    outfile="result.txt"
    MergeTxt(filepath,outfile)
    time2 = time.time()
    print(u'总共耗时：' + str(time2 - time1) + 's')