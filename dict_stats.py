"""
Skrypt do pracy na słowniku i liście sylab do celów statystycznych.
"""
import main, csv, os, division

def dict_read(filepath):
    '''
    Ładuje plik słownika odmian w formacie *.txt i dzieli go na sylaby.
    Usuwa powtarzające się sylaby i sortuje je.
    Zwraca:
        - listę wszystkich możliwych sylab wg słownika
        - listę słów w słowniku (wszystkich form)
        - dictionary zawierający możliwe sylaby oraz liczbę ich występowania
          (posortowany wg częstotliwości występowania)
    ''' 

    file = open(filepath, encoding="utf-8")
    text = file.read().replace("\n"," ")
    file.close
    print("plik odczytany")
    
    syllables_all, words = main.main(text)
    text = None
    print("sylaby wyekstrahowane")
    
    syllables = []
    syl_freq = {}
    for syl in syllables_all:
        if not syl in syllables:
            syllables.append(syl)
            syl_freq[syl] = 1
        if syl in syllables:
            syl_freq[syl] += 1
        
    syllables_all = None
    print("sylaby powtarzające się usunięte")
    
    syllables.sort()
    print("lista posortowana")
    
    syl_freq = sorted(syl_freq.items(), key=lambda x: x[1], reverse=True)
    print("dictionary posortowany")
    
    return syllables, words, syl_freq

def write_to_csv(syllables):
    '''
    Zapisuje listę sylab jako plik w formacie *.csv.
    Nie zwraca nic.
    '''
    
    with open('syllables.csv', 'w', newline='', encoding="utf_16") as csv_file:
        write = csv.writer(csv_file, quoting=csv.QUOTE_NONE)
        write.writerow(syllables)
    print("sylaby zapisane w pliku .csv")
    
    return

def syl_stats(syllables):
    '''
    Liczy, ile sylab z listy podanej jako argument zostało już nagranych.
    Nie zwraca nic.
    '''
    
    all_count = len(syllables)
    count = 0     
    for filename in os.listdir("Dźwięki"):
        if filename[:-4] in syllables:
            count += 1
    print("Nagrano już {} z {} możliwych sylab, czyli {:.1f}% sylab.".format(count, all_count, count/all_count*100))
    
    return

def word_stats(words):
    '''
    Liczy, ile słów z listy podanej jako argument można wypowiedzieć przy użyciu
    nagranych już sylab.
    Nie zwraca nic.
    '''
    
    all_count = len(words)
    count = 0
    recorded = os.listdir("Dźwięki")
    for word in words:
        syls, r = division.divide(word)
        for i, syl in enumerate(syls):
            syls[i] = syl + ".wav"
        if set(syls).issubset(recorded):
            count += 1
    print("Możliwe jest wypowiedzenie {} z {} słów, czyli {:.1f}% słów.".format(count, all_count, count/all_count*100))

syllables, words, stat_syls = dict_read("odm.txt")
#write_to_csv(syllables)
#syl_stats(syllables)
#word_stats(words)
