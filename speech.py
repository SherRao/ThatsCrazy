import speech_recognition as sr
import pyttsx3
# import win32api

recog = sr.Recognizer()
engine = pyttsx3.init()


def listen():
    with sr.Microphone() as source:
        sound = recog.listen(source)

    try:
        result = recog.recognize_google(sound)
        return {"result": result}

    except sr.UnknownValueError:
        return {"error": "Google Speech Recognition could not understand audio"}

    except sr.RequestError as e:
        return {"error": "Could not request results from Google Speech Recognition service; {0}".format(e)}

def speak(text):
    # # Language in which you want to convert
    # language = 'en'

    # myobj = gTTS(text=text, lang=language, slow=False)

    # # Saving the converted audio in a mp3 file named
    # # welcome
    # myobj.save("text.mp3")

    # # Playing the converted file
    # system("text.mp3")

    # getting details of current speaking rate
    # rate = engine.getProperty('rate')
    # print(rate)  # printing current voice rate
    engine.setProperty('rate', 150);

    # voices = engine.getProperty('voices')  # getting details of current voice
    # print(voices)
    # engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine.setProperty('voice', engine.getProperty('voices')[0].id)

    # getting to know current volume level (min=0 and max=1)
    # volume = engine.getProperty('volume')
    # print(volume)  # printing current volume level

    engine.say(text)
    engine.runAndWait()
