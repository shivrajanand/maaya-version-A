import os
from speakcommand import *


def unautorizedaccess():
    os.system('Rundll32.exe user32.dll,LockWorkStation')
    speak("Authentication unsuccessful. Unauthorized user detected. Initiating security protocols.")
    # alarm = "C:\\Users\\Dell\\Desktop\\Coding\\python\\maaya\\securityalarm.mp3"
    os.startfile("securityalarm.mp3")
    


