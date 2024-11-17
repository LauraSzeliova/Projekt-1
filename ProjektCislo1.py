'''
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Laura Szeliova
email: szeliova.laura@gmail.com
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

rozdelovac = "*"*40
uzivatel = input("username: ")
heslo = input("password: ")
print(rozdelovac)

registrovanyU = {
    "bob":"123",
    "ann":"pass123",
    "mike":"password123",
    "liz":"pass123"}

if uzivatel.lower() in registrovanyU.keys() and heslo.lower() in registrovanyU.values():
    print(f"Welcome to the app {uzivatel}")
    print(f"We have {len(TEXTS)} texts to be analyzed.",rozdelovac,sep="\n")
else:
    print("unregistered user, terminating the program..")
    exit()

vybranyText = int(input(f"Enter a number btw. 1 and {len(TEXTS)} to select: "))
vycistenyText = [slovo.strip('.,<>?:!') for slovo in TEXTS[vybranyText-1].split()]
print("-"*40)

print(f"There are {len(vycistenyText)} words in the selected text.")

pocetTitle = 0
for slovo in vycistenyText:
    if slovo.istitle():
        pocetTitle += 1
print(f"There are {pocetTitle} words in the selected text.") 

pocetUpper = 0
for slovo in vycistenyText:
    if slovo.isupper() and slovo.isalpha():
        pocetUpper += 1
print(f"There are {pocetUpper} words in the selected text.")

pocetLower = 0
for slovo in vycistenyText:
    if slovo.islower() and slovo.isalpha():
        pocetLower += 1
print(f"There are {pocetLower} words in the selected text.")

pocetCisel = 0
for slovo in vycistenyText:
    if slovo.isdigit():
        pocetCisel += 1
print(f"There are {pocetCisel} numeric strings.")

cisla = []
for slovo in vycistenyText:
    if slovo.isdigit() and not slovo.isalpha():
        cisla.append(int(slovo))
print(f"There are {sum(cisla)} numeric strings.")

zoznamCetnosti = []
for slovo in vycistenyText:
    dlzka = len(slovo)
    zoznamCetnosti.append(dlzka)
tupleCetnosti = tuple(set(zoznamCetnosti))

# pocetSlov = []
# for cislo in zoznamCetnosti:
#     count = zoznamCetnosti.count(cislo)
#     pocetSlov.append(count)
# print(zoznamCetnosti)
# print(pocetSlov) 

slovnikCetnosti = {}
for cislo in zoznamCetnosti:
    if cislo in slovnikCetnosti:
        slovnikCetnosti[cislo] += 1
    else:
        slovnikCetnosti[cislo] = 1
zoradKlic = list(slovnikCetnosti.keys())
zoradKlic.sort()
zoradSlovnik = {}
for key in zoradKlic:
    zoradSlovnik[key] = slovnikCetnosti[key]

print(rozdelovac)
print("LEN|","OCCURENCES".center(22),"|NR.".ljust(22),sep="")
print(rozdelovac)

for key in zoradSlovnik:
    y = key
    z = zoradSlovnik.get(key)
    print(f"{y:>3}|{z*"*":<14} | {z:<3}")
