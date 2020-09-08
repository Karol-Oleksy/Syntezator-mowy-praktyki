"""
Próbny skrypt główny programu
"""

import spell, substitution, division


def main(sentence):
    words = sentence.split() #dzieli tekst na wyrazy 
    
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


#sentence = 'Litwo! Ojczyzno moja! ty jesteś jak zdrowie: Ile cię trzeba cenić, ten tylko się dowie, Kto cię stracił. Dziś piękność twą w całej ozdobie Widzę i opisuję, bo tęsknię po tobie. '
#
#print(main(sentence))