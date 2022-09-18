import pyaudio
import speech_recognition as sr

recog = sr.Recognizer()
sound = ""

def listen():
    with sr.Microphone() as source:
        sound = recog.listen(source)

    try:
        result = recog.recognize_google(sound)
        return { "result": result };

    except sr.UnknownValueError:
        return { "error": "Google Speech Recognition could not understand audio" };

    except sr.RequestError as e:
        return { "error": "Could not request results from Google Speech Recognition service; {0}".format(e) };
