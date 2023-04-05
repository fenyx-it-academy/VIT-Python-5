telefon_defter={}
def kisi_ekle():
    isim=input('Kişi ismi giriniz:  ').upper()
    telefon=input('Telefon numarasını giriniz:  ')
    telefon_defter[isim]=telefon
    print('Kişi eklendi')

def kisi_duzenle():
    isim=input('Lütfen düzenlemek istediğiniz ismi giriniz:   ').upper()
    if isim in telefon_defter:
        print(f' {isim} adlı kişiye ait telefon numarası:  {telefon_defter[isim]}')
        tercih=input("""
                        İsmi Düzenlemek İçin (1) 
                        Numara düzenlemek için (2) """)
        if tercih=='1':
            yenisim=input('Yeni İsmi Giriniz:  ').upper()
            telefon_defter[yenisim]=telefon_defter.pop(isim)
            print(f'{isim}  adlı kişinin ismi  {yenisim} olarak değiştirildi')
        elif tercih=='2':
            yeninumara=input('Yeni Telefon Numarası Giriniz:  ')
            telefon_defter[isim]=yeninumara
            print(f'{isim} isimli kişinin telefon numrası {yeninumara} olarak değiştirildi')
        else:
            print('Lütfen Geçerli Bir Seçim Yapınız...')
    else:
         print(f'Aradığınız {isim} isimli kişi telefon defterinde bulunamadı !')
    

def kisi_sil():
    isim=input('Lütfen silmek istediğiniz ismi giriniz:   ').upper()
    if isim in telefon_defter:
        secenek=input(f' {isim} Adlı kişiyi telefon defterinden silmek istediğinizden eminmisiniz: E/H ').upper()
        if secenek=='E' :
            telefon_defter.pop(isim)
            print('Kayıt Silindi !')
        else:
            print('Kayıt Silinmedi')
    else:
         print(f'Aradığınız {isim} isimli kişi telefon defterinde bulunamadı !')
        
def kisi_ara():
    isim=input('Aramak istediğiniz ismi giriniz:   ').upper()
    if isim in telefon_defter:
        print(f'Aradığınız {isim} adlı kişiye ait telefon numarası:  {telefon_defter[isim]}')
    else:
        print(f'Aradığınız {isim} isimli kişi telefon defterinde bulunamadı !')

def tum_rehber():
    print('İsim ---- Telefon Numarası')
    for isim,numara in telefon_defter.items():
        print(f"{isim}---- {numara}")



while True:
    print("""
          --Telefon Defteri--
          (1)-Kişi Ekle
          (2)-Kişi Duzenle
          (3)-Kişi Sil
          (4)-Kişi Ara
          (5)-Tüm Rehberi Göster
          (6)-Çıkış""")
    giris=input("Lütfen Seçiminizi Yapınız:  ")
    if giris=='1' :
        kisi_ekle()
    elif giris=='2':
        kisi_duzenle()
    elif giris=='3':
        kisi_sil()
    elif giris=='4':
        kisi_ara()
    elif giris=='5':
        tum_rehber()
    elif giris=='6':
        break
    else:
        print('Lütfen Geçerli Bir Seçim Yapınız')
        continue
