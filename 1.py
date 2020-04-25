import zipfile
import os
import time
import psutil



def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size

def filenamechange(filename):
    try:
        filename = filename[:-1] + str(int(filename[-1:]) + 1)
    except:
        filename = filename + " 2"

    return filename

def filecheck(filename, filesize):
    if filename in os.listdir():

        if get_size(filename) == filesize:
            pass
        else:
            filecheck(filenamechange(filename), filesize)
    else:
       
        zip_ref.extractall(filename)


while True:
    hdd = psutil.disk_usage('/')
    diskspace = hdd.used
    time.sleep(1)
    files = os.listdir()
    for file in files:
        if file[-4:] == ".zip":   
            with zipfile.ZipFile(file, 'r') as zip_ref:
                for a in zip_ref.infolist():
                    if a.file_size > diskspace:
                        pass
                    else:
                        filename = file[:-4]
                        filecheck(filename, a.file_size)
                



