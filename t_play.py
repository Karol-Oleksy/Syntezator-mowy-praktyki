"""
Próbny skrypt do odtwarzania dźwięków
"""

import simpleaudio as sa
from main import main


#ko = sa.WaveObject.from_wave_file('Dźwięki/ko.wav')
#że = sa.WaveObject.from_wave_file('Dźwięki/że.wav')
#ńe = sa.WaveObject.from_wave_file('Dźwięki/ńe.wav')
#wi = sa.WaveObject.from_wave_file('Dźwięki/wi.wav')
#rus = sa.WaveObject.from_wave_file('Dźwięki/rus.wav')

word = main('')

for syllable in word:
    play_obj = sa.WaveObject.from_wave_file('Dźwięki/'+syllable+'.wav').play()
    play_obj.wait_done()
