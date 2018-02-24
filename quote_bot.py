#!/usr/bin/env python
# -*- coding: utf-8 -*-
import redis
import schedule
import time
import urllib
import requests
from config import *
from lib import *
def startJob():
    try:
        photos = getPhotos(PHOTO_FOLDER)
        selected_photo = pickRandomly(photos)
        FULL_LINK = getFullLink(selected_photo)
        # print(FULL_LINK)
        notifyChannel( { "text":FULL_LINK  , "channel": CHANNEL , "username": BOT_USERNAME } )
    except Exception , e:
        print("Something is wrong")
        print(e)

def notifyChannel(data):
    r = requests.post( WEBHOOK, json=data )
    print("#sent " , r.text)