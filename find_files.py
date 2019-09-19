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
    else:
        print("This path doesn't exist")


# Test case 1
suffix, path = ".c", "./testdir"
print("\nThe files with suffix {} in path {}:".format(suffix, path))
find_files(suffix, path)

# Test case 2
suffix, path = ".m", "./testdir"
print("\nThe files with suffix {} in path {}:".format(suffix, path))
find_files(suffix, path)

# Test case 3
suffix, path = ".c", "./test"
print("\nThe files with suffix {} in path {}:".format(suffix, path))
find_files(suffix, path)



