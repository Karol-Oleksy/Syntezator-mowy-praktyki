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


#ko = sa.WaveObject.from_wave_file('Dźwięki/ko.wav')
#że = sa.WaveObject.from_wave_file('Dźwięki/że.wav')
#ńe = sa.WaveObject.from_wave_file('Dźwięki/ńe.wav')
#wi = sa.WaveObject.from_wave_file('Dźwięki/wi.wav')
#rus = sa.WaveObject.from_wave_file('Dźwięki/rus.wav')

word = main('Litwo! Ojczyzno moja! ty jesteś jak zdrowie: Ile cię trzeba cenić, ten tylko się dowie, Kto cię stracił. Dziś piękność twą w całej ozdobie Widzę i opisuję, bo tęsknię po tobie. ')
i=0
for syllable in word:
    #play_obj = sa.WaveObject.from_wave_file('Dźwięki/'+syllable+'.wav').play()
    #play_obj.wait_done()
    #playsound('Dźwięki/'+syllable+'.wav')
    if i==0:
        audio = normalize(AudioSegment.from_file('Dźwięki/'+syllable+'.wav'))
    else:
        sound = normalize(AudioSegment.from_file('Dźwięki/'+syllable+'.wav'))
        audio += sound
    #play(sound)
    i+=1
play(audio)