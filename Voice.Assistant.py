import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import pyaudio
import pathlib
import calendar
import pyjokes
import psutil

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def joke():
    for i in range(5):
        speak(pyjokes.get_jokes()[i])


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage)

    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!,hope you are having a good day sir")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!,hope you are having a good day sir")

    else:
        speak("Good Evening!,Hope you are having a good day sir")

    speak("My name is SINISTER Sir. I am your personal assistant... Please tell me ,how may I help you sir")


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


##########################################################################
# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('youremail@gmail.com', 'your-password')
#     server.sendmail('youremail@gmail.com', to, content)
#     server.close()
#############################################################################

if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("ok sir")
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("ok sir..")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("ok sir..")
            webbrowser.open("google.com")


        elif 'open stack over flow' in query:
            speak("ok sir..")
            webbrowser.open("stackoverflow.com")


        elif 'open linkedin' in query:
            speak("ok sir..")
            webbrowser.open("linkedin.com")


        elif 'open weather report' in query:
            speak("ok sir..")
            webbrowser.open("www.accuweather.com")


        elif 'open stack overflow' in query:
            speak("ok sir..")
            webbrowser.open("stackoverflow.com")

        elif 'what is the date today' in query:
            strday = datetime.date.today()
            speak(f"Sir, today's date is  {strday}")

        elif ' are you there' in query:
            speak("Yes Sir, at your service")

        elif 'tell me some jokes' in query:
            speak("sure sir.")
            joke()



        # elif 'play music' in query:
        #     music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
        #     songs = os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        # elif 'what is the day today' in query:
        #     my_date = date.today()
        #     a = calendar.day_name[my_date.weekday()]
        #     speak(f"Sir, the time is {a}")

        elif 'open pycharm' in query:
            pyloc = "C:/Program Files/JetBrains/PyCharm Community Edition 2020.2.1/bin/pycharm64.exe"
            os.startfile(os.path.normpath(pyloc))

        elif 'open V S Code' in query:
            vsloc = "C:/Users/noida/AppData/Local/Programs/Microsoft VS Code/Code.exe"
            os.startfile(vsloc)

        elif 'open c drive' in query:
            cdrive = "C:/"
            os.startfile(cdrive)

        elif 'open d drive' in query:
            ddrive = "D:/"
            os.startfile(ddrive)

        elif 'open  utorrent' in query:
            utt = "C:/Users/noida/AppData/Roaming/uTorrent/uTorrent.exe"
            os.startfile(utt)

        elif 'open github ' in query:
            speak("ok sir..")
            webbrowser.open("github.com")

        elif 'today news' in query:
            speak("ok sir, opening the newswebsite")
            webbrowser.open("news.google.com")

        elif 'open map' in query:
            speak("Opening map sir")
            webbrowser.open("maps.google.com")

        elif 'switch on light' in query:
            speak("switching on the lights sir")

        elif 'switch on fan' in query:
            speak("switching on the fan sir")

        elif 'switch on ac' in query:
            speak("switching on the Air conditioner  sir")

        elif 'switch on light' in query:
            speak("switching on the lights sir")

##############################################################################################################
# # elif 'email to receiver' in query:
#     try:
#         speak("What should I say?")
#         content = takeCommand()
#         to = "receiver"
#         sendEmail(to, content)
#         speak("Email has been sent!")
#         except Exception as e:
#         print(e)
#         speak("Sorry sir. I am not able to send this email")
#################################################################################################################

