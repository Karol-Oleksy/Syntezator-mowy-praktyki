"""
Funkcje potrzebne do podzielenia słowa na sylaby
"""

def divide(word):
    '''
    Funkcja dzieli słowo na sylaby. Zwraca listę sylab zapisanych jako string.
    '''
    
    vowels = ['a','ą','e','ę','i','o','u','y'] #samogłoski
    consonants = ['b','c','ć','d','f','g','h','j','k','l','ł','m','n','ń','p','r','s','ś','t','w','z','ź','ż','ζ','∂','δ','3','σ'] #spółgłoski
    
    vowel_i = [] #lista indeksów samogłosek
    syllables = [] #lista sylab
    rest = '' #zmienna na wypadek wyrazu bez samogłoski, który trzeba dołączyć do następnego wyrazu
    
    
    for i in range(len(word)):
        if word[i] in vowels:
            vowel_i.append(i)  #zapisywanie indeksów samogłosek w wyrazie
        
        
    if not vowel_i: #przypadek wyrazów bez samogłoski
        #if word in ['z','w']: rest = word
        #else:
        syllables.append(word)   #problem: potrzeba nagrania sylab z dodatkowym 'w' lub 'z' na początku
        
    elif len(vowel_i)==1: #przypadek jednosylabowych wyrazów
        syllables.append(word) 
    
    else:
        first = 0 #początek kolejnej sylaby
        for i in range(len(vowel_i)-1):
            dist = vowel_i[i+1]-vowel_i[i] #dystans między dwiema kolejnymi samogłoskami
            
            if dist%2==0: #dystans jest parzysty (nieparzysta liczba spółgł. między samogł.)
                syllables.append(word[first:(vowel_i[i]+int(dist/2))])
                first = vowel_i[i]+int(dist/2)
                
            elif dist%2==1: #dystans jest nieparzysty (parzysta liczba spółgł. między samogł.)
                syllables.append(word[first:(vowel_i[i]+int(dist/2)+1)])
                first = vowel_i[i]+int(dist/2)+1
                
        syllables.append(word[first:]) #didanie ostatniej sylaby
            
    return syllables, rest

#a = 'marσ3y'
#b,x = divide(a)
#print(b)