from os import path
import os

strpath = r"C:\Priya_Dev\sourcecode\api_ui_test_framework"

def get_file(file_name):

    data_folder_path = "test_data_sheets"

    data_folder_abs_path = path.join(path.abspath(path.curdir), data_folder_path)

    print("data_folder_abs_path -> ", data_folder_abs_path)

    list_of_files = os.listdir(data_folder_abs_path)
    for file in list_of_files:
        print("File name in loop is--->", file)
        if file_name+".json" in file:
            print("File Found ->", file)
            return path.join(data_folder_abs_path, file)