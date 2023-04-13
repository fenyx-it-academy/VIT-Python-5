Telefon_Rehberi = "1 - Yeni Kisi Ekleme\n2 - Kisi Duzenleme\n3 - Kisi silme\n4 - Kisi arama"

def kisi_ekleme():
    isim = input("AD:").capitalize()
    numara = input("NUMARA:")
    rehber[isim] = numara

def kisi_duzenle():
    kisi = input("KISI ADI:").capitalize()
    if kisi in rehber:
        # print(rehber.items(kisi))
        duzenle = input("ISIM DUZENLEMEK ICIN -> 'I'\nNUMARA DUZENLEMEK ICIN -> 'N'\nKISIYI SILMEK ICIN -> 'S' ").upper()
        if duzenle == "I":
            yeni_isim = input("YENI ISIM:").capitalize()
            rehber[yeni_isim] = rehber.pop(kisi)
        elif duzenle == "N":
            yeni_numara = input("YENI NUMARA:")
            rehber[kisi] = yeni_numara
        elif duzenle == "S":
            kisi_silme()
    else:
        print("ARADIGINIZ KISI BULUNAMADI!")


def kisi_silme():
    sil = input("SILMEK ISTEDIGINIZ KISI ADINI YAZIN:").capitalize()
    sor = input("EMIN MISIN: E/ H").upper()
    if sor == "E":
        rehber.pop(sil)
    elif sor == "H":
        print("SILME ISLEMI IPTAL EDILDI!")

def kisi_arama():
    ara = input("ARADIGINIZ KISI:").capitalize()
    if ara in rehber:
        print("NUMARASI:",rehber.get(ara))
    else:
        print("BULUNAMADI!")

rehber = {}
while True:
    print("Hosgeldiniz")
    print("Cikis icin -> 'q'")
    print(Telefon_Rehberi)
    secim = input("Bir islem seciniz:")

    if secim == "q":
        break
    elif secim == "1":
        kisi_ekleme()
    elif secim == "2":
        kisi_duzenle()
    elif secim == "3":
        kisi_silme()
    elif secim == "4":
        kisi_arama()
    else:
        print("HATALI GIRIS! TEKRAR DENEYIN.")

    print(20*"-")
    print("MEVCUT REHBERINIZ:")
    print(rehber)
    print(20*"-")
