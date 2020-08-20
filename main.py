"""
Próbny skrypt główny programu
"""

import spell, substitution, division

sentence = 'Litwo! Ojczyzno moja! ty jesteś jak zdrowie: Ile cię trzeba cenić, ten tylko się dowie, Kto cię stracił. Dziś piękność twą w całej ozdobie Widzę i opisuję, bo tęsknię po tobie. '

def main(sentence):
    words = sentence.split() #dzieli tekst na wyrazy 
    
    syllables = []
    
    rest = '' #zmienna na wypadek wyrazów bez samogłoski do doklejenia do kolejnego wyrazu
    
    i = 0
    for word in words:
        
        #usunięcie znaków niealfanumerycznych z początku i końca wyrazu
        nonalphanumerics = ['-','!','?','(',')','[',']','{','}',':',';','+','=','/','\\','&','\'','\"','.',',','„','”','*','#'] 
        word = word.strip(''.join(nonalphanumerics))
        
        #usunięcie znaków ze środka wyrazu (podzielenie na 2 wyrazy)
        j = 0
        for char in word:
            if char in nonalphanumerics:
                words.insert(i+1, word[j+1:])
                word = word[:j]
            j += 1
    
        #skrótowce
        if word.isupper():
            word = spell.acronym(word)
            
        #liczby
        elif word.isdecimal():
            word = spell.number(word)
            
        #skróty
        word = spell.shortcut(word)         
        
        #działania na każdym wyrazie        
        word = word.lower()
        word = rest + word #dodaje bezsamogłoskowy wyraz do następnego wyrazu (np. 'w' lub 'z')
        
        word = substitution.dipht_simpl(word)
        word = substitution.subst_diff(word)
        syls, rest = division.divide(word)
        syllables.extend(syls)
        
        i += 1
    
    print(syllables)
    return syllables



main(sentence)