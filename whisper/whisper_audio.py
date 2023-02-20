import os
import time
import pickle
import whisper
import sounddevice as sd
from scipy.io.wavfile import write

import warnings
warnings.filterwarnings('ignore')

class Audio_To_Text:
	def __init__(self, model_type = 'tiny.en'):
		self.model = whisper.load_model(model_type)

	def transcribe(self, audio_file = 'output.wav'):
		text = self.model.transcribe(os.path.join(audio_file))['text']
		text = text.lower()
		return 'hello spotify' in text

	def listen(self):
		fs = 44100
		seconds = 3
		myrecording = sd.rec(int(seconds * fs), samplerate = fs, channels = 1)
		sd.wait()
		write('output.wav', fs, myrecording)