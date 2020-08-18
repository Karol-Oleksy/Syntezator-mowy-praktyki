"""
Próbny skrypt główny programu
"""

import spell
import substitution
import division




sentence = 'Mamy nadzieję, że ostatni rok z eleven był to czas pełen inspiracji, ciekawych tematów i powodów do dyskusji. Zależy nam, by kolejny rok też taki był. Dlatego przygotowaliśmy dla Ciebie specjalną ofertę ze zniżką i torbą w prezencie.'


words = sentence.split() #dzieli tekst na wyrazy 

syllables = []

rest = '' #zmienna na wypadek wyrazów bez samogłoski do doklejenia do kolejnego wyrazu

for word in words:
    
    #usunięcie znaków przestankowych i innych
    word = word.strip('-!?()[]{}:;+=/\\&\'\".,„”*#') #jesli wyraz zawiera znak w srodku, kod nie usunie go i wyraz zostanie źle podzielony

    #skrótowce
    if word.isupper():
        if len(rest)>0: syllables.append(rest) #w wypadku skrótowców i liczb trzeba nagrać 'w' i 'z' jako osobne sylaby
        syllables.extend(spell.shortcut(word))
        
    #liczby
    elif word.isdecimal():
        if len(rest)>0: syllables.append(rest) #w wypadku skrótowców i liczb trzeba nagrać 'w' i 'z' jako osobne sylaby
        syllables.extend(spell.number(word))
    
    #normalne wyrazy    
    else:
        word = word.lower()
        word = rest + word #dodaje bezsamogłoskowy wyraz do następnego wyrazu (np. 'w' lub 'z')
        
        word = substitution.dipht_simpl(word)
        word = substitution.subst_diff(word)
        syls, rest = division.divide(word)
        syllables.extend(syls)
            
            

print(syllables)



