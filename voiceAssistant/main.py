import speech_recognition as sr
import pyttsx3
import datetime
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
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass

    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'how are you' in command:
        talk('i am good what about you??')
    elif 'i am good' in command:
        talk('thats really good')
    elif 'tell me about yourself' in command:
        talk('i am ai bot created by Mayur Saini')
    elif 'bye' in command:
        talk('bye bye')
    elif 'morning' in command:
        talk('good morning')
    elif 'night' in command:
        talk('good night')        
    else:
        talk('Please say the command again.')


while True:
    run_alexa()
