# # VIT-Python-5

# ## Telefon Rehberi Uygulamasi

# Bu program, kullanicilarin telefon rehberlerindeki kisileri yönetmelerine ve aramalarina olanak tanir. 
# Program, Python sözlüklerini kullanarak verileri depolar.

# **Özellikler**

#   *  Yeni kisi ekleme
#   *  Kisi düzenleme
#   *  Kisi silme
#   *  Kisi arama


# ### Fonksiyonlar

# Programiniz asağidaki fonksiyonlardan olusabilir:

# #### `kisi_ekle()`
# Bu fonksiyon, kullanicidan bir kisi adi ve telefon numarasi alarak  telefon rehberine ekler.
telefon_rehberi={}
def kisi_ekle():
    ad = input("Kisinin adini girin: ")
    numara = input("Kisinin telefon numarasini girin: ")
    telefon_rehberi[ad] = numara
    print(ad, "kisisi telefon rehberine eklendi.")




# #### `kisi_düzenle()`
# Bu fonksiyon, kullanicidan bir kisi adi alarak telefon rehberindeki kisiler listesinde bu kisiyi bulur. Ardindan, kullaniciya mevcut verileri güncelleme veya silme seçenekleri sunar.

def kisi_düzenle():
    ad = input("Düzenlemek istediğiniz kisinin adini girin: ")
    if ad in telefon_rehberi:
        print(ad, "kisisinin mevcut numarasi:", telefon_rehberi[ad])
        print("Ne yapmak istersiniz?")
        print("1. Numarayi güncelle")
        print("2. Kisiyi sil")
        secim = int(input("Seçiminizi yapin (1 veya 2): "))
        if secim == 1:
            yeni_numara = input("Yeni telefon numarasini girin: ")
            telefon_rehberi[ad] = yeni_numara
            print(ad, "kisisinin numarasi güncellendi.")
        elif secim == 2:
            del telefon_rehberi[ad]
            print(ad, "kisisi rehberden silindi.")
        else:
            print("Geçersiz seçim.")
    else:
        print(ad, "kisisi telefon rehberinde bulunamadi.")



# #### `kisi_sil()`
# Bu fonksiyon, kullanicidan bir kisi adi alarak telefon rehberindeki kisiler listesinde bu kisiyi bulur ve siler.
def kisi_sil():
    ad = input("Silmek istediğiniz kisinin adini girin: ")
    if ad in telefon_rehberi:
        del telefon_rehberi[ad]
        print(ad, "kisisi rehberden silindi.")
    else:
        print(ad, "kisisi telefon rehberinde bulunamadi.")




# #### `kisi_arama()`
# Bu fonksiyon, kullanicidan bir kisi adi alarak telefon rehberindeki kisiler listesinde bu kisiyi bulur ve ekrana görüntüler.

def kisi_arama():
    ad = input("Aramak istediğiniz kisinin adini girin: ")
    if ad in telefon_rehberi:
        print(ad, "kisisinin numarasi:", telefon_rehberi[ad])
    else:
        print(ad, "kisisi telefon rehberinde bulunamadi.")




#Kisinin yapmak istedigi islemi soran ana ekran

while True:
    print("\nTelefon Rehberi Uygulamasi")
    print("1. Yeni kisi ekleme")
    print("2. Kisi düzenleme")
    print("3. Kisi silme")
    print("4. Kisi arama")
    print("5. Çikis\n")

    secim = input("Bir seçenek seçin: ")

    if secim == "1":
        kisi_ekle()
    elif secim == "2":
        kisi_düzenle()
    elif secim == "3":
        kisi_sil()
    elif secim == "4":
        kisi_arama()
    elif secim == "5":
        print("Programdan çikiliyor...")
        break
    else:
        print("Geçersiz seçenek! Lütfen tekrar deneyin.")
    print(telefon_rehberi)
        
