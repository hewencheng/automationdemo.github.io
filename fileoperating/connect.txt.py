import os
from os.path import join
from tqdm import tqdm

filepath = r'D:\workspace\Fileprocessing\file\data\1\merge'
#os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
filenames = os.listdir(filepath)
print(filenames)
# Tqdm 是一个快速，可扩展的Python进度条，可以在 Python 长循环中添加一个进度提示信息，
# 用户只需要封装任意的迭代器 tqdm(iterator)。
with open(filepath + '/2300zong.txt','w',encoding='utf-8') as f:
    for filename in tqdm(filenames):
        print(filename)
        file_path = os.path.join(filepath,filename)   # os.path.join合并目录
        for line in open(file_path,'r',encoding='utf-8', errors='ignore'):
            f.writelines(line)



