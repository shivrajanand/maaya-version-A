#importing modules
import pyttsx3
import speech_recognition as sr

#setting up engines and voices
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty("voice", voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def printvoices():
    for i in range(len(voices)):
        print(voices[i].id, end="\n")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1.5

        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        print("Maaya: Say that again please")
        speak("Say that again please")
        return "None"
    return query