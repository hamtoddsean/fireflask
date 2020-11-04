import requests,json,csv,datetime,os,time,sys
#from telebot import apihelper
import traceback#,telebot
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMPLEMENTOFDEFAULT"

#  CHAT_ID1 = -1001127170747



#import atexit

# v2.x version - see https://stackoverflow.com/a/38501429/135978
# for the 3.x version
from apscheduler.scheduler import Scheduler
from flask import Flask

app = Flask(__name__)

  
  
  



def send_message(text):
  token='802247903:AAHLYB3LODL0pW7kwjkf3encZGqGGuSB5GE'

  chat_id='564189421'
  api_url = "https://api.telegram.org/bot{}/".format(token)
 
  params = {'chat_id': chat_id, 'text': str(text)}
  method = 'sendMessage'
  resp = requests.post(api_url + method, params)
  return resp


#def appdo():
#  v=1
#  text='doing this'
#  while v==1:
#    v=send_message(text)
#    print(v)
#    time.sleep(300)

def appdo():
  v=1
  text='doing this'
#  while v==1:
  v=send_message(text)
  print(v)
#    v=1
#    time.sleep(300)




cron = Scheduler(daemon=True)
# Explicitly kick off the background thread
cron.start()

@cron.interval_schedule(minutes=5)
def job_function():
    appdo()


# Shutdown your cron thread if the web process is stopped
#atexit.register(lambda: cron.shutdown(wait=False))

if __name__ == '__main__':
    app.run()

