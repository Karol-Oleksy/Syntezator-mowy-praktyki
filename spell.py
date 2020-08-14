# -*- coding: utf-8 -*-
"""
Obsługa sniezwyczajnych wyrazów (skrótowce, liczby)
"""

def shortcut(word):
    '''
    Funkcja zwraca sylaby składające się na skrótowiec podany jako argument
    '''
    
    syllables = []
    
    for letter in word:
        if   letter=='A': syllables.append('a')
        elif letter=='Ą': syllables.append('ą')
        elif letter=='B': syllables.append('be')
        elif letter=='C': syllables.append('ce')
        elif letter=='Ć': syllables.append('će')
        elif letter=='D': syllables.append('de')
        elif letter=='E': syllables.append('e')
        elif letter=='Ę': syllables.append('ę') #trzeba dograć 'ę' i 'ą' do sylab otwartych!
        elif letter=='F': syllables.append('ef')
        elif letter=='G': syllables.append('gje')
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
        elif letter=='Ź': syllables.append('źet')
        elif letter=='Ż': syllables.append('żet')
    
    return syllables
        

def number(word):
    '''
    Funkcja zwraca sylaby składające się na liczbę zapisaną w tekscie cyframi
    Obsługuje cyfry od 0 do 9.999.999
    '''
    syllables = []
    
    word = ''.join(reversed(word)) #zaczniemy wymowę od najmniejszej wielokrotnosci
    
    
    for dig_i in range(len(word)):
        digit = word[dig_i]
        
#        if digit=='0':  #nie ogarnia, kiedy liczby to "50000" np.
#            continue
        #RZĄD
        
        if dig_i in [1,4]:
            if   digit=='2': syllables.extend(('ća','∂eś'))
            elif digit in ['3','4']: syllables.extend(('ći','∂eś'))
            elif digit!='1': syllables.extend(('śąt','∂e'))
            
        if dig_i in [2,5]:
            if   digit=='1': syllables.append('sto')
            elif digit=='2': syllables.append('śće')
            elif digit in ['3','4']: syllables.append('sta')
            else: syllables.append('set')
            
        if dig_i==3:
            if   digit=='1' and word[4]!='1': syllables.extend(('śąc','ty'))
            elif digit in ['2','3','4'] and word[4]!='1': syllables.extend(('ce','śą','ty'))
            else: syllables.extend(('cy','śę','ty'))
            
        if dig_i==6:
            if   digit=='1': syllables.extend(('jon','mil'))
            elif digit in ['2','3','4']: syllables.extend(('ny','jo','mil'))
            else: syllables.extend(('nów','jo','mil'))
            
        
        #CYFRA
        
        #liczby zakończone na 'nascie'
        if dig_i in [0,3] and len(word)>dig_i+1 and word[dig_i+1]=='1':
            if   digit=='0': syllables.extend(('śęć','∂e'))
            elif digit=='1': syllables.extend(('će','naś','de','je'))
            elif digit=='2': syllables.extend(('će','naś','dwa'))
            elif digit=='3': syllables.extend(('će','naś','tσy'))
            elif digit=='4': syllables.extend(('će','naś','3ter'))
            elif digit=='5': syllables.extend(('će','naś','pjet'))
            elif digit=='6': syllables.extend(('će','naś','σes'))
            elif digit=='7': syllables.extend(('će','naś','dem','śe'))
            elif digit=='8': syllables.extend(('će','naś','śem','o'))
            elif digit=='9': syllables.extend(('će','naś','wjet','∂e'))
            dig_i += 1
            
        #liczby niezakończone na 'nascie' 
        else:
            if   digit=='0' and len(word)==1: syllables.extend(('ro','ze'))
            elif digit=='1' and dig_i==0: syllables.extend(('den','je'))
            elif digit=='2' and dig_i!=2: syllables.append('dwa')
            elif digit=='2' and dig_i==2: syllables.append('dwje')
            elif digit=='3': syllables.append('tσy')
            elif digit=='4' and dig_i!=1: syllables.extend(('ry','3te'))
            elif digit=='4' and dig_i==1: syllables.append('3ter')
            elif digit=='5': syllables.append('pjęć')
            elif digit=='6': syllables.append('σeść')
            elif digit=='7': syllables.extend(('dem','śe'))
            elif digit=='8': syllables.extend(('śem','o'))
            elif digit=='9': syllables.extend(('wjęć','∂e'))
        
    syllables.reverse()
    
    return syllables
    
num = '110'
print(number(num))