import os
import glob


def get_complete_path_of_the_file_to_test_in_test_data_sheets(file_name):
    full_path_of_file_to_test = os.path.abspath(os.path.join('.\..\\test_data_sheets', file_name))
    print("Full path of file to test--->", full_path_of_file_to_test)
    return full_path_of_file_to_test


def get_current_working_directory():
    path = os.getcwd()
    print("Current path is-->", path)
    return path


def get_full_path_of_a_file(file_name):
    path = (os.path.realpath(file_name))
    print("Full path of the file is--->", path)
    return path

# get_full_path_of_a_file("config.py")
# get_current_working_directory()
# get_complete_path_of_the_file_to_test_in_test_data_sheets("sample.xml")
