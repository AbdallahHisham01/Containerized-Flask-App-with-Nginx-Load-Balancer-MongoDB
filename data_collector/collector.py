import os
import time
import shutil

SRC_PATH = os.environ.get("SRC_PATH")
DST_PATH = os.environ.get("DST_PATH")
duration = 30  

def collect_data(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)

    if not os.path.exists(src):
        return

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dst, item)

        if os.path.isdir(src_path):
            collect_data(src_path, dest_path)
        else:
            shutil.copy2(src_path, dest_path)

while True:
    collect_data(SRC_PATH, DST_PATH)
    time.sleep(duration)

