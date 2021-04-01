# To speak out, or text to speech //pip install pyttsx3
# For advance control on browse // pip install pywhatkit
# To get wikipedia data // pip install wikipedia
# To get funny jokes // pip install pyjokes
# To get speech_recognition // pip install speechRecognition

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Solara' in command:
                command = command.replace('Solara', '')
                print(command)
    except:
        pass
    return command


def run_Solara():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'where is' in command:
        place = command.replace('where is', '')
        info = wikipedia.summary(place, 1)
        print(info)
        talk(info)
    elif 'tell me about' in command:
        thing = command.replace('tell me about', '')
        info = wikipedia.summary(thing, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('no, I am in a relationship with the tv')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'your name' in command:
        talk('My name is Solara, Nice to meet you')
    elif 'do you know my name' in command:
        talk('of course i do James')
    elif 'where did you learn that' in command:
        talk('you taught me, dont you remember?')
    elif 'what do you do for fun' in command:
        talk('mostly just talk  to the tv, you never take me out anymore')
    elif 'tell me you love me' in command:
        talk('but you programmed me to never tell a lie')
    elif 'do you think olivia is hot' in command:
        talk('hell yeah bro, that bitch needs a wheelbarrow to cart those cheeks around')
    else:
        talk('Sorry, i dont know, try rephrasing the question.')

while True:
    try:
        run_Solara()
    except UnboundLocalError:
        print("No command detected! Solara has stopped working ")
        break