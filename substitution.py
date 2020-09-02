"""
Zamiana głosek (dyftongi, głoski inaczej wymawiane)
"""

#należy najpierw wykonać zamianę dyftongów, potem uwzględnić różnice w wymowie

def dipht_simpl(string):
    '''
    Zastępuje dyftongi pojedynczymi znakami. Zwraca zmodyfikowany string.
    '''
    string=string.replace('ch','h')
    if not "marzn" in string: string=string.replace('rz','ř')   #if dla eliminacji 'marznąć' i słów pochodnych
    string=string.replace('dz','ζ')                             #dodatkowo rozróżnienie ż-ř ze wzgledu na upodobnienia głoskowe
    string=string.replace('dż','δ')                             #(rz podlega ubezdźwięcznieniu postępowemu, ż nie podlega)
    string=string.replace('dź','∂')
    string=string.replace('sz','σ')
    string=string.replace('cz','3')
   
    
    return string   


def subst_diff(string):
    '''
    Zastępuje w słowie głoski, które są wymawiane inaczej
    ze względu na różnego rodzaju procesy fonetyczne.
    Zwraca zmodyfikowany string.
    '''
    #homofonia
    
    vowels = ['a','ą','e','ę','i','o','u','y'] #samogłoski
    unpals = ['c','n','s','z','ζ'] #spółgłoski podlegające zmiękczeniu, w wersji twardej
    pals   = ['ć','ń','ś','ź','∂'] #spółgłoski zmiękczone
    
        #'i' niezgłoskotwórcze zmiękczające
        
    for j in range(len(unpals)):
        x = 0
        while x < len(string):
            i = string.find(unpals[j]+'i',x)
            if i==-1: break
            elif len(string)>i+2:
                if string[i+2] in vowels:
                    string = string[:i]+pals[j]+string[i+2:]
                    x = i+2
                else:
                    string = string[:i]+pals[j]+string[i+1:]
                    x = i+1
            else:
                string = string[:i]+pals[j]+string[i+1:]
                x = i+1
                
        #'i' niezgłoskotwórcze wymawiane jako 'j'
        
    for v in vowels:
        string=string.replace('i'+v,'j'+v)
    
        #'u' niezgłoskotwórcze
        
    string=string.replace('ó','u')
    string=string.replace('au','ał')
    if not (string.startswith(('ńeu','pżeu')) and 'euσ' in string): string=string.replace('eu','eł') #np. wyrazy takie jak: nieuk, przeuprzejmy, słabeusz
    
        #litery niewystępujące w wyrazach polskich
        
    string=string.replace('x','ks')
    string=string.replace('v','w')
    string=string.replace('q','kw')
    
    #upodobnienie
    
    voiced   = ['b','d','ζ','∂','δ','g','w','z','ź','ż','ř'] #spółgłoski dźwięczne      
    unvoiced = ['p','t','c','ć','3','k','f','s','ś','σ','σ'] #spółgłoski bezdźwięczne (odpowiedniki dźwięcznych)
    
        #ubezdźwięcznienie na końcu wyrazu
    if len(string)>0:
        if string[len(string)-1] in voiced and len(string)>1:
            string = string[:len(string)-1] + unvoiced[voiced.index(string[len(string)-1])]
                #(nie uwzględnia przypadków, gdy głoska nie ulega ubezdźwięcznieniu z powodu dźwięcznego rozpoczęcia kolejnego wyrazu)
            
            #ubezdźwięcznienie wsteczne, postępowe i udźwięcznienie wsteczne
            
        for i in range(len(string)-1):
            if string[i] in voiced and string[i+1] in unvoiced:
                x = voiced.index(string[i])
                string = string[:i]+unvoiced[x]+string[i+1:]
            elif string[i] in unvoiced and string[i+1] in voiced:
                if string[i+1] in ['w','ř']:
                    x = voiced.index(string[i+1])
                    end = string[i+2:] if i+2<len(string) else '' #unika błędu IndexError
                    string = string[:i+1]+unvoiced[x]+end
                else:
                    x = unvoiced.index(string[i])
                    string = string[:i]+voiced[x]+string[i+1:]  
                
    #homofonia ř-ż
        
    string = string.replace('ř','ż')
    
    return string


#a = "siema, jestem karol. co ty na to?"
#
#b = a.split()
#print(b)
#
#for x in range(len(b)):
#   b[x] = b[x].strip('-!?()[]{}:;+=/\\&\'\".,')
#
#print(b)

#a = "rozstrzelany"
#b = "kwierzenie"
#c = "korzenie"
#d = "bohdan"
#e = "kwiat"
#f = "potrzeba"
#print(subst_diff(dipht_simpl(a)),subst_diff(dipht_simpl(b)),subst_diff(dipht_simpl(c)),subst_diff(dipht_simpl(d)),subst_diff(dipht_simpl(e)),subst_diff(dipht_simpl(f)))
