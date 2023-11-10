import os
from pygame import mixer

class Audio:
	def __init__(self):
		mixer.init()

	@staticmethod
	def capture():
		mixer.music.load(os.curdir + '/src/assets/audio/crunch.mp3')
		mixer.music.play()

	@staticmethod
	def move():
		mixer.music.load(os.curdir + '/src/assets/audio/move.mp3')
		mixer.music.play()