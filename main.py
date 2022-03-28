from functions import *
from speakcommand import *
from introduce import *
from internet_search import *
from authentication import *
from security_protocol import *
import random
from Music.playmusic import *

if __name__ == '__main__':
    check = authentication()

    if check == True:
        speak("Authentication successfull")

    else:
        # speak("Authentication unsuccessful. Unauthorized user detected. Initiating security protocols.")
        # print("\n"*100)
        # print("UNAUTHORIZED USER! Starting Security Alarm")
        unautorizedaccess()
        quit()  #authorization failed so AI System closed


    print("MAAYA ACTIVATING..........................")
    speak("ACTIVATING MAAYA SYSTEM....")
    print("\n"*100)
    speak("MAAYA SYSTEM ACTIVATED....")
    print("**********************    M.A.A.Y.A. Activated    **********************")
    wishme()

    #Initiating logfile to start saving all data of user
    logfile = open("logfile.txt", "a+")
    logfile.write("\n\n\n\n\n ***************************************************************************** \n")
    logfile.write("Starting: ")
    logfile.write(present_date_time())

    #Initiating infinite loop to serve AI speaking
    while True:
        query = takeCommand().lower()

        logfile.write("\n")
        logfile.write("User: ")
        logfile.write(query)

        ########### Closing AI system code for system ###########
        if "shutdown maiya" in query:
            speak("Goodbye boss! Shutting down MAAYA System!")

            logfile.write("\nM.A.A.Y.A.: Goodbye boss! Shutting down MAAYA System!")
            logfile.write("\nClosing: ")
            logfile.write(present_date_time())
            logfile.close()

            print("\n"*100)
            speak("Saving all log files")
            speak("Removing temporary files")
            speak("Please wait")
            speak("uploading all log files to remote repository")
            speak("Shutdown Successfull")
            print("M.A.A.Y.A. System Shutdown Successfull")
            
            quit() #closing 'AI system

        elif "introduce yourself" in query:
             introduce()
             logfile.write("\nM.A.A.Y.A: Introduction")

        elif "search from wikipedia" in query:
            wikisearch(query)

        elif "search internet" in query:
            i_search(query)

        elif "play music" in query:
            play_music()

        elif "show all available songs" in query:
            print_music_available()

        elif "open youtube" in query:
             webbrowser.get("chrome").open_new("youtube.com")
        elif "open stack overflow" in query:
             webbrowser.get("chrome").open_new("stackoverflow.com")
        elif "open whatsapp web" in query:
             webbrowser.get("chrome").open_new("https://web.whatsapp.com/")
        elif "open gmail" in query:
             webbrowser.get("chrome").open_new("https://mail.google.com/mail/u/0/#inbox")
        else:
            print()
    





