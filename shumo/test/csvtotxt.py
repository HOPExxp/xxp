#原封打印
fo = open(r"detailsdata.csv", "r")
ls = []
for line in fo:
    line = line.replace("\n","")
    #每次加入一行数据
    ls = line.split(",")
    lns = ""
    #打印输出一行的内容
    # for s in ls:
    #     lns += "{}\t".format(s)
    # print(lns)
    print(type(ls))
fo.close()