# pip install speechrecognition pyaudio setuptools pyttsx3 pockesphinx
import speech_recognition as sr
import pyttsx3 as pt
import webbrowser
import projects.musiclib as musiclib
import requests

recognizer=sr.Recognizer()
engine=pt.init()
newsapi="e797a936cd7146269cf81367d4320854"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def proccessCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com") 
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/") 
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com") 
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclib.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r=requests.get(" https://newsapi.org/v2/top-headlines?country=us&apiKey=e797a936cd7146269cf81367d4320854")
        if r.status_code==200:
            data=r.json()
            articles=data.get('articles',[])
            for arti in articles:
                print(arti['title'])
    else:
        # let open ai handle 
        print("something went wrg") 
                
if __name__=="__main__":
    speak("Initializing Elsa...") 
    print("recognizing...")
    while True:
        # listen for wake up word Elsa
        r = sr.Recognizer()
        
        try:
            with sr.Microphone() as source:
                print("Listening!...")
                audio = r.listen(source,timeout=2,phrase_time_limit=2)
            word=r.recognize_google(audio)
            # print(word)
            if(word.lower()=="elsa"):
                speak("Ya")
                # listen for command 
                with sr.Microphone() as source:
                    print("Elsa active...")
                    audio = r.listen(source)
                    command=r.recognize_google(audio)
                    
                    proccessCommand(command)
                    
        except Exception as e:
            print("error; {0}".format(e))
            

    
