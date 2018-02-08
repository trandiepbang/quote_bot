import glob
import os
import random, string
import random
from config import *
def getPhotos(mypath):
    return glob.glob(mypath + "/*.*")

def getFullLink(photo):
    folder = os.path.dirname(photo)
    new_path = folder + '/' + getRandomName(20) + '.jpg'
    path_local = os.rename(photo, new_path)
    _link = HOST + 'photo/'+ os.path.basename(new_path)
    return _link

def getRandomName(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def pickRandomly(photos):
    print(photos)
    return random.choice(photos)