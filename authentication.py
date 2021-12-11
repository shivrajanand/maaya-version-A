from speakcommand import *

def authentication():
    password = "correct_password"
    print("Enter your password\n")
    speak("please authenticate yourself")
    code = input("Enter here: ")

    if password == code:
        check = True
    else:
        check = False


    return check
    