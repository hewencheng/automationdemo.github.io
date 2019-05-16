import hashlib
import os
def get_info_data(filenames,file_path,file_path2):
    num = 0
    for val in filenames:
        with open(file_path + "/" + val, 'rb') as f:
            md5obj = hashlib.md5()
            md5obj.update(f.read())
            _hash = md5obj.hexdigest()
        print(str(_hash).upper() + ".wav")
        num += 1
        oldname = file_path + "/" + val
        newname = file_path2 + "/" + str(_hash).upper() + ".wav"
        os.rename(oldname, newname)
    print(num)


if __name__ == '__main__':
    file_path = r"C:\Users\v_wenche\Desktop\test"
    file_path2 =r"C:\Users\v_wenche\Desktop\test2"
    filenames = os.listdir(file_path)
    data_list=get_info_data(filenames,file_path,file_path2)
