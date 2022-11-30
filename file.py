import speech_recognition as sr 
from os import path
from pydub import AudioSegment

# convert mp3 to wav
sound = AudioSegment.from_mp3("sample.mp3")
sound.export("sample.wav", format="wav")

Audio_file = "sample.wav"

# using the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(Audio_file) as source:
    audio = r.record(source)
    print(r.recognize_google(audio))