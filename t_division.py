
"""
Próbny skrypt do dzielenia wyrazu na sylaby
"""

import shortcuts
import substitution

vowels = ['a','ą','e','ę','i','o','u','y']
consonants = ['b','c','ć','d','f','g','h','j','k','l','ł','m','n','ń','p','r','s','ś','t','w','z','ź','ż','ζ','∂','δ','3','σ']


sentence = 'koronawirus to wirus'

#przed podzieleniem na wyrazy trzeba poddać zdanie podstawieniom z pliku substitution.py
#skrótowców też trzeba poszukać tutaj, przed podziałem na wyrazy,
# bo trzeba dać do lowercase wyrazy zaczynające się wielką literą,
# żeby dobrze dokonały się podstawienia

#albo można po prostu działać od razu na słowach zamiast na całosci...

words = sentence.split()

syllables = []
vowel_i = []

for word in words:
    
    #usunięcie znaków przestankowych i innych
    word = word.strip('-!?()[]{}:;+=/\\&\'\".,')

    #wymowa skrótowca
    if word.isupper():
        syls = shortcuts.spell(word)
    else:
        word = word.lower()
        
    for i in range(len(word)-1):
        if word[i] in vowels:
            vowel_i.append(i)
    for i in range(len(vowel_i)-1):
        if vowel_i[i]:
            
            
    syllables.append(syls) #inaczej, bo syls to lista

print(syllables)



