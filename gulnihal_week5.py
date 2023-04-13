telefon_rehberi = {}

def kisi_ekle():
    ad = input("Kişinin adini girin: ")
    numara = input("Kişinin telefon numarasini girin: ")
    telefon_rehberi[ad] = numara
    print(ad, " kişisi başariyla eklendi.")

def kisi_duzenle():
    ad = input("Düzenlemek istediğiniz kişinin adini girin: ")
    if ad in telefon_rehberi:
        print("Mevcut veriler: ", ad, ":", telefon_rehberi[ad])
        secim = input("numarayi guncellemek icin 'n', adi guncellemek icin 's' giriniz: ")
        if secim == 'n':
            numara = input("Yeni telefon numarasini girin: ")
            telefon_rehberi[ad] = numara
            print(ad, " kisisinin verileri basariyla güncellendi.")
        elif secim == "s":
            if ad in telefon_rehberi:
                del telefon_rehberi[ad]
                print(ad, " kişisi başariyla silindi.")
            
    else:
        print(ad, " kişisi rehberde bulunamadi.")

def kisi_sil():
    ad = input("Silmek istediğiniz kişinin adini girin: ")
    if ad in telefon_rehberi:
        del telefon_rehberi[ad]
        print(ad, " kişisi başariyla silindi.")
    else:
        print(ad, " kişisi rehberde bulunamadi.")

def kisi_arama():
    ad = input("Aramak istediğiniz kişinin adini girin: ")
    if ad in telefon_rehberi:
        print(ad, " kişisi: ", telefon_rehberi[ad])
    else:
        print(ad, " kişisi rehberde bulunamadi.")

while True:
    print("\nTelefon Rehberi Uygulamasi\n")
    print("1. Kişi Ekle")
    print("2. Kişi Düzenle")
    print("3. Kişi Sil")
    print("4. Kişi Arama")
    print("5. Çikiş")

    secim = input("Seçiminizi girin (1-5): ")

    if secim == '1':
        kisi_ekle()
    elif secim == '2':
        kisi_duzenle()
    elif secim == '3':
        kisi_sil()
    elif secim == '4':
        kisi_arama()
    elif secim == '5':
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
