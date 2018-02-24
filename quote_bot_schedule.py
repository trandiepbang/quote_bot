import schedule
import time
import redis
import os
from quote_bot import startJob
from config import *

if PRODUCT is False:
    schedule.every(SENT_INTERVAL).minutes.do(startJob)
else:
    schedule.every().day.at(SENT_TIME).do(startJob)

while True:
    schedule.run_pending()
    time.sleep(1)
