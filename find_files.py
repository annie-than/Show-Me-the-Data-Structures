import os

item_list = []

def find_files(suffix, path):
    if os.path.isdir(path):
        my_list = os.listdir(path)
        for item in my_list:
            item_path = os.path.join(path, item)
            if os.path.isfile(item_path) and item.endswith(suffix):
                item_list.append(item_path)
            elif os.path.isdir(item_path):
                find_files(suffix, item_path)
            else:
                continue
        return item_list
    else:
        print("This path doesn't exist")


# Test case 1
suffix, path = ".c", "./testdir"
item_list = []
print("\nThe files with suffix {} in path {}:".format(suffix, path))
print(find_files(suffix, path))

# Test case 2
suffix, path = ".m", "./testdir"
item_list = []
print("\nThe files with suffix {} in path {}:".format(suffix, path))
print(find_files(suffix, path))

# Test case 3
suffix, path = ".c", "./test"
item_list = []
print("\nThe files with suffix {} in path {}:".format(suffix, path))
print(find_files(suffix, path))



