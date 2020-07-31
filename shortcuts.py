# -*- coding: utf-8 -*-
"""
Obsługa skrótowców
"""

def spell(word):
    '''
    Funkcja zwraca sylaby składające się na skrótowiec podany jako argument
    '''
    syllables = []
    
    for letter in word:
        if letter=='A': syllables.append('a')
        elif letter=='Ą': syllables.append('ą')
        elif letter=='B': syllables.append('be')
        elif letter=='C': syllables.append('ce')
        elif letter=='Ć': syllables.append('cie')
        elif letter=='D': syllables.append('de')
        elif letter=='E': syllables.append('e')
        elif letter=='Ę': syllables.append('ę')
        elif letter=='F': syllables.append('ef')
        elif letter=='G': syllables.append('gie')
        elif letter=='H': syllables.append('ha')
        elif letter=='I': syllables.append('i')
        elif letter=='J': syllables.append('jot')
        elif letter=='K': syllables.append('ka')
        elif letter=='L': syllables.append('el')
        elif letter=='Ł': syllables.append('eł')
        elif letter=='M': syllables.append('em')
        elif letter=='N': syllables.append('en')
        elif letter=='Ń': syllables.append('eń')
        elif letter=='O': syllables.append('o')
        elif letter=='Ó': syllables.append('u')
        elif letter=='P': syllables.append('pe')
        elif letter=='R': syllables.append('er')
        elif letter=='S': syllables.append('es')
        elif letter=='Ś': syllables.append('eś')
        elif letter=='T': syllables.append('te')
        elif letter=='U': syllables.append('u')
        elif letter=='V': syllables.append('fał')
        elif letter=='W': syllables.append('wu')
        elif letter=='X': syllables.append('iks')
        elif letter=='Y': syllables.append('y')
        elif letter=='Z': syllables.append('zet')
        elif letter=='Ź': syllables.append('ziet')
        elif letter=='Ż': syllables.append('żet')
    
    return syllables
        