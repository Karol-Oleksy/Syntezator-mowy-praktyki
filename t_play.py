
"""
Próbny skrypt do odtwarzania dźwięków
"""

import simpleaudio as sa


ko = sa.WaveObject.from_wave_file('Dźwięki/ko.wav')
ro = sa.WaveObject.from_wave_file('Dźwięki/ro.wav')
na = sa.WaveObject.from_wave_file('Dźwięki/na.wav')
wi = sa.WaveObject.from_wave_file('Dźwięki/wi.wav')
rus = sa.WaveObject.from_wave_file('Dźwięki/rus.wav')

word = [ko,ro,na,wi,rus]

for syllable in word:
    play_obj = syllable.play()
    play_obj.wait_done()
