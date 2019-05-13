limit = 1000000     #切割后单个文件的最大行数
file_count = 0
line_list =[]
#打开需要切割的文件
with open(r'D:\workspace\Fileprocessing\file\data\1\crash\All-testlog.txt','r', errors='ignore') as f:
    for line in f:              #读取每一行
        line_list.append(line)      #把每一行数据分别加入到line_list列表里面
        if len(line_list)<limit:        #如果line_list列表的长度‘小’于指定的切割后单个文件的最大行数
            continue
        file_name = './data/log' + str(file_count) + '.txt'         #如果line_list列表的长度‘等’于指定的切割后单个文件的最大行数
        with open(file_name,'w') as file:                           #写入文件
            for new_line in line_list[:-1]:
                file.write(new_line)
            file.write(line_list[-1].strip())
            line_list = []
            file_count += 1
if line_list:                                                       #文件读取完后，如果line_list列表里仍有数据未保存，就把数据写入一个文件
    file_name = './data/log' + str(file_count) + '.txt'
    with open(file_name,'w') as file:
        for line in line_list:
            file.write(line)

print('done')