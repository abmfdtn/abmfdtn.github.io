import os
path = "C:\\Users\\admin\\Desktop\\data1\\3"
dirs = os.listdir(path)
print(dirs)

file = None
path_start = None
for i in dirs:
    file = i
    path_start = path + "\\" + file
    print(path_start)
    os.startfile(path_start)
