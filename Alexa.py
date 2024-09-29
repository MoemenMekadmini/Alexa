import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import time

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
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command
run = True

def run_alexa(first_run=False):
    global run
    
    if first_run:
        talk('How can I help you today?')
        print('How can I help you today?')
    else:
        talk('What would you like me to do next?')
        print('What would you like me to do next?')

    command = take_command()
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'what time is it' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + current_time)
    elif 'search' in command:
        search = command.replace('search', '')
        info = wikipedia.summary(search, 1)
        print(info)
        talk(info)
    elif 'tell me a joke' in command:
        talk(pyjokes.get_joke())
    elif 'stop' in command:
        talk('Goodbye!')
        print('Goodbye!')
        run = False
    else:
        talk('Please say the command again.')
    
    if not first_run:
        time.sleep(15)

first_run = True
while run:
    run_alexa(first_run)
    first_run = False


