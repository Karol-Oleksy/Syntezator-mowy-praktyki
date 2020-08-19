"""
Skrypt do rozłożenia wyrazów ze słownika odmian na sylaby
"""
import main, csv

#file = open("odm.txt", encoding="utf-8")
#text = file.read().replace("\n"," ")
#file.close
#
#syllables_all = main.main(text)
#
#syllables = []
#
#for syl in syllables_all:
#    if not syl in syllables:
#        syllables.append(syl)
#
#syllables.sort()


with open('syllables.csv', 'w', newline='', encoding="utf_16") as csv_file:
    write = csv.writer(csv_file, quoting=csv.QUOTE_NONE)
    write.writerow(syllables)
    
        
