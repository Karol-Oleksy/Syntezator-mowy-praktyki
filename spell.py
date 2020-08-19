"""
Obsługa niezwyczajnych wyrazów (skróty, skrótowce, liczby)
"""

def shortcut(word):
    '''
    Funkcja przepisuje skrót tak, jak powinien być wymówiony. Zwraca string.
    '''
    spelling = ''
    
    shortcuts  = ['dr','prof','inż','mgr','hab','lek','med','ks','jw','np','itd','itp','tj','tzn','mln','mld','tys','n.p.m','n.e','p.n.e','nr','pkt','%','°','°C']
    howtospell = ['doktor','profesor','inżynier','magister','habilitowany','lekarz','medycyny','ksiądz','jakwyżej','naprzykład','itakdalej','itympodobne','tojest','toznaczy','milionów','miliardów','tysięcy','nadpoziomemmorza','naszejery','przednasząerą','numer','punkty','procent','stopni','stopnicelsjusza']
    
    if word in shortcuts:
        i = shortcuts.index(word)
        spelling += howtospell[i]  
    else: spelling = word
    
    return spelling


def acronym(word):
    '''
    Funkcja przepisuje skrótowiec tak, jak powinien być wymówiony. Zwraca string.
    '''
    
    spelling = ''
    
    uppercase  = ['A','Ą','B','C','Ć','D','E','Ę','F','G','H','I','J','K','L','Ł','M','N','Ń','O','Ó','P','Q','R','S','Ś','T','U','V','W','X','Y','Z','Ź','Ż','0','1','2','3','4','5','6','7','8','9']
    howtospell = ['a','ą','be','ce','će','de','e','ę','ef','gje','ha','i','jot','ka','el','eł','em','en','eń','o','u','pe','ku','er','es','eś','te','u','fał','wu','iks','igrek','zet','źet','żet','zero','jeden','dwa','trzy','cztery','pięć','sześć','siedem','osiem','dziewięć']
    
    for letter in word:
        i = uppercase.index(letter)
        if i>-1: spelling += howtospell[i]
    
    return spelling
        

def number(word):
    '''
    Funkcja przepisuje liczebnik zapisany cyframi na tekst.
    Obsługuje cyfry od 0 do 9.999.999 (możliwosc rozszerzenia zakresu przez dodanie warunków).
    Nie obsługuje liczb z separatorami (kropkami, spacjami itp. pomiędzy segmentami).
    Zwraca string.
    '''
    words_num = [] #lista słów liczebnika
    
    word = ''.join(reversed(word)) #pętla rozpoczyna od najmniejszej wielokrotnosci, dlatego następuje odwrócenie liczby
    
    
    for dig_i in range(len(word)):
        digit = word[dig_i]
        
        #RZĄD
        
        if dig_i in [1,4]:
            if   digit=='2': words_num.append('dzieścia')
            elif digit in ['3','4']: words_num.append('dzieści')
            elif digit=='0': continue
            elif digit!='1': words_num.append('dziesiąt')
            
        if dig_i in [2,5]:
            if   digit=='1': words_num.append('sto')
            elif digit=='2': words_num.append('ście')
            elif digit in ['3','4']: words_num.append('sta')
            elif digit=='0': continue
            else: words_num.append('set')
            
        if dig_i==3:
            try:
                if   digit=='1' and len(word)<5: words_num.append('tysiąc')
                elif digit in ['2','3','4'] and word[4]!='1': words_num.append('tysiące')
                else: words_num.append('tysięcy')
            except IndexError:
                if   digit=='1': words_num.append('tysiąc')
                elif digit in ['2','3','4']: words_num.append('tysiące')
                else: words_num.append('tysięcy')
            
        if dig_i==6:
            if   digit=='1': words_num.append('milion')
            elif digit in ['2','3','4']: words_num.append('miliony')
            else: words_num.append('milionów')
            
        #CYFRA
        
        #liczby zakończone na 'nascie'
        if dig_i in [0,3] and len(word)>dig_i+1 and word[dig_i+1]=='1':
            if   digit=='0': words_num.append('dziesięć')
            elif digit=='1': words_num.append('jedenaście')
            elif digit=='2': words_num.append('dwanaście')
            elif digit=='3': words_num.append('trzynaście')
            elif digit=='4': words_num.append('czternaście')
            elif digit=='5': words_num.append('pietnaście')
            elif digit=='6': words_num.append('szesnaście')
            elif digit=='7': words_num.append('siedemnaście')
            elif digit=='8': words_num.append('osiemnaście')
            elif digit=='9': words_num.append('dziewietnaście')
            dig_i += 1
            
        #liczby niezakończone na 'nascie' 
        else:
            if   digit=='0' and len(word)==1: words_num.append('zero')
            elif digit=='1' and (dig_i==0 or (dig_i==3 and len(word)>4)): words_num.append('jeden')
            elif digit=='2' and dig_i!=2: words_num.append('dwa')
            elif digit=='2' and dig_i==2: words_num.append('dwie')
            elif digit=='3': words_num.append('trzy')
            elif digit=='4' and dig_i!=1: words_num.append('cztery')
            elif digit=='4' and dig_i==1: words_num.append('czter')
            elif digit=='5': words_num.append('pięć')
            elif digit=='6': words_num.append('sześć')
            elif digit=='7': words_num.append('siedem')
            elif digit=='8': words_num.append('osiem')
            elif digit=='9': words_num.append('dziewięć')
        
    words_num.reverse() #odwrócenie dla poprawnej kolejnosci
    numeral = ' '.join(words_num)
    
    return numeral
    
#num = '200'
#print(number(num))