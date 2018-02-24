import glob
import os
import random, string
import random
from config import *
def getPhotos(mypath):
    return glob.glob(mypath + "/*.*")

def getFullLink(photo):
    _link = HOST + 'photo/'+ os.path.basename(photo) + '?v=' + getRandomName(5)
    return _link

def getRandomName(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def pickRandomly(photos):
    return random.choice(photos)