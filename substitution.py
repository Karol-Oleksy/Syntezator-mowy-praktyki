"""
Zamiana głosek (dyftongi, głoski inaczej wymawiane)
"""

#należy najpierw wykonać zamianę dyftongów, potem uwzględnić różnice w wymowie

def dipht_simpl(string):
    '''
    Zastępuje dyftongi pojedynczymi znakami
    '''
    
    string=string.replace('ch','h')
    string=string.replace('rz','ż')  #wziąć pod uwagę, że są słowa jak 'marznąć'
    string=string.replace('dz','ζ')
    string=string.replace('dż','δ')
    string=string.replace('dź','∂')
    string=string.replace('sz','σ')
    string=string.replace('cz','3')
   
    
    return string   


def subst_diff(string):
    '''
    Zastępuje w słowie głoski, które są wymawiane inaczej
    ze względu na różnego rodzaju procesy fonetyczne
    '''
    #homofonia
        #'i' niezgłoskotwórcze zmiękczające
        
    vowels = ['a','ą','e','ę','i','o','u','y']
    unpals = ['c','n','s','z','ζ']
    pals   = ['ć','ń','ś','ź','∂']
    
    for j in range(len(unpals)):
        x = 0
        while x < len(string):
            i = string.find(unpals[j]+'i',x)
            if i==-1: break
            elif string[i+2] in vowels:
                string = string[:i]+pals[j]+string[i+2:]
                x = i+2
            else:
                string = string[:i]+pals[j]+string[i+1:]
                x = i+1
                
        #'i' niezgłoskotwórcze wymawiane jako 'j'
        
    for v in vowels:
        string=string.replace('i'+v,'j'+v)
    
        #'u' niezgłoskotwórcze
        
    string=string.replace('ó','u')
    string=string.replace('au','ał')
    if not string.startswith(('ńeu','pżeu')): string=string.replace('eu','eł') #np. wyrazy takie jak: nieuk, przeuprzejmy
    
    
    #ubezdźwięcznienie
        #na końcu wyrazu
        
    voiced = ['b','d','ζ','∂','δ','g','w','z','ź','ż']
    unvoiced = ['p','t','c','ć','3','k','f','s','ś','σ','h']
    
    if string[len(string)-1] in voiced:
        string = string[:len(string)-1] + unvoiced[voiced.index(string[len(string)-1])]
    
    #ubezdźwięcznienie przez upodobnienie
    
 
    
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
#a = 'w australii'
#print(subst_diff(a))