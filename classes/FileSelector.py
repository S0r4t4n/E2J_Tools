import glob
import os
from typing import Sequence


class FileSelector:
    def __init__(self, directory_name: str):
        if not os.path.exists(os.getcwd() + os.sep + directory_name):
            print(f"Not exist {directory_name} directory...")
            choice = input(f"Create the {directory_name} directory?[yes/no] : ")
            if choice in ['y', 'yes']:
                os.mkdir(os.getcwd() + os.sep + "directory_name")
                print(f"Create the {directory_name} directory.")
                self.path = os.getcwd() + os.sep + "directory_name"
            elif choice in ['n', 'no']:
                while True:
                    input_path = input("Input directory_name directory : ")
                    if os.path.exists(input_path):
                        self.path = input_path
                        break
                    else:
                        print(f"Not exist {input_path} directory...")
        else:
            self.path = os.getcwd() + os.sep + directory_name

    def show_files(self, extensions: Sequence[str]):
        files = []
        for e in extensions:
            files += glob.glob("*." + e)
        print(f"In {os.getcwd()} :")
        for file in files:
            print(file.replace(self.path, ''))

    def get_file_path(self, extensions: Sequence[str]) -> str:
        self.set_current_directory()
        files = []
        for e in extensions:
            files += glob.glob("*." + e)
        print(f"In {os.getcwd()} :")
        for i in range(0, len(files)-1):
            print(f"{i + 1} : {files[i].replace(self.path, '')}")
        selected_file_num = input(f"Select file[1-{len(files)-1}] : ")
        return files[int(selected_file_num) - 1]

    def set_current_directory(self):
        os.chdir(self.path)