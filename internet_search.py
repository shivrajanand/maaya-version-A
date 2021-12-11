import wikipedia
from speakcommand import *
import webbrowser

webbrowser.register(
    "chrome",
    None,
    webbrowser.BackgroundBrowser(
        "C:\Program Files\Google\Chrome\Application//chrome.exe"
    ),
)

def wikisearch(query):
    speak("Searching wikipedia...")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to wikipedia...")
    speak(results)
    
def i_search(query):
    url = "https://www.google.com.tr/search?q={}".format(query)
    webbrowser.get("chrome").open_new(url)