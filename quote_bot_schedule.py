import schedule
import time
import redis
import os
from quote_bot import startJob

schedule.every(1).minutes.do(start_job)
# schedule.every().day.at("22:30").do(reset)

while True:
    schedule.run_pending()
    time.sleep(1)
