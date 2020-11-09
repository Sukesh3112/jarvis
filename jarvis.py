import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)
  
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good evening")

    speak("I am Jarvis the AI assistance how may i help you ?")               

def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing ...")
        query = r.recognize_google(audio, language="en-in") 
        print(f"user said: {query} \n")
    except Exception as e:
        # print(e)
        print("say that again please ...")
        return "None"                           
    return query

if __name__ == "__main__":
    #speak("jaihabibi")
    wishMe()
    while True:
        query = takeCommand().lower()
    # logic for executing task
        if 'wikipedia' in query:
            speak('searching wikipedia ...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 5)
            speak("according to wikipedia")
            print (results)
            speak (results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")    

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open twitter' in query:
            webbrowser.open("twitter.com")  

        elif 'open stack overflow' in query:
            webbrowser.open("stack overflow.com")  

        elif 'play music' in query:
            webbrowser.open("open.spotify.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"the time is :{strTime}")   
            speak(strTime) 

        elif 'how are you' in query:
            speak("i am fine what about you ")  

        elif 'i am fine' in query:
            speak("what can i do for you")  

        elif 'i am hungry' in query:
            webbrowser.open("https://www.zomato.com/mumbai")

        elif 'order me medicines' in query:
            webbrowser.open("https://www.medlife.com/")       

        elif 'open amazon' in query:
            webbrowser.open("https://www.amazon.in/")

        elif 'open flipcart' in query:
            webbrowser.open("https://www.flipkart.com/")         
             