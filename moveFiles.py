import os
import shutil


def moveFilesByCounter(count, src, dest):


    for subdir, dirs, files in os.walk(src):
        for file in files:
            # print os.path.join(subdir, file)
            filepath = subdir + os.sep + file

            try:
                shutil.move(filepath, dest)

                count = count -1
                if count ==0:
                    return
            
            except:
                continue

