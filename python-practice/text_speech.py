from gtts import gTTS
import os
file_name = input("Enter file name: ")
file = open(file_name, 'r').read()

speech = gTTS(text=file, lang='en', slow=False)
speech_name = input("Enter name with .mp3 extension to save speech: ")
speech.save(speech_name)
os.system(speech_name)