import os
path = r'C:\Users\Angie\Desktop\text.txt'
with open(path) as fp:
    for cnt, line in enumerate(fp):
        print("Line {}: {}".format(cnt, line))