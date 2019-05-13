# -*- encoding: utf-8 -*-
import xlwt  # 需要的模块


def txt_xls(filename, xlsname):
    """
    :文本转换成xls的函数
    :param filename txt文本文件名称、
    :param xlsname 表示转换后的excel文件名
    """
    try:
        f = open(filename,encoding="utf-8")
        xls = xlwt.Workbook()
        # 生成excel的方法，声明excel
        sheet = xls.add_sheet('sheet1', cell_overwrite_ok=True)
        x = 0
        while True:
            # 按行循环，读取文本文件
            line = f.readline()
            if not line:
                break  # 如果没有内容，则退出循环
            for i in range(len(line.split('\t'))):
                item = line.split('\t')[i]
                items=item.split(":")
                print(items[1])
                sheet.write(x, i, items[0])  # x单元格经度，i 单元格纬度
            x += 1  # excel另起一行
        f.close()
        xls.save(xlsname)  # 保存xls文件
    except:
        raise


if __name__ == "__main__":
    filename = "E:/test.txt"
    xlsname = "E:/test.xlsx"
    txt_xls(filename, xlsname)
