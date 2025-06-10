import speech_recognition as sr
import wikipedia
import numpy
import pyttsx3
import pyjokes
import twilio
import os
import subprocess
import datetime
import time
import webbrowser
import wolframalpha
import requests
import tkinter
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')
def speak(text):
    engine.say(text)
    engine.runAndWait()
def greetings():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Hello, Goodmorning!")
        print("Hello, Goodmorning!")
    elif hour>=12 and hour<17:
        speak("Hello, Goodafternoon!")
        print("Hello, Goodafternoon!")
    else:
        speak("Hello, Goodevening!")
        print("Hello, Goodevening!")
    aname=("Ultron")
    speak("I'm your Assistant ")
    speak(aname)
    print("I'm your Assistant",aname)
def username():
    speak("What's your name?")
    uname= takeCommand()
    speak("welcome")
    speak(uname)
    print("Welcome")
    print(uname)
    speak("What can I do for you,")
    speak(uname)

def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio= r.adjust_for_ambient_noise(source, duration=2)
        audio= r.listen(source)
    try:
        print("Recognizing...")
        speech=r.recognize_google(audio, language='en-us')
        print("User said:\n",speech)
    except Exception as e:
        print(e)
        print("I'm sorry. I don't understand.")
    return speech
if __name__=='__main__':
    clear= lambda:os.system('cls')  #will clear commands before execution of this python file
    clear()
    greetings()
    username()
    while True:
        query= takeCommand().lower()
        if 'wikipedia' in speech:
            speak('Searching wikipedia...')
            speech=speech.replace("wikipedia","")
            results=wikipedia.summary(speech,sentences=4)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in speech:
            speak('here you go to youtube')
            print('opening...')
            webbrowser.open("youtube.com")
        elif 'open google' in speech:
            speak('Opening google')
            print('opening...')
            webbrowser.open("google.com")
        elif 'open geeksforgeeks' in speech:
            speak('Opening geeksforgeeks')
            print('opening...')
            webbrowser.open("geekforgeek.com")
        elif 'open stackoverflow' in speech:
            speak('opening it for you')
            print('opening....')
            webbrowser.open("stackoverflow.com")
        elif 'the time' in speech:
            current_time= datetime.datetime.now().current_time("%H:%M:%S")
            speak("The time is{current_time}")
            print("the time is",current_time)
        elif 'send a mail' in speech or 'send mail' in speech:
            try:
                speak('what should I send?')
                print('What should I send?')
                content=takeCommand()
                print(content)
                speak('Whom should I send this to?')
                print('Whom should I send this to?')
                to=takeCommand()
                sendEmail(to,content)
                speak('The email has been sent')
                print('The email has been sent')
            except Exception as e:
                print(e)
                speak("I'm not able to send this e-mail")
                print("I'm not able to send this e-mail")
        elif 'how are you?' in speech:
            speak("I'm fine,Thank you!")
            print("Im fine, Thank you!")
            speak("How are you doing?")
            print("How are you doing?")
        elif 'fine' in speech or 'good' in speech or'great' in speech:
            speak("Well, that's good to hear")
            print("Well, that's good to hear")
        elif 'not good' in speech or 'bad day' in speech:
            speak("Oh, Don't worry I'm sure everything will be fine" )
            print("Oh, Don't worry I'm sure everything will be fine")
        elif "call me" in speech or "change my name to" in speech:
            speech=speech.replace('change my name to',"")
            uname=speech
        elif "change name" in speech or " can I call you?" in speech:
            speak("What would you like to call me?")
            print("What would you like to call me?")
            aname=takeCommand()
            speak(f"Hey, I'm {aname}")
            print("Hey I'm ", aname)
        elif 'joke' in speech:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())
        elif "Who made you" in speech or " who created you" in speech:
            speak("I was created by Gurseerat Kaur")
            print("I was created by Gurseerat Kaur")
        elif "search" in speech or "play" in speech:
            speech=speech.replace("search","")
            speech=speech.replace("play","")
            webbrowser.open(speech)
        elif "who I am" in speech or "who am I" in speech:
            speak("I would like to think that you're human")
            print("I would like to think that you're human")
        elif "love" in speech:
            speak("Love is nothing but a game between two people. It can be beautiful and sad depending upon the feelings of the players.")
            print("Love is nothing but a game between two people. It can be beautiful and sad depending upon the feelings of the players.")
        elif 'why were you made' in speech or 'reason for you' in speech:
            speak("I'm a mini project for Gurseerat Kaur")
            print("I'm a mini project for Gurseerat Kaur")
        elif 'where is'in speech:
            speech=speech.replace("where is","")
            location=speech
            speak(location)
            print(location)
            webbrowser.open("https://www.google.nl/maps/place/"+location+"")
        elif 'I love you' in speech:
            speak("Aww, I'm flattered.")
            print("Aww, I'm flattered.")
        elif 'will you be my girlfriend' in speech or 'will you my boyfriend' in speech:
            speak("I'm sorry. I'm sure you will find a human.")
            print("I'm sorry. I'm sure you will find a human.")
    time.sleep(3)































































