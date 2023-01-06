import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
from requests import get
import smtplib
import cv2
import sys
import time
import pywhatkit as kit
import pyautogui
import psutil
from gtts import gTTS
import pyjokes
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 179)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening4.")

    speak("how are you sir. Please tell me how may I help you")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yahan gmail id dalna hai', 'yahan gmail password dalna hai')
    server.sendmail('yahan gmail id dalna hai', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        if 1:

            query = takeCommand().lower()

            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                speak("about what you want to search on youtube")
                s = takeCommand()
                webbrowser.open(
                    "www.youtube.com/results?search_query=" + s + "")

            elif "open google" in query:
                speak("opening google sir, what should i search on google")
                cm = takeCommand().lower()
                webbrowser.open(f"{cm}")

            elif 'open stack overflow' in query:
                webbrowser.open("stackoverflow.com")

            elif 'play music' in query:
                speak("just a second sir")
                songs_dir = "E:\\music"
                songs = os.listdir(songs_dir)
                print(songs)
                os.startfile(os.path.join(songs_dir, songs[0]))

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(
                    f" its , {strTime} , sir, the weather outside is 21 degree celcius, it will be a bright suny day outside ")

            elif 'open vs code' in query:
                speak("opening visual studio sir")
                codePath = "C:\\Users\\NETCOM\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            elif 'email to' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "vashupandey872@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak(
                        "Sorry sir due to network issue. I am not able to send this email")

            elif 'open notepad' in query:
                speak("opening notepad sir")
                codePath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(codePath)

            elif 'open calculator' in query:
                speak("opening calculator sir")
                codePath = "C:\\Windows\\system32\\calc.exe"
                os.startfile(codePath)

            elif "close calculator" in query:
                speak("okay, closing calculator sir")
                os.system("taskkill /f /im calc.exe")
            elif "hey hey hey" in query:
                speak("hey hi hello how are you hahahah")

            elif "do you know jarvis" in query:
                speak("about what sir")
            elif "open visual studio" in query:
                speak("wait sir i am working on that")

            elif 'open camera' in query:
                speak("opening camera sir")
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break
                cap.release()
                cv2.destroyAllWindows()

            elif 'open facebook' in query:
                speak("opening facebook sir")
                webbrowser.open("facebook.com")

            elif "play song on youtube" in query:
                speak("about what you want to search on youtube")
                search_query = takeCommand()
                kit.playonyt("faded")

            elif "jarvis quit" in query or "javascript" in query:
                speak("as your wish sir, just a second ")
                songs_dir = "E:\\music"
                songs = os.listdir(songs_dir)
                os.startfile(os.path.join(songs_dir, songs[1]))
                time.sleep(2)
                sys.exit()

            elif "jarvis listen" in query or "listen jarvis" in query:
                speak("yes sir!")

            elif "thanks jarvis" in query or "thank you" in query:
                speak("no problem sir for you anything")

            elif "who are you" in query or "jarvis reset" in query or "what is your name" in query:
                print("iam jarvis, a virtual artificial intelligence, and iam hear to assist you with the variety of tasks, as best i can, 24 hours a day, 7 days a weak, importing all preferences from home interface, system is now fully operational")
                speak("iam jarvis, a virtual artificial intelligence, and iam hear to assist you with the variety of tasks, as best i can, 24 hours a day, 7 days a weak, importing all preferences from home interface, system is now fully operational")

            elif "close notepad" in query:
                speak("okay, closing notepad sir")
                os.system("taskkill  /f /im notepad.exe")

            elif "close google" in query or "close facebook" in query:
                speak("okay, closing google sir")
                os.system("taskkill /f /im msedge.exe")

            elif "close youtube" in query:
                speak("okay, closing youtube sir")
                os.system("taskkill /f /im chrome.exe")

            elif "close vs code" in query:
                speak("okay, closing visual studio sir")
                os.system("taskkill /f /im code.exe")

            elif "shutdown the system" in query:
                speak("shut the system under 10 seconds")
                os.system("shutdown /s /t 5")
                songs_dir = "E:\\music"
                songs = os.listdir(songs_dir)
                print(songs)
                os.startfile(os.path.join(songs_dir, songs[0]))

            elif "restart the system" in query:
                os.system("shutdown /r /t 5")
                songs_dir = "E:\\music"
                songs = os.listdir(songs_dir)
                print(songs)
                os.startfile(os.path.join(songs_dir, songs[0]))

            elif "sleep the system" in query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                songs_dir = "E:\\music"
                songs = os.listdir(songs_dir)
                print(songs)
                os.startfile(os.path.join(songs_dir, songs[0]))

            elif "where i am" in query or "where we are" in query:
                speak("let me check sir, where we are")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    country = geo_data['country']
                    speak(
                        f"sir iam not sure, but i think we are in {city} city of {country} country")
                    print("sir iam not sure, but i think we are {city}")
                except Exception as e:
                    speak(
                        "sorry sir, Due to network issue iam not able to find where we are.")
                    pass

            elif "take screenshot" in query or "take a screenshot" in query:
                speak("sir,please tell me the name for this screenshot")
                name = takeCommand().lower()
                speak("plese hold the screen sir , iam taking screenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("done sir, screenshot saved in our computer")

            elif "jarvis are you there" in query:
                print("for you sir, always")
                speak("for you sir, always")

            elif 'stop' in query or 'play' in query:
                speak('ok sir')
                pyautogui.press('space')

            elif 'volume up' in query:
                speak('volume up sir')
                pyautogui.hotkey('volumeup')
                pyautogui.hotkey('volumeup')
                pyautogui.hotkey('volumeup')

            elif 'volume down' in query:
                speak('volume down sir')
                pyautogui.hotkey('volumedown')
                pyautogui.hotkey('volumedown')
                pyautogui.hotkey('volumedown')

            elif 'switch window' in query or 'switch tab' in query:
                pyautogui.hotkey('alt', 'shift', 'tab')

            elif 'scroll up' in query:
                speak("okay sir")
                pyautogui.press('up')
                pyautogui.press('up')
                pyautogui.press('up')
                pyautogui.press('up')
                pyautogui.press('up')
                pyautogui.press('down')

            elif 'down' in query:
                speak("okay sir")
                pyautogui.press('down')
                pyautogui.press('down')
                pyautogui.press('down')
                pyautogui.press('down')
                pyautogui.press('down')
                pyautogui.press('up')

            elif 'left' in query:
                pyautogui.press('left')

            elif 'right' in query:
                pyautogui.press('right')

            elif 'inter' in query or 'wake up' in query:
                pyautogui.press('enter')

            elif 'hello jarvis' in query or 'hi jarvis' in query:
                speak("yes sir")

            elif 'how are you' in query:
                speak("i am feeling positively tip top thanks , what about you sir")

            elif 'i am also good' in query or 'also fine' in query:
                speak("thats great")

            elif 'battery percent' in query or 'battery percentage' in query:
                speak("wait sir, let me check the device")
                battery = psutil.sensors_battery()
                percent = str(battery.percent)
                print("device has been running on "+percent + "%" "battery")
                speak("device has been running on "+percent + "%" "battery")

            elif 'jarvis are you here' in query or 'jarvis are you their' in query:
                speak("offcourse sir")

            elif 'read text for me' in query:
                speak("Wait for a moment")
                fh = open("test.txt", "r")
                myText = fh.read().replace("\n", " ")

                language = 'en'

                output = gTTS(text=myText, lang=language, slow=False)

                output.save("result.mp3")
                fh.close()
                os.system("start result.mp3")
                speak(result.mp3)
            elif "joke" in query:
                speak(pyjokes.get_joke())
            elif "developer" in query or "creator" in query or "develope" in query:
                speak("my developers are shivkesh, , satvik,  harsh, , ramansh, ,akash ,here are the email id's if you want to contact them shivkeshpandey872@gmail.com , satvikpandey35@gmail.com , ramanshkala01102002@gmail.com, akash2umar@gmail.com")
          
