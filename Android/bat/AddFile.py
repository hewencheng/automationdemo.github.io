import os
import time
import zipfile
import subprocess
import shutil
time1 = time.time()


def pushfile(path,list):
    for devices in list:
        print(devices)
        
        #向bat文件中写入下面命令
        with open(path,'w') as w:
            w.write('@echo off\n')
            w.write('adb -s %s shell rm /sdcard/test.txt\n' % devices)  #移除test.txt文件
            w.write('adb -s %s shell rm -r /sdcard/file\n' % devices)   #移除file文件夹
            w.write('adb -s %s shell mkdir /sdcard/file\n' % devices)   #创建file文件夹
            w.write(r'adb -s %s push automationdemo.github.io\Android\batfile\file /file'% devices+"\n")  #向手机导入文件
            w.write(r'adb -s %s push automationdemo.github.io\Android\batfile\file /sdcard/file'% devices+"\n") #向手机导入文件
            w.write(r'adb -s %s install automationdemo.github.io\Android\batfile\data\test.apk' % devices)   #向手机导入apk
            w.close()

        # 运行bat文件
        os.system(path)
        file=open(path, 'w')
        # 清空内容
        file.truncate()


def clearfile():
    shutil.rmtree(r"automationdemo.github.io\Android\file)


def un_zip():

    file_name = "test.zip"
    filename_out = r'automationdemo.github.io\Android\batfile\flie\%s'，% file_name  # 要解压的文件

    apk_name = "apk.zip"
    filename_apk = r'automationdemo.github.io\Android\batfile\flie\%s' % apk_name  # 要解压的apk文件

    filedir = r'automationdemo.github.io\Android\batfile\data'  # 解压后放入的目录
    r_out = zipfile.is_zipfile(filename_out)

    if r_out:
        fz = zipfile.ZipFile(filename_out, 'r')
        for file in fz.namelist():
            print(file)  # 打印zip归档中目录
            fz.extract(file, filedir)
    else:
        print('This file is not zip file')

    r_apk = zipfile.is_zipfile(filename_apk)
    if r_apk:
        fz = zipfile.ZipFile(filename_apk, 'r')
        for file in fz.namelist():
            print(file)  # 打印zip归档中目录
            fz.extract(file, filedir)
    else:
        print('This file is not zip file')


def devices():
    list = []
    devices = subprocess.Popen(
        'adb devices'.split(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    ).communicate()[0]
    aa = str(devices)
    bb = aa.split('\\tdevice')
    for dd in bb:
        cc = dd.split('\\r\\n')
        if cc[1] != "":
            list.append(cc[1])
    return list


if __name__ == '__main__':
    path=r"automationdemo.github.io\Android\batfile\file.bat"
    un_zip()
    list=devices()
    pushfile(path,list)
    clearfile()
    time2 = time.time()
    print(u'总共耗时：' + str(time2 - time1) + 's')