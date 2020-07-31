# -*- coding: utf-8 -*-
"""
Próbny skrypt do dzielenia wyrazu na sylaby
"""

import shortcuts
import substitution

vowels = ['a','ą','e','ę','i','o','u','y']
consonants = ['b','c','ć','d','f','g','h','j','k','l','ł','m','n','ń','p','r','s','ś','t','w','z','ź','ż']


sentence = 'koronawirus to wirus'


words = sentence.split()

syllables = []

for word in words:
    
    if word.isupper():
        syllables = shortcuts.spell(word)
    
    else:
        for i in range(len(word)-1):
            if word[i] in consonants and word[i+1] in vowels:
                syllables.append(word[i:i+2])

print(syllables)



