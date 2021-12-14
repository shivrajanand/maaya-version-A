from speakcommand import *
import pwinput

def authentication():
    password = "hithisisshiva"
    print("Enter your password\n")
    speak("please authenticate yourself")
    #code = getpass("Enter here: ", stream="*")
    code = pwinput.pwinput(mask="*")
    if password == code:
        check = True
        # print("Unlocked")
    else:
        check = False
        # print("Wrong passs")


    return check