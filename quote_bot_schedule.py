import schedule
import time
import redis
import os

client_redis = redis.StrictRedis(host='localhost', port=6379, db=0)

def resetData ():
    global client_redis
    client_redis.delete("is_sent")
    print(" #deleted ")

def reset():
    print("I'm working...")
    resetData()

def start_job():
    os.system('./run_rain_bot.sh')

schedule.every(3).minutes.do(start_job)
schedule.every().day.at("22:30").do(reset)

while True:
    schedule.run_pending()
    time.sleep(1)
