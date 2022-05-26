from base64 import encode
import os
import sys
import re


# dir=os.getcwd().split('\\')[-1]
# # 列出目录
# for name in os.listdir(os.getcwd()):
#     if(re.search("\.pdf$", name)):
#         # print(name.split('_')[-1])
#         newname=dir+'_'+name.split('_')[-1]
#         # print(newname)
#         os.rename(name,newname)
# print('ok')
Directory = os.getcwd()

# 提示输入想遍历的文件夹路径

for root, dirs, files in os.walk(Directory):
    # print(root)
    dir = root.split('\\')[-1]
    for name in dirs:
        print("Directory:", name)  # 打印文件夹名
    for name in files:
        if(re.search("\.doc|\.pdf$", name)):
            print(os.path.join(root, name))  # 打印文件名
            newname = dir+'_'+name.split('_')[-1].strip('实验名称：')
            print(newname)
            os.rename(os.path.join(root, name), os.path.join(root, newname))

# print())
# 重命名
# os.rename("test","test2")

print("重命名成功。")

# # 列出重命名后的目录
# print "目录为: %s" %os.listdir(os.getcwd())
