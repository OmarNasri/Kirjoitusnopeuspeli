import random
import time
import math
import json
import os
def avaa(tiedosto,lista):
    with open (tiedosto,"r") as tiedosto:
        for rivi in tiedosto:
            lista.append(rivi)
def Tallennus(pelaaja, nopeus, kokonaisaika, virheet, tiedosto):
    tulokset = {pelaaja:{
        "Nopeus": nopeus,
        "Virheet":virheet,
        "Kokonaisaika":kokonaisaika
        }
        }
    with open(tiedosto,"a") as f:
        json.dump(tulokset,f,indent=1)
def NopeusPeli(lista,maara):
    PeliSanat = random.sample(lista,maara)
    PeliSanatTulostus = ' '.join(PeliSanat)
    print ("Sinulla on muutama sekunti aikaa tutustua sanoihin, jonka jälkeen kirjoita ne mahdollisimman nopeasti: " ,PeliSanatTulostus)
    time.sleep(4)
    alku = time.time()
    KayttajanSanat = [item for item in input("Syötä näkemäsi sanat mahdollisimman nopeasti: ").split()] 
    loppu = time.time()
    syottoaika = loppu-alku
    syottonopeus = math.ceil(15/(syottoaika/60))
    virheet = 0
    for i in range (maara):
        try:
            if PeliSanat[i] != KayttajanSanat[i]:
                virheet += 1
        except IndexError:
             virheet = virheet+(maara-len(KayttajanSanat))
             print("Syötit väärän määrän sanoja, sait sakkopisteitä.")
             break
    pisteet = math.ceil(syottoaika+virheet*10)
    print("Sinulla kesti yhteensä" ,math.ceil(syottoaika) ,"sekuntia")
    print("Kirjoitit" ,syottonopeus, "sanaa minuutissa")
    print ("Sinulle tuli" ,virheet, "syöttövirhettä.")
    print("Kokonaisaikasi sakkopisteet mukaan laskettuna on: ", pisteet ,"sekuntia")
    tallennus = True
    while tallennus:
        Save = input("Haluatko tallentaa tuloksesi pistetilastoihin? k tai e. : ")
        if Save == "k":
            nimi = input("Kirjoita tähän nimesi: ")
            Tallennus(nimi, syottonopeus, pisteet, virheet, "tulokset.json.")
            print("Peli tallennettu!")
            break
        if Save == "e":
            print("peli päättyi.")
            break
        else:
            print("Virheellinen vaihtoehto, yritä uudelleen.")
pelaus = True
while pelaus == True:
    print("Jos haluat sulkea pelin, kirjoita sulje.")
    Pelitila = input("Haluatko pelata, vai tulostaa pistetilastot? Kirjoita Peli tai Pisteet: " )
    if Pelitila == "Peli":
        Sanat = []
        pelisymboli = input("Haluatko pelata satunnaisilla sanoilla, vai kokonaisilla lauseilla? Kirjoita sanat tai lauseet!: ")
        if pelisymboli == "lauseet":
            avaa("sanat2.txt",Sanat)
            Sanat = [item.strip() for item in Sanat]
            NopeusPeli(Sanat,3)
        elif pelisymboli == "sanat":
            avaa("sanat.txt",Sanat)
            Sanat = [item.strip() for item in Sanat]
            NopeusPeli(Sanat,15)
    elif Pelitila == "Pisteet":
        with open ("tulokset.json","r") as tiedosto:
            for i in tiedosto:
                print (i)
        jatkaminen = True
        while jatkaminen:
            print("Jos haluat tyhjentää pistetilastot, kirjoita tyhjenna.")
            jatko = input("Jos haluat jatkaa peliä, kirjoita tähän jatka. Jos haluat sulkea ohjelman kirjoita sulje. :")
            if jatko == "jatka":
                break
            elif jatko == "sulje":
                print("Kiitos pelaamisesta, peli sulkeutuu.")
                time.sleep(2)
                exit()
            elif jatko == "tyhjenna":
                varmennus = True
                while varmennus:
                    varmuus = input("Oletko varma että haluat tyhjentää tulostaulukon? Jos haluat syötä k, jos et syötä e: ")
                    if varmuus == "k":
                        os.remove("tulokset.json")
                        print("Tulostaulu tyhjennetty!")
                        break
                    if varmuus == "e":
                        break
                    else:
                        print("Virheellinen vaihtoehto, yritä uudelleen.")
            else:
                print("Virheellinen vaihtoehto, yritä uudelleen.")
    elif Pelitila == "sulje":
        print("Kiitos pelaamisesta, peli sulkeutuu.")
        time.sleep(2)
        exit ()
    else:
        print("Virheellinen vaihtoehto, yritä uudelleen.")
    
    
        
        
    


        



