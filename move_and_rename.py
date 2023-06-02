import os
import shutil


def move_and_rename_file(src_path, dest_path):
    try:
        shutil.move(src_path, dest_path)
        print(f"文件成功移动并重命名为: {dest_path}")
    except Exception as e:
        print(f"移动文件时出错: {e}")

if __name__ == "__main__":
    src_path = input("请输入原始文件的路径: ")
    dest_path = input("请输入目标文件的路径: ")

    move_and_rename_file(src_path, dest_path)