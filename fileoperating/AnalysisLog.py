import os
from os.path import join
from tqdm import tqdm
import shutil
import time
time1=time.time()


def backtrace(filepath):
    # os.remove(filepath + '/crash.txt')
    with open(filepath + '/test.txt', 'r',encoding='utf-8', errors='ignore') as f:
        a = 0
        for key,line in enumerate(f):
            if "eac6d57254bd462f" in line:
                print("come here")
                a = key
                break
    f.close()
    if a != 0:
        num=a-5000
        num2=a+10000
        f.close()
        backtrace2(num, num2, filepath)
    else:
        print("no crash")


def backtrace2(num,num2,filepath):
    with open(filepath + '/crash.txt', 'w', encoding='utf-8', errors='ignore') as f:
        with open(filepath + '/test.txt', 'r',encoding='utf-8', errors='ignore') as file:
            for key, line in enumerate(file):
                if (key >= num) and (key <= num2):
                    f.writelines(line)
        file.close()
    f.close()
    time2=time.time()
    print("End"+"耗时:"+str(time2-time1)+"s")


if __name__ =="__main__":
    filepath = r'automationdemo.github.io\fileoperating\data'
    backtrace(filepath)
