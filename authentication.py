from speakcommand import *
import pwinput

def authentication():
    password = "mypass"
    print("Enter your password\n")
    pass
    pass
    pass
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