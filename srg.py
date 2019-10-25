import speech_recognition as sr

r = sr.Recognizer()
Microphone = sr.Microphone()
def __init__(self):
    self.pyaudio_module = self.get_pyaudio()
    
with sr.__init__(Microphone) as source:
    print("Speak Anything: ")
    audio = r.listen(source)
    
    try:
        text = r.recognize_api(audio)
        print("You said: {}".format(text))
    except:
        print("Sorry, could not recognize your voice")


