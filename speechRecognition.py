import pyaudio
import speech_recognition as sr
from google.cloud import speech

recog = sr.Recognizer()
sound = ""

with sr.Microphone() as source: 
    print("Say something!")
    sound = recog.listen(source)

try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said \"" +
          recog.recognize_google(sound) + "\"")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print(
        "Could not request results from Google Speech Recognition service; {0}".format(e))
