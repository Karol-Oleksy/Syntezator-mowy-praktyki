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
vowel_i = []

for word in words:
    
    if word.isupper():
        syllables = shortcuts.spell(word)
    
    else:
        for i in range(len(word)-1):
            if word[i] in vowels:
                vowel_i.append(i)
        for i in range(len(vowel_i)-1):
            if vowel_i[i]

print(syllables)



