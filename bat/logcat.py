import os


def Catchlog(path):
    with open(path,'w') as w:
        w.write(r"adb logcat -v time >adb logcat -v time >C:\Users\v_wenche\Desktop\test.txt")
        w.close()
    os.system(path)

    file = open(path, 'w')
    file.truncate()


if __name__=="__main__":
    path = r"automationdemo.github.io\batfile\file.bat"
    Catchlog(path)