from vosk import Model, KaldiRecognizer
import pyaudio

class voxListener:
    def __init__(self):

        model = Model("model")
        self.recognizer = KaldiRecognizer(model, 16000)

        self.mic = pyaudio.PyAudio().open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
        self.mic.start_stream()
    def listen(self):
        print("Listening...")
        while True:
            data = self.mic.read(4000, exception_on_overflow=False)
            if self.recognizer.AcceptWaveform(data):
                command = self. recognizer.Result()
                print("Recognized:", command)