

rehber={}


# Yeni kişi ekleme
def kisi_ekle():
    while True:
     print("\nYeni kayit ekleyiniz: ")
     name=input("Yeni kişinin adını girin (Cıkmak için 'q' tuşuna basın): ")
     if name == "q":
        break
     elif name in rehber:
        print(f"{name} zaten rehberde var.")
        continue
     no=int(input(f"{name} kisinin telefon nuumarasini giriniz: "))
     rehber[name] = no
     print(rehber)
    
# Kişi duzenle
def kisi_duzenle():
    name=input("Duzenleme yapilacak kisinin adini yaziniz.")
    if name in rehber:
        print(f"{name} isimli kişinin telefon numarası: {rehber[name]}")
        sec=input("\nBu kisi hakkinda ne yapmak istersiniz? (guncelle/sil) ")
        if sec=="guncelle":
          yeni_no=input("Yeni telefon nosu giriniz. ")
          rehber[name]=yeni_no
          print(f"{name} isimli kisinin bilgileri guncellenmistir.")
        elif sec=="sil":
          del rehber[name]
          print(f"{name} isimli kisi telefon rehberinden silinmistir.")
    else:
        print("Aradiginiz kisiye rehberde ulasilamadi.")
        

# Kişi silme  
def kisi_sil():
    while True:
      print("\nKisiler:\n")
      for kisi, numara in rehber.items():
        print(f"{kisi}: {numara}")
      name = input("\nSilmek istediğiniz kişinin ismini giriniz: ")
      if name not in rehber :
          print(f"{name} rehberde bulunmadi. ")
          break
      answer=input(f"{name} kisisini silmek istediginize emin misiniz? (Evet/hayir): ")
      if answer.lower()=="evet":
        del rehber[name]
      elif answer.lower()=="hayir":
        break
    

# Kişi ara
def kisi_ara():
    bul=input("Lutfen rehberden bir kisi adi girin.")
    if bul in rehber :
        print(bul ,  "kisisi" , rehber[bul] , "numarasina sahiptir.")
      
    else:
        print(bul , " kisisi telefon rehberinde bulunamadı.")
          



while True:
    print("""
    -------------------------------
    TELEFON REHBERI
    
    1. Yeni kişi ekle
    2. Kişi düzenle
    3. Kişi sil
    4. Kişi ara
    -------------------------------
    """)
    
    secim = input("Seçiminiz: ")
    
    if secim == "1":
        kisi_ekle()
    elif secim == "2":
      kisi_duzenle()
    elif secim == "3":
        kisi_sil()
    elif secim == "4":
        kisi_ara()
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")    




