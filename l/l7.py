#1
import random
import time

def show_running_time(start_time):
    difference = time.time() - start_time
    minutes = difference/60
    print("%.2f minutes" % minutes)

def show_running_time_indefinetly(a, b):
    start_time = time.time()
    while True:
        time.sleep(random.randint(a, b))
        show_running_time(start_time)

# show_running_time_indefinetly(1,2)

#4
import os
import json
import hashlib

def get_file_md5_sha256(file_path):
    try:
        md5 = hashlib.md5()
        sha1 = hashlib.sha256()
        f = open(file_path,"rb") 
        while True:
            data = f.read(4096)
            if len(data)==0: 
                break
            md5.update(data)
            sha1.update(data)
        f.close()
        return (md5.hexdigest(), sha1.hexdigest())
    except:
        return ""

def file_details(file_path):
    name = os.path.basename(file_path)
    sha256, md5 = get_file_md5_sha256(file_path)
    stats = os.stat(file_path)
    size = stats.st_size
    creation_time = time.asctime(time.gmtime(stats.st_ctime))
    abs_path = os.path.abspath(file_path)
    return {"name":name,"sha256":sha256,"md5":md5,"size":size,"creation_time":creation_time,"abs_path":abs_path}

def dir_files_details(dir_path):
    files_details = []
    files_paths = [path for path in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, path)) == True]
    for file_path in files_paths:
        files_details.append(file_details(os.path.join(dir_path,file_path)))
    return files_details

print(dir_files_details("/BHD/Personal/Pythoning/l"))

