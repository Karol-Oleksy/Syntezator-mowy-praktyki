# -*- coding: utf-8 -*-
"""
Zamiana głosek (dyftongi, głoski inaczej wymawiane)
"""

#należy najpierw wykonać zamianę dyftongów, potem uwzględnić różnice w wymowie

def dipht_simpl(string):
    '''
    Zastępuje dyftongi pojedynczymi znakami
    '''
    
    string.replace('ch','h')
    string.replace('rz','ż')  #wziąć pod uwagę, że są słowa jak 'marznąć'
    string.replace('dz','ζ')
    string.replace('dż','δ')
    string.replace('dź','∂')
    string.replace('sz','σ')
    string.replace('cz','3')
   
    
    return    


def subst_diff(string):
    '''
    Zastępuje w słowie głoski, które są wymawiane inaczej
    ze względu na różnego rodzaju procesy fonetyczne
    '''
    voiced = ['b','d','ζ','∂','δ','g','w','z','ź','ż']
    unvoiced = ['p','t','c','ć','3','k','f','s','ś','σ','h']
    
    #homofonia
    string.replace('ó','u')
    string.replace('au','ał')
    
    #ubezdźwięcznienie na końcu wyrazu
    if string[len(string)-1] in voiced:
        string = string[:len(string)-1] + unvoiced[voiced.index(string[len(string)-1])]
    
    #ubezdźwięcznienie przez upodobnienie
    
    
    
    
   
    
    
    
    return string


a = "siema, jestem karol. co ty na to?"

b = a.split()
print(b)

for x in range(len(b)):
   b[x] = b[x].strip('-!?()[]{}:;+=/\\&\'\".,')

print(b)
