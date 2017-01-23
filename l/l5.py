#2
import os
def read_path(path):
    if not os.path.exists(path):
        print("Invalid")
    elif os.path.isfile(path):
        file = open(path, 'r')
        print(file.read(4096))
    else:
        print(os.listdir(path))

import sys
# read_path(sys.argv[1])

#3
def write_environ(path):
    file = open(path, 'w')
    for key, value in os.environ.items():
        string = key + "\t" + value + "\n"
        file.write(string)
    file.close()

write_environ("test.txt")

#4
def browse(path, idx = 0):
    print(" " * idx + path)
    sub_list = ()
    try:
        sub_list = os.listdir(path)
    except:
        return
    for index, sub in enumerate(sub_list):
        browse(os.path.join(path, sub), idx + index)

def browse2(path, idx = 0):
    print(" " * idx + path)
    for index, sub in enumerate(os.listdir(path)):
        sub_path = os.path.join(path, sub)
        if os.path.isfile(sub_path):
            print(" " * (idx + index) + sub_path)
        else:
            browse2(sub_path, idx + index)

browse("/BHD/Personal/Pythoning")

#8
def create_file(path, filesize):
    file = open(path, 'w')
    file.write("a" * filesize)
    file.close()

def create_files(path, filecount, filesize):
    for x in range(0, filecount):
        create_file(os.path.join(path, "file"+str(x)), filesize)

def create_folders_with_files(path, filesize, filecount, dircount):
    for x in range(0, dircount):
        dir_path = os.path.join(path, "dir"+str(x))
        os.mkdir(dir_path)
        create_files(dir_path, filecount, filesize)

def create_folders_with_files_for_paths(paths, filesize, filecount, dircount):
    for path in paths:
        create_folders_with_files(path, filesize, filecount, dircount)

def create_dummy_tree(path, tree_depth, filesize , filecount, dircount):
    current_depth = 1
    os.mkdir(os.path.join(os.path.curdir, path))
    create_files(path, filecount, filesize)
    paths = [path]

    while current_depth < tree_depth:
        create_folders_with_files_for_paths(paths, filesize, filecount, dircount)
        new_paths = []
        for path in paths:
            new_paths.extend([os.path.join(path, x) for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))])
        paths = new_paths
        current_depth += 1

create_dummy_tree("test", 4, 1024, 3, 3)