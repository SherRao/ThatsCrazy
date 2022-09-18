import pyaudio
import speech_recognition as sr

recog = sr.Recognizer()
sound = ""

def listen():
    with sr.Microphone() as source:
        print("Say something!")
        sound = recog.listen(source)

    try:
        result = recog.recognize_google(sound)
        print("Google Speech Recognition thinks you said \"" + result + "\"")
        return result;
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
