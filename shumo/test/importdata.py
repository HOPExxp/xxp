# 导入csv库；
#
# 打开文件，并用csv库函数reader读入数据；
#
# csv读入的数据是一行一行的，所以通过循环语句把读到的数据放入到数组里

import csv # 必要库导入
filepath = 'detailsdata2.csv' # 定义文件名称，本文件要与当前的.py文件要在同一文件夹下，不然要用绝对路径
with open(filepath,'r') as csvfile: # 打开数据文件
    reader = csv.reader(csvfile) # 用csv的reader函数读取数据文件
    header = next(reader) # 读取数据文件的表头
    data = [] # 定义一个空数组用于保存文件的数据
    for line in reader: # 循环读取数据文件并保存到数组data中
        data.append(line) # line是个一维数组，是数据文件中的一行数据
print(header) # 表头
print(data) # 读取的二维数组