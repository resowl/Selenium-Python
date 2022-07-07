import os


def get_file(file_name):

    full_file = os.path.abspath(os.path.join('.\..\\test_data_sheets', file_name))
    print(full_file)
    return full_file



