import os


def find_files(suffix, path):
    if os.path.isdir(path):
        my_list = os.listdir(path)
        for item in my_list:
            item_path = os.path.join(path, item)
            if os.path.isfile(item_path) and item.endswith(suffix):
                print(item_path)
            elif os.path.isdir(item_path):
                find_files(suffix, item_path)
            else:
                continue


find_files(".c", "./testdir")

