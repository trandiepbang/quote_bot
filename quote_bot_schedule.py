import schedule
import time
import redis
import os
from quote_bot import startJob
from config import *

schedule.every(SENT_INTERVAL).minutes.do(startJob)
# schedule.every().day.at("22:30").do(reset)

while True:
    schedule.run_pending()
    time.sleep(1)
