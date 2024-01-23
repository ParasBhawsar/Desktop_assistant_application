from distutils.cmd import Command
from tkinter import *
from tkinter import messagebox
import datetime
from unicodedata import name
from unittest import result
from flask import request
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import ctypes
from keyboard import press_and_release
import pywhatkit as pwt
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
voices = engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning")
    elif hour >= 12 and hour < 16:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("hello i am Ging, how can i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"you said: {query}\n")

    except Exception as e:

        print("please say again...")
        return "none"
    return query

def click():
    while True:
     query = takeCommand().lower() 

     if 'temperature of' in query:
        url = f"https://www.google.com/search?q={query}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temperature = data.find("div", class_ = "BNeawe").text
        speak(f"the temperature is {temperature} celcius")

     elif 'my location' in query:   
        ip_adr = requests.get("https://api.ipify.org").text
        url = "https://get.geojs.io/v1/ip/geo/"+ip_adr+".json"
        geo_q = requests.get(url)
        geo_d = geo_q.json()
        state = geo_d['city']
        country = geo_d['country']
        print(f"you are now in {state , country} .")
        speak(f"you are now in {state , country} .")

     elif 'microphone in meet' in query:
        press_and_release('ctrl + d')

     elif 'camera in meet' in query:
        press_and_release('ctrl + e')

     elif 'chat in meet' in query:
        press_and_release('ctrl + alt + c')

     elif 'raise hand in meet' in query:
        press_and_release('ctrl + alt + h')

     elif 'participant in meet' in query:
        press_and_release('ctrl + alt + p')

     elif 'open whatsapp web' in query:
        webbrowser.open("https://web.whatsapp.com/")

     if 'hi Ging' in query:
        speak('hi how are you')

     elif 'i am fine' in query:
        speak('good to here that')

     elif 'how are you' in query:
        speak('i am fine, thank you')

     elif 'where do you live Ging' in query:
        speak('in your device haha')

     elif 'bye' in query:
            speak("Ging exiting, bye master")
            exit()

     elif 'song' in query:
            song = query.replace("song", "")
            url = 'https://open.spotify.com/search/' + song
            webbrowser.open(url)

     elif 'copy' in query:
            press_and_release('ctrl + c')
            speak('copied')

     elif 'cut' in query:
            press_and_release('ctrl + x')

     elif 'underline' in query:
            press_and_release('ctrl + u')

     elif 'bold text' in query:
            press_and_release('ctrl + b')

     elif 'italic text' in query:
            press_and_release('ctrl + i')

     elif 'undo' in query:
            press_and_release('ctrl + z')

     elif 'print' in query:
            press_and_release('ctrl + p')

     elif 'open files' in query:
            press_and_release('ctrl + o')

     elif 'select all' in query:
            press_and_release('ctrl + a')

     elif 'align center' in query:
            press_and_release('ctrl + e')

     elif 'justify' in query: 
            press_and_release('ctrl + j')

     elif 'align left' in query:
            press_and_release('ctrl + l')

     elif 'align right' in query:
            press_and_release('ctrl + r')

     elif 'increase font size' in query:
            press_and_release('ctrl + shift + >') 

     elif 'decrease font size' in query:
            press_and_release('ctrl + shift + <')  

     elif 'subscript' in query:
            press_and_release('ctrl + =')

     elif 'save' in query:
            press_and_release('ctrl + s')

     elif 'new file' in query:
            press_and_release('ctrl + n')

     elif 'close' in query:
            press_and_release('alt + f4')

     elif 'screenshot' in query:
            press_and_release('win + prtscn')

     elif 'lock my device' in query:
            ctypes.windll.user32.LockWorkStation()

     elif 'shut down my device' in query:
            os.system("shutdown /s /t 1")

     elif 'new folder' in query:
            press_and_release('ctrl + shift + n')

     elif 'directions' in query:
        speak("enter source")
        source = takeCommand()
        speak("enter destination")
        destination = takeCommand("enter destination: ")
        webbrowser.open(f"https://www.google.com/maps/dir/{source}/{destination}")

     elif 'on youtube' in query:
            src = query.replace("on youtube", "")
            url = "https://www.youtube.com/results?search_query=" + src
            webbrowser.open(url)

     elif 'pause' in query:
            press_and_release('k')

     elif 'play' in query:
            press_and_release('k')

     elif 'mute' in query:
            press_and_release('m')

     elif 'unmute' in query:
            press_and_release('m')

     elif 'next video' in query:
            press_and_release('shift + n')

     elif 'open miniplayer' in query:
            press_and_release('i')

     elif 'caption' in query:
            press_and_release('c')

     elif 'speed up' in query:
            press_and_release('shift + >')

     elif 'slow down' in query:
            press_and_release('shift + <')

     elif 'forward' in query:
            press_and_release('l')

     elif 'backward' in query:
            press_and_release('j')

     elif 'full screen' in query:
            press_and_release('f')
    
     if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

     elif 'search' in query:
            search = query.replace("search", "")
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            speak("Here\'s what i found about" + search)

     elif 'open' in query:
            website = query.replace("open ", "")
            url = f'https://www.{website}.com'
            webbrowser.open(url)

     elif 'open google' in query:
            webbrowser.open("https://www.google.com")

     elif 'new tab' in query:
            press_and_release('ctrl + t')

     elif 'close tab' in query:
            press_and_release('ctrl + w')

     elif 'switch to tab' in query:
            no = query.replace("switch to tab", "")
            press_and_release(f"ctrl + {no}")

     elif 'open incognito' in query:
            press_and_release('ctrl + shift + n')

     elif 'exit' in query:
            speak('Ging is exiting, bye master !')
            exit()

def btn_clicked():
    print("Button Clicked")


window = Tk()
window.title('Ging : Desktop Assistant')                                        # TTTLE : Displayed at the top of gui window
window.geometry("1000x600")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

# entry0_img = PhotoImage(file = f"img_textBox0.png")                             # Textbox : For entering whatsapp message
# entry0_bg = canvas.create_image(
#     732.0, 316.0,
#     image = entry0_img)

# entry0 = Entry(
#     bd = 0,
#     bg = "#ebebeb",
#     highlightthickness = 0)

# entry0.place(
#     x = 550.0, y = 243,
#     width = 364.0,
#     height = 144)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = window.destroy,                                                   # EXIT Button : Exits the GUI when clicked
    relief = "flat")

b0.place(
    x = 673, y = 523,
    width = 115,
    height = 52)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = click,                                                   # SPEAK Button : Should Start the assistant program when clicked (add_program_path)
    relief = "flat")

b1.place(
    x = 648, y = 456,
    width = 167,
    height = 64)

background_img = PhotoImage(file = f"background.png")                           # Background Image 
background = canvas.create_image(
    493.5, 302.5,
    image=background_img)

window.resizable(False, False)
window.mainloop()