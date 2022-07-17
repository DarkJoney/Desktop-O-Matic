import os, shutil, time
import eyed3
from pyexpat import model
from PIL import Image, ExifTags
from PIL.ExifTags import TAGS


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


def checkIfCameraPresentInExif(file):
    img = Image.open(file)
    img_exif = img.getexif()
    try:
        data = img.getexif()[272]
        print(data)
        return data
    except KeyError:
        return False

def defineIfAudioIsMusic(file):
    audiofile = eyed3.load(file)
    print(audiofile.tag.artist)
    print(audiofile.tag.album)#separate