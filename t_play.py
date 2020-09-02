"""
Próbny skrypt do odtwarzania dźwięków
"""

import simpleaudio as sa
from main import main
from playsound import playsound
import pydub
from pydub import AudioSegment
from pydub.playback import play
from pydub.effects import normalize

word = main('cześć mamo co dziś na o bjadek')
i=0
for syllable in word:
    #play_obj = sa.WaveObject.from_wave_file('Dźwięki/'+syllable+'.wav').play()
    #play_obj.wait_done()
    #playsound('Dźwięki/'+syllable+'.wav')
    if syllable == "con": syllable = "conn" #plik nie może nazywać się 'con.wav'
    if i==0:
        audio = normalize(AudioSegment.from_file('Dźwięki/'+syllable+'.wav'))
    else:
        sound = normalize(AudioSegment.from_file('Dźwięki/'+syllable+'.wav'))
        audio += sound
    #play(sound)
    i+=1
play(audio)