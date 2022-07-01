import os, shutil, time


def locate_desktop():
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    #print("The Desktop path is: " + desktop)
    return desktop

def get_files(fFormat, desktopPath):
    foundFiles = []
    for file in os.listdir(desktopPath):
        if file.endswith(fFormat):
            print(os.path.join(desktopPath, file))
            foundFiles.append(os.path.join(desktopPath, file))
    return foundFiles

def move_to_folder(targets, fFormat):
    targetFormat =  (str(fFormat).replace(".","")).upper()
    path = locate_desktop() + "\\" + targetFormat
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)
        print("The new directory is created!")
    else:
        print("it exists!")
    for i in targets:
        print(i)
        #to do copy here

def move_to_folder_timeline(targets, fFormat):
    targetFormat =  (str(fFormat).replace(".","")).upper()
    path = locate_desktop() + "\\" + targetFormat
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)
        print("The new directory is created!")
    else:
        print("it exists!")
    for i in targets:
        print(i)
        f_mod_time = os.path.getmtime(i)
        time_stamp = time.strftime("%Y-%m-%d", time.strptime(time.ctime(f_mod_time)))
        print(time_stamp)
        isExist = os.path.exists(path  + "\\" + time_stamp)
        
        if not isExist: 
            os.makedirs(path  + "\\" + time_stamp)
            print("The new directory is created!")
        else:
            print("it exists!")
        #to do copy here