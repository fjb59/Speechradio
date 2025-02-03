import pyttsx3
class talker:
    def __init__(self):
        self.engine = pyttsx3.init()
    def testMessage(self,tFreq):
        self.engine.say(f"Frequency set to {tFreq} megahertz")
    def speak(self):
        self.engine.runAndWait()

