import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning sir. I am your assistand Aleksa. How may I help you?")
    elif hour < 18:
        speak("Good afternoon sir. I am your assistand Aleksa. How may I help you?")
    else:
        speak("Good evening sir. I am your assistand Aleksa. How may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query

    except Exception:
        print("Say that again please...")
        return ""

if __name__ == "__main__":
    wishMe()
while True:
    query = takeCommand().lower()

    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")

    elif 'play music' in query:

        music_file = "C:\\Users\\DELL\Music\\Bye Bye Bye - Deadpool _ English Song.mp3"
        os.startfile(music_file)

    elif 'time' in query :
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(strTime)
        speak(f"The time is {strTime}")

    elif'open code' in query:
        codePath="C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)


       

    elif 'exit' in query or 'quit' in query:
        speak("Goodbye sir")
        break
