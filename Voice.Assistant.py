import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir... I am Sinister... How may I help you")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir ... i am sinister..how may i help you")
    else:
        speak("good evening sir...i am sinister..how may i help you ")


def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gamil.com', 'your password')
    server.sendmail('youremsil@gmail.com', to, content)
    server.close()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listering.....")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing....")
            query = r.recognize_google(audio)
            print(f"User said:{query}\n")

        except Exception as e:
            print(e)

            print("Say that again please...")
            return "None"
        return query


if __name__ == '__main__':
    wishe()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching in wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        elif 'open amazon' in query:
            webbrowser.open("amazon.com")
        elif 'play music' in query:
            music_dic = 'path'
            songs = os.listdir(music_dic)
            print(songs)
            os.startfile(os.path.join(music_dic, songs[0]))
        elif 'time now' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        # elif 'open code' in query:
        #     codepath=""
        elif 'email to atul' in query:
            try:
                speak("what should i say ?")
                content = takecommand()
                to = "atul168908@gmail.com"
                sendemail(to, content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry sir i am not able to send the mail")
takecommand()
