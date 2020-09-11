"""
Główne funkcje wykonawcze programu
"""

import spell, substitution, division
from pydub import AudioSegment
from pydub.playback import play
from pydub.effects import normalize


def process_text(text):
    '''
    Funkcja używa napisanych w innych plikach funkcji w celu wyekstrahowania wyrazów
    z tekstu, który należy przeczytać. Dzieli wyrazy na sylaby, w razie potrzeby
    zamienia inne znaki (liczby, skróty) na tekst możliwy do przeczytania.
    Zwraca listę sylab i listę wyrazów.
    '''
    
    words = text.split() #dzieli tekst na wyrazy 
    
    syllables = []
    
    rest = '' #zmienna na wypadek wyrazów bez samogłoski do doklejenia do kolejnego wyrazu
    
    for i, word in enumerate(words):
        
        #usunięcie znaków niealfanumerycznych z początku i końca wyrazu
        nonalphanumerics = ['-','!','?','(',')','[',']','{','}',':',';','+','=','/','\\','&','\'','\"','.',',','„','”','*','#'] 
        words[i] = word = word.strip(''.join(nonalphanumerics))
        
        #usunięcie znaków ze środka wyrazu (podzielenie na 2 wyrazy)
        j = 0
        for char in word:
            if char in nonalphanumerics:
                words.insert(i+1, word[j+1:])
                words[i] = word = word[:j]
            j += 1
    
        #skrótowce
        if word.isupper():
            words[i] = word = spell.acronym(word)
            
        #liczby
        elif word.isdecimal():
            words[i] = word = spell.number(word)
            
        #skróty
        words[i] = word = spell.shortcut(word)         
        
        #działania na każdym wyrazie        
        words[i] = word = word.lower()
        words[i] = word = rest + word #dodaje bezsamogłoskowy wyraz do następnego wyrazu (np. 'w' lub 'z')
        
        words[i] = word = substitution.dipht_simpl(word)
        words[i] = word = substitution.subst_diff(word)
        syls, rest = division.divide(word)
        syllables.extend(syls)
        
    
    return syllables, words

def play_text(text):
    '''
    Główna funkcja programu. Odtwarza tekst podany w argumencie
    '''
    
    syllables, words = process_text(text)
    i=0
    for syllable in syllables:
        if syllable == "con": syllable = "conn" #plik nie może nazywać się 'con.wav'
        if i==0:
            audio = normalize(AudioSegment.from_file('Dźwięki/'+syllable+'.wav'))
        else:
            sound = normalize(AudioSegment.from_file('Dźwięki/'+syllable+'.wav'))
            audio += sound
        i+=1
    play(audio)
