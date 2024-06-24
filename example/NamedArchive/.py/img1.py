import os
import shutil

def sort_and_move_files(source_dir):
    # 循环遍历源文件夹的所有文件
    for filename in os.listdir(source_dir):
        # 文件后缀获取
        suffix = filename.split('.')[-1]
        # 排除.bat文件
        if suffix == "bat":
            continue
        # 新文件夹路径
        folder = os.path.join(source_dir, suffix)
        # 若文件夹不存在，则创建新的文件夹
        if not os.path.exists(folder):
            os.mkdir(folder)
        # 获取新文件夹内的文件数量以进行自增文件命名
        existing_files = os.listdir(folder)
        num_existing_files = len(existing_files)
        # 创建新的文件名和路径
        new_filename = str(num_existing_files+1) + "." + suffix
        new_path = os.path.join(folder, new_filename)
        # 移动文件
        shutil.move(os.path.join(source_dir, filename), new_path)

source_dir = r"D:\Github\awesomeTools\example\NamedArchive"  # 更改为你的源文件夹路径
sort_and_move_files(source_dir)