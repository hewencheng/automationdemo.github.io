from openpyxl import load_workbook


def get_excel_to_txt(excel,txt):
    """
    转换excel 成txt文本
    :param excel: excel路径
    :param txt: 保存的txt路径
    :return:
    """
    wb = load_workbook(excel)
    sheet = wb.worksheets[0]
    rows = sheet.rows
    data_list = [[i.value if i .value else " " for i in item] for item in rows]
    with open(txt_path,"w+",encoding="utf-8",errors="ignore") as f:
        for data in data_list:
            text = ""
            for num in range(len(data)):
                text += data[num].strip()+" "
            f.write(text + "\n")

    return True


if __name__ == '__main__':
    #excel 文件名
    file = r"C:\Users\issuser\Documents\WXWork\1688850523260107\Cache\File\2018-10\10_26\contacts"
    excel_path = file +".xlsx"  #excel路径
    txt_path = file + ".txt"    #保存的txt路径
    get_excel_to_txt(excel_path,txt_path)