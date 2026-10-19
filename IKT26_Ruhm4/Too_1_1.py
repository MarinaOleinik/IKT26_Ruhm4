# Kirjuta enda esimene programm, mis väljastab käsureale teksti: “Tere, maailm!”. 
# Küsi kasutaja nimi ja muuda tekst, et ta näeks välja nii: 
#     “Tere, maailm! Tervitan sind Mati”, kui kasutaja nimi on Mati.
# Küsi kasutajalt sisend tema vanuse kohta ning väljasta see ekraanile:
# “Tere, maailm! Tervitan sind Mati! Sa oled N aastat vana.”
# Ülesanne 1
print("Tere, maailm!")
nimi=input("Sisesta oma nimi => ")
print("Tere, maailm! Tervitan sind", nimi)
vanus=input("Sisesta oma vanus => ")
print("Tere, maailm! Tervitan sind", nimi, "! Sa oled", vanus, "aastat vana.")

# Mis tüüpi on järgnevad muutujad:
# a) vanus = 18
# b) eesnimi = "Jaak"
# c) pikkus = 16.5
# d) kas_käib_koolis = True
# Mis võimalus veel peale True oleks viimast muutujat väärtustada? Kuidas võiks nende muutujate väärtusi koodis kontrollida?
# Kirjuta kood tüüpide kontrollimiseks. Type() funktsioon tagastab muutuja tüübi.
# Ülesanne 2
vanus=18
eesnimi="Jaak"
pikkus=16.5
kas_käib_koolis=True

print(type(vanus)) #-> <class 'int'>
print(type(eesnimi)) #-> <class 'str'>
print(type(pikkus)) #-> <class 'float'>
print(type(kas_käib_koolis)) #-> <class 'bool'>

# Kirjuta enda koodis laual olevate kommide arv muutujasse
# (kommide arv on juhuslik). 
# Seejärel kuva muutujas olev kommide arv ekraanile kasutades print() käsku.
# Küsi kasutajalt sisendit, mitu kommi ta soovib laualt ära võtta. 
# Eemalda soovitud kommide arv laual olevate kommide arvust ja kuva ekraanile, 
# kui palju komme laual nüüd on.
#Ülesanne 3
from random import *
kommide_arv=randint(1, 100) # juhuslik arvu 1-100 vahel
print("Laual on", kommide_arv, "kommi.")
mitu_ara_võta=int(input("Mitu kommi soovid laualt ära võtta? => "))
kommide_arv -= mitu_ara_võta
print("Laual on nüüd", kommide_arv, "kommi.")

# Puu läbimõõdu arvutamine
# Kirjuta programm, mis küsib kasutaja käest puu ümbermõõdu
# ning teatab selle peale puu läbimõõdu.
#Ülesanne 4
ümbermõõt=float(input("Sisesta puu ümbermõõt => "))
läbimõõt=ümbermõõt/3.14
print("Puu läbimõõt on", läbimõõt)


