import glob
import os
import random
from config import *
def getPhotos(mypath):
    return glob.glob(mypath + "/*.*")

def getFullLink(photo):
    return HOST + os.path.basename(photo)

def pickRandomly(photos):
    return random.choice(photos)