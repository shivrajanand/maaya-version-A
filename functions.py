#importing modules
import datetime
from speakcommand import *

def present_date_time():
    present = datetime.datetime.now()
    present_time = present.strftime("%d/%m/%Y %H:%M:%S")

    return present_time

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 5 and hour < 12:
        speak("Good morning boss")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening boss")
