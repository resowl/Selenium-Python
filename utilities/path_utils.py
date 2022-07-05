import os


def get_file(file_name):

    full_file = os.path.abspath(os.path.join('.\..\\test_data_sheets', file_name))
    print(full_file)
    return full_file


def get_current_working_directory():
    path = os.getcwd()
    print("Current path is-->", path)
    return path

def get_the_path_of_the_file(file_name):
    file_path = os.chdir(os.path.dirname(os.path.abspath(file_name)))
    print("Path of the file is--->", file_path)
    return file_path



