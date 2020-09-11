--------------------------------------------------------
Opis projektu
--------------------------------------------------------
	Autor: Karol Oleksy
	Opiekun praktyki: dr Krzysztof Rzecki

	Projekt został wykonany w ramach praktyk zawodowych w ramach kierunku Inżynieria Biomedyczna na Akademii Górniczo-Hutniczej im. Stanisława Staszica w Krakowie. 
	Projekt miał na celu stworzenie syntezatora mowy przez nagranie własnej biblioteki dźwięków (opartej na sylabach) i napisanie algorytmu odpowiedzialnego za odtworzenie podanego tekstu.




--------------------------------------------------------
Opis plików programu i możliwości rozwoju
--------------------------------------------------------

-> main.py

	Tutaj zachodzi wykonanie programu. Do zmiennej 'text' należy wpisać tekst, który ma zostać przeczytany.

-> execute.py

  -> funkcja 'process_text'

	W tej funkcji wykorzystywane są funkcje z plików 'spell.py', 'substitution.py' oraz 	'division.py'. Przy przetwarzaniu tekstu usuwane są wszelkie znaki nie będące literami bądź liczbami. Funkcja sprawdza też każdy wyraz, czy nie jest liczbą, skrótem czy skrótowcem (akronimem). Wzięty pod uwagę został również fakt, że wyrazy bez samogłosek ('w', 'z') są wymawiane łącznie z następującym po nich wyrazem (o tym szerzej przy pliku 'division.py').
	Sylaby zwrócone w formie listy nie są już zapisane wg zasad polskiej ortografii, ale wg ich wymowy. Za wymianę znaków odpowiedzialne są funkcje w pliku 'substitution.py' (tam szerzej o ich działaniu). 
	Funkcja zwraca też listę wyrazów w celach statystyczych - wykorzystuje ją plik 		'dict_stats.py'.
	W przyszłości można dodatkowo przeanalizować to, na których miejscach w wyrazie znajdują się sylaby, i na tej podstawie rozróżnić sylaby akcentowane i nieakcentowane. Przy nagrywaniu sylab musiałoby wtedy być dwa razy więcej, ale naturalność odtwarzania byłaby większa.

  -> funkcja 'play_text'

	Funkcja odtwarza tekst podany jako argument. Wykorzystuje funkcję 'process_text'.
	Działanie funkcji opiera się na pakiecie 'pydub', z którego zaimportowanych jest kilka funkcji. W celu osiągnięcia większej płynności odtwarzania sylab dźwięki są najpierw dodawane do siebie w pętli(sklejana jest ścieżka dźwiękowa), a potem dopiero razem odtwarzane. Funkcja 'normalize' zapewnia tą samą głośność każdej sylaby, zmniejszając w ten sposób wpływ różnic w warunkach nagrywania poszczególnych sylab.
	Dźwięki powinny być umieszczone w folderze "Dźwięki" znajdującym się w tym samym folderze, co pliki programu. Dźwięki powinny być zapisane w formacie *.wav - w przeciwnym razie należy uwzględnić rozszerzenie w kodzie w tej funkcji a także w funkcjach pliku 'dict_stats.py'.
	Sama funkcja zapewnia odpowiednio płynne odtwarzanie sylab. W przyszłości można dopracować ręcznie wykonany proces nagrywania - zadbać o wyższą jakość i podobne warunki nagrywania każdej sylaby. Należy też dopracować proces przycinania nagranych sylab, aby były możliwie jak najkrótsze przy jednoczesnym zapewnieniu maksimum zrozumienia sylaby - to zapewni większą płynność i naturalność odtwarzania.



-> spell.py

	Plik ma na celu zapewnienie odpowiedniej wymowy każdego wyrazu, również tych niezapisanych dosłownie tak, jak się je wymawia. Obecnie obsługiwane są skróty, skrótowce i liczby.

  -> funkcja 'shortcut'
	
	Skróty podmieniane są na odpowiadające im wyrazy. Lista skrótów jest ograniczona, w przyszłości można ją rozwinąć o więcej, szczególnie mniej popularnych skrótów.

  -> funkcja 'acronym'
	
	Każda litera jest wymawiana zgodnie z zasadami języka polskiego. Funkcja nie uwzględnia skrótowców pochodzących z innego języka i tamtejszych zasad wymowy (np. angielskie CIA lub francuskie TGV). W przyszłości możnaby dodać wyjątki dla najbardziej popularnych skrótowców zagranicznych.

  -> funkcja 'number'

	Funkcja składa się z szeregu warunków w pętli, zapewniających odpowiednie odczytanie każdej z cyfr w zależności od miejsca w liczbie. Funkcja ma skończone możliwości - obsługuje jedynie liczby do 9999999. W razie rozdzielenia liczby separatorami (spacje, kropki) liczba zostanie potraktowana jako osobne wyrazy, czyli osobne liczby. W przyszłości można zaadresować ten problem przez uwzględnienie dodatkowych warunków sprawdzających sąsiednie wyrazy w tekście. Słuszne będzie również dodanie większej liczby warunków do rozszerzenia zakresu obsługiwanych liczb.



-> substitution.py

	Plik zawiera funkcje odpowiadające za podmianę liter w przetwarzanym tekście, aby jak najbardziej upodobnić reprezentację tekstową do wymowy słów.

  -> funkcja 'dipht_simpl'

	Funkcja ma na celu zastąpienie występujących w tekście dyftongów pojedynczymi znakami. Jest to istotne przy dzieleniu wyrazów na sylaby w pliku 'division.py', które opiera się na wzajemnej pozycji kolejnych samogłosek oddzielonych spółgłoskami - w przypadku dyftongu mogłaby zajść sytuacja, w której zostanie on podzielony na dwie osobne głoski w dwóch sylabach.
	W przyszłości należy opracować więcej warunków dla przypadków, w których określony układ dwóch liter nie jest wymawiany jako dyftong (np. 'marznąć', już uwzględniony w kodzie).
	W tej funkcji i w innych plikach programu, jak również w nazwach dźwięków używa się następujących znaków dla reprezentacji dyftongów:
	ζ = dz
	δ = dż
	∂ = dź
	σ = sz
	3 = cz
	ř = rz (na razie; po obsłudze ubezdźwięcznień i udźwięcznień  w funkcji 'subst_diff' zamiana na 'ż')
	W tym miejscu również zastępowany jest dyftong 'ch' przez 'h' - te głoski we współczesnym języku polskim wymawia się identycznie.

  -> funkcja 'subst_diff'

	Funkcja obsługuje zjawiska zachodzące w języku polskim wpływające na zmienioną wymowę niektórych liter pod wpływem miejsca w słowie i sąsiadujących liter. Obsługiwane są poniższe zjawiska:

	- 'i' niezgłoskotwórcze

	'i' może występować w roli samogłoski zgłoskotwórczej, jak np. w wyrazach "ikona" i "wizyta", a także w roli niezgłoskotwórczej, jak np. w wyrazach "pies" i "nie". Algorytm sprawdza, czy po literze 'i' w słowie występuje inna samogłoska - wtedy 'i' jest wyrzucane z tekstu, a spółgłoska ją poprzedzająca jest poddawana palatalizacji (zmiękczeniu; w przypadku głosek: 'c', 'n', 's', 'z', 'ζ') lub zamianie na kombinację spółgłoska+'j' (w przypadku pozostałych spółgłosek, np. 'p', 'b', 'w' itp.).
	Jeśli 'i' jest zgłoskotwórcze, również zmiękcza poprzedzającą je spółgłoskę. W takim przypadku również następuje zamiana spółgłoski na jej spalatalizowaną wersję, aby zwrócić na to uwagę przy nagrywaniu dźwięków. Jest to ważne przy nazywaniu plików dźwiękowych - sylaba 'nić' powinna być zapisana wtedy jako 'ńić', gdyż tak zostanie zapisana przez algorytm w liście sylab.

	- 'u' niezgłoskotwórcze
	
	To zjawisko jest obserwowane zwykle w wyrazach obcego pochodzenia, gdzie występują złożenia 'au', 'eu', wymawiane jako 'ał', 'eł' (np. 'Europa', 'auto'). W przyszłości należy dopisać więcej warunków dla przypadków szczególnych, kiedy 'u' w takich złożeniach jest zgłoskotwórcze, np. uwzględnione już w kodzie 'nieuk', 'przeuprzejmy' czy 'słabeusz'.
	W tym miejscu uwzględniona jest również podmiana 'ó' przez 'u' - głoski wymawiane identycznie.

	- litery niepolskie

	Podmiana liter 'x', 'v', 'q' przez wymowę odpowiadającą im zazwyczaj w wyrazach obcych używanych w języku polskim. W przyszłości można również uwzględnić inne litery charakterystyczne dla innych języków mogących pojawić się w nazwach własnych bądź zapożyczeniach zapisanych wg oryginalnej pisowni (np. 'ö', 'ñ', 'ß').

	- upodobnienia

	Algorytm obsługuje następujące rodzaje upodobnień:

		- ubezdźwięcznienie na końcu wyrazu

		- ubezdźwięcznienie wsteczne (głoska traci dźwięczność pod wpływem następującej po niej głoski bezdźwięcznej)

		- ubezdźwięcznienie postępowe (głoska traci dźwięczność pod wpływem poprzedzającej ją głoski bezdźwięcznej)

		- udźwięcznienie wsteczne (głoska zyskuje dźwięczność pod wpływem następującej po niej głoski dźwięcznej)

	Nie są uwzględnione przypadki upodobnień międzywyrazowych - zwykle na końcu wyrazu zachodzi ubezdźwięcznienie, jednak gdy następny wyraz rozpoczyna się głoską dźwięczną, ubezdźwięcznienie nie zachodzi (a nawet następuje udźwięcznienie, jeśli ostatnia głoska pierwszego wyrazu jest bezdźwięczna). W przyszłości można dopracować algorytm np. przez stworzenie zmiennej zachowującej ostatnią głoskę wyrazu i przekazywanej do obsługi kolejnego wyrazu.



-> division.py

	-> funkcja 'divide'

	Funkcja ma na celu podział wyrazu na sylaby. Wyraz podany jako argument powinien uprzednio zostać poddany działaniu funkcji z pliku 'substitution.py'. 
	Funkcja opiera się na ilości samogłosek w wyrazie oraz ich pozycji. Podział na sylaby następuje w połowie między dwiema samogłoskami (np. 'kości' -> 'koś','ci'). W przypadku nieparzystej liczby spółgłosek między samogłoskami, większą ilość spółgłosek otrzymuje druga sylaba (np. 'koty' -> 'ko','ty'; 'marszczy' -> 'mar','szczy').
	Funkcja oprócz listy sylab zwraca również zmienną 'rest', która winna być przydatna w przypadku, gdy wyraz nie zawiera żadnych sylab (np. wyrazy 'w', 'z', staropolskie 'k'). Zawartość 'rest' jest potem "doklejana" do początku następnego wyrazu wewnątrz funkcji 'execute.process_text'. Obecnie funkcjonalność ta nie jest wykorzystywana i w bibliotece nagranych dźwięków znajdują się "sylaby" 'w' oraz 'z'. Skorzystanie z tej funkcjonalności spowoduje większą naturalność odczytywanego tekstu, jednak wymaga nagrania dodatkowej ilości sylab z 'z' i 'w' "doklejonymi" na początku.



-> dict_stats.py

	Plik nie jest częścią konieczną do działania programu syntezatora. Służy celom opracowania biblioteki dźwięków na podstawie słowników oraz celom statystycznym (kontrola ilości nagranych sylab). Wyniki statystyk są zamieszczone na końcu tego pliku tekstowego.
	W pliku tym ważne jest, aby nagrane sylaby znalazły się w folderze "Dźwięki" w tym samym miejscu, co plik.

	-> funkcja 'dict_read'

	Funkcja opracowuje listę słów, listę sylab a także listę sylab wraz z liczbą określającą częstotliwość ich występowania na podstawie słownika w formacie *.txt przekazanego jako argument. Do opracowania pełnej listy sylab skorzystano ze słownika słów z formami pochodnymi dostępnego na stronie https://sjp.pl/slownik/odmiany/ (plik słownika znajduje się wśród plików projektu pod nazwą 'odm.txt'). Należy wziąć pod uwagę, że w tym słowniku obecne są także słowa obcego pochodzenia zapisane wg pisowni oryginalnej, co powoduje wytworzenie sylab nieobecnych w języku polskim. 

	-> funkcja 'tuple_list_to_list'
	
	Funkcja tworzy listę pierwszych elementów krotek znajdujących się w liście podanej jako argument. Funkcja powstała w celu stworzenia listy sylab posortowanych wg częstotliwości występowania w słowniku.

	-> funkcja 'write_to_csv'

	Funkcja zapisuje listę w formacie *.csv w celu późniejszej pracy nad nią w programie MS Excel.

	-> funkcja 'syl_stats'
	
	Opracowuje statystykę nagranych sylab - ile sylab jest już nagranych i jaki to procent możliwych sylab.

	-> funkcja 'word_stats'

	Opracowuje statystykę słów możliwych do wypowiedzenia z użyciem nagranych sylab - ile słów można już wypowiedzieć i jaki to procent wszystkich słów.

	-> funkcja 'manage_popular_words'

	Funkcja powstała w celu opracowania przejrzystej listy najpopularniejszych 1000 i 100 słów języka polskiego. Jako argument podano plik tekstowy 'pop.txt' będący kopią treści strony https://pl.wiktionary.org/wiki/Indeks:Polski_-_Najpopularniejsze_słowa_1-1000_wersja_Jerzego_Kazojcia , na której podano listę tysiąca najpopularniejszych polskich słów wg słownika frekwencyjnego autorstwa Jerzego Kazojcia wraz z liczbą określającą częstość występowania. Wynik działania funkcji można zobacyć w plikach 'words1000.txt' oraz 'words100.txt'.

	-> funkcja 'delete_recorded'

	Funkcja usuwa z podanej jako argument listy sylab te sylaby, które już zostały nagrane.




--------------------------------------------------------
Pozostałe pliki w projekcie
--------------------------------------------------------

-> folder 'Dźwięki'

	Bezpośrednio w folderze znajdują się dotychczas nagrane sylaby (na bierząco uzupełniane). Znajduje się tu także folder 'projekty audacity' zawierający pliki projektów programu Audacity używanego do nagrywania sylab.

-> 1000w_sylstorec_freq.xlsx

	Lista sylab składających się na 1000 najpopularniejszych słów, które należy jeszcze nagrać (stan na dzień 11.09.2020). Lista jest posortowana wg częstości występowania sylab (malejąco).

-> odm.txt

	Słownik odmian ze strony https://sjp.pl/slownik/odmiany/ .

-> pop.txt
	
	Lista 1000 najpopularniejszych wyrazów wraz z częstością występowania wg Jerzego Kazojcia - kopia treści strony https://pl.wiktionary.org/wiki/Indeks:Polski_-_Najpopularniejsze_słowa_1-1000_wersja_Jerzego_Kazojcia .

-> sylaby otwarte.xlsx

	Sylaby otwarte w języku polskim ([spółgłoska]+samogłoska). Wszystkie zostały nagrane.

-> syllables.xlsm

	Lista sylab wyekstrahowana ze słownika odmian. Plik zawiera makro pozwalające na obliczenie sylab oznaczonych poszczególnymi kolorami. Legenda kolorów:
	- zielony: sylaba nagrana
	- żółty: sylaba nagrana już wcześniej (w gronie 'sylab otwartych')
	- niebieski: suma sylab zielonych i żółtych (wszystkie nagrane)
	- czerwony: sylaba odrzucona ze względu na jej bezsensowność dla języka polskiego
	- biały: pozostałe sylaby

-> words100.txt

	Lista 100 najpopularniejszych wyrazów wg Jerzego Kazojcia.

-> words1000.txt
	
	Lista 1000 najpopularniejszych wyrazów wg Jerzego Kazojcia.




--------------------------------------------------------
Statystyki
--------------------------------------------------------

	Poniżej zamieszczono wyniki statystyk aktualnych na dzień 11.09.2020.

Ilość sylab wg słownika odmian              23610
W tym ilość sylab nagranych                  2180  (9,2%)

Ilość sylab wg words1000.txt		      870
W tym ilość sylab nagranych		      222 (25,5%)

Ilość sylab wg words100.txt		      106
W tym ilość sylab nagranych		       56 (52.8%)

Ilość wyrazów wg słownika odmian	  4527259
W tym ilość wyrazów nagranych	           587388 (13,0%)

Ilość wyrazów wg words1000.txt		     1000
W tym ilość wyrazów nagranych		      239 (23,9%)

Ilość wyrazów wg words100.txt                 100
W tym ilość wyrazów nagranych                  50 (50,0%)