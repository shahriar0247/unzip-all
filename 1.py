import zipfile
import os
import time
import psutil



def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size

def filenamechange(filename):
    print(" /// Creating new file name for "+ filename)
    try:
        filename = filename[:-1] + str(int(filename[-1:]) + 1)
    except:
        filename = filename + " 2"
    print(" /// New file name is "+filename)
    return filename

def filecheck(filename, filesize):
    if filename in os.listdir():

        if get_size(filename) == filesize:
            print("Same file exists")
        else:
            print(filesize)
            filecheck(filenamechange(filename), filesize)
    else:
       
        zip_ref.extractall(filename)


while True:
    hdd = psutil.disk_usage('/')
    diskspace = hdd.free
    print(" --- Disk space available: "+ str(diskspace) +" bytes")
    time.sleep(1)
    files = os.listdir()
    for file in files:
        if file[-4:] == ".zip":   
            print(" \\\ Unzipping "+ file)
            with zipfile.ZipFile(file, 'r') as zip_ref:
                filesize = 0
                for a in zip_ref.infolist():
                    filesize = filesize + a.file_size
                if filesize > diskspace:
                        print(" --- Not enough space for "+ file)
                        print(" --- Available " + str(diskspace) + " bytes. Required "+ str(filesize) + " bytes")
                else:
                    filename = file[:-4]
                    filecheck(filename, filesize)
            os.remove(filename +".zip")    
                



