"""
Skrypt do rozłożenia wyrazów ze słownika odmian na sylaby
"""
import main, csv

file = open("odm.txt", encoding="utf-8")
text = file.read().replace("\n"," ")
file.close
print("plik odczytany")

syllables_all = main.main(text)
print("sylaby wyekstrahowane")

syllables = []
for syl in syllables_all:
    if not syl in syllables:
        syllables.append(syl)
print("sylaby powtarzające się usunięte")

syllables.sort()
print("sylaby posortowane")

with open('syllables.csv', 'w', newline='', encoding="utf_16") as csv_file:
    write = csv.writer(csv_file, quoting=csv.QUOTE_NONE)
    write.writerow(syllables)
print("sylaby zapisane w pliku .csv")
        
