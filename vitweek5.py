rehber = {
    'ALI': '+31 6123456780',
    'VELI': '+31 6123456781',
    'AYSE': '+31 6123456782'
}
print('Rehberiniz: ', rehber)
# Bu fonksiyon, kullanıcıdan bir kişi adı ve telefon numarası alarak telefon rehberine ekler.
while True:
    def kisi_ekle():
        kisi = input('Rehbere eklemek icin yeni kisi adi giriniz: ').upper()
        numara = input('Rehbere eklemek icin yeni numara giriniz: ')
        rehber[kisi] = '+31 ' + numara
    kisi_ekle()
    print('Yeni kisi rehbere eklendi')
    print('Yeni rehberiniz: ', *rehber)

# Bu fonksiyon, kullanıcıdan bir kişi adı alarak telefon rehberindeki kişiler listesinde bu kişiyi bulur.
# Ardından, kullanıcıya mevcut verileri güncelleme veya silme seçenekleri sunar.
    def kisi_duzenle():
        global kisiBul
        kisiBul = input(
            "Lutfen rehberinizdeki silmek yada guncellemek istediginiz ismi yaziniz: ").upper()
        if kisiBul in rehber:
            sonuc = rehber[kisiBul]
            print(
                f'Aradiginiz isim: {kisiBul} {sonuc} olarak Rehber icinde bulunmustur')
        else:
            print(
                f'Ardiginiz isim: {kisiBul} rehberde bulunamamistir.')
        return

    def kisi_sil_ara():
        guncelle = input(
            "Sectiginiz ismi silmek isterseniz: 'S', guncellemek isterseniz: 'G' , aramak isterseniz 'A' tusuna, vazgecmek isterseniz 'X' tusuna basiniz: ").upper()

        if guncelle == 'S':
            silindi = rehber.pop(kisiBul)
            print(kisiBul, 'rehberden basariyla silindi')
        elif guncelle == 'X':
            print('Cikis yapildi.')
            return rehber
        elif guncelle == 'A':
            print(f'Sectiginiz isim olan {kisiBul} araniyor')
        elif guncelle == 'G':
            yeniGuncelIsim = input('Yeni bir isim giriniz: ').upper()
            yeniGuncelNumara = int(input('Yeni bir numara giriniz: '))
            if kisiBul in rehber:
                rehber[yeniGuncelIsim] = yeniGuncelNumara
                if yeniGuncelIsim != kisiBul:
                    del rehber[kisiBul]
                print("Rehber güncellendi.")
            else:
                print("Girilen anahtar rehberde mevcut değil.")

            print('Yeni isim: ', yeniGuncelIsim, 've', 'Numarasi: ', yeniGuncelNumara,
                  'rehberde basariyla guncellendi')
        else:
            print("Girdiginiz isim rehberde bulunamadi.")
    kisi_duzenle()
    kisi_sil_ara()
    print('Yeni rehber: ', rehber)
