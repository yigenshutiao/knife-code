import os
import os.path

# 列出当前目录下所有的文件
pwd_file = [item for item in os.listdir(os.path.realpath(".")) if os.path.isfile(item)]

# 列出当前目录下所有的目录
pwd_dir = [item for item in os.listdir(os.path.realpath(".")) if os.path.isdir(item)]

# 列出当前目录下所有的目录名与绝对路径之间的字典
pwd_dict_path = {item:os.path.realpath(item) for item in os.listdir(os.path.realpath(".")) if os.path.isdir(item)}

pwd_dict_size = {item:os.path.getsize(item) for item in os.listdir(os.path.realpath(".")) if os.path.isdir(item)}

# 文件读写demo
with open('/etc/passwd') as source, open("target.txt", 'w') as target:
    for line in source:
        data = line.split(":")
        user, home, shell = data[0], data[5], data[6].strip()
        target.write("{0},{1},{2}".format(user, home, shell))
