import os
path = r'C:\Users\Angie\Desktop\text.txt'
with open(path) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        print("Line {}:{}".format(cnt, line.strip()))
        line = fp.readline()
        cnt += 1
        


