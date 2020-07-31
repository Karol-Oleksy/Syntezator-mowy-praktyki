# -*- coding: utf-8 -*-
"""
Zamiana głosek (dyftongi, głoski niewyróżniające się)
"""

def subst_unused(string):
    '''
    Zastępuje głoski, które nie wyróżniają się w tekscie
    '''
    string.replace('ó','u')
    string.replace('b ','p ')
    string.replace('b.', 'b.')
    
    
    
   
    
    
    
    return




def dipht_simpl(string):
    
    string.replace('ch','h')
    string.replace('rz','ż')
    string.replace('dz','C')
    string.replace('dż','D')
    string.replace('dź','Δ')
    string.replace('sz','S')
   
    
    return    
