rehber = {}
def kisi_ekle():
    isim = input("Lutfen isim giriniz: ")
    num = int(input("Lutfen numara giriniz: "))
    rehber[isim] = num
    return print(f"{isim} {num} rehbere kaydedildi." )    
def kisi_duzenle():
    global rehber
    isim = input("Lutfen duzenlemek istediginiz ismi girin: ")

    if isim not in rehber:
        return "Bu kisi rehberde bulunamadi"
    tercih = int(input(f"""{isim} kisisini 
                        guncellemek icin 1, 
                        silmek icin 2 
                        cikmak icin 3 e basin"""))

    if tercih == 3:
      return
    
    elif tercih == 1:      
      tel_num = rehber.pop(isim)
      yeni_isim = input("Lutfen ismi guncelleyin: ")
      rehber.update({yeni_isim : tel_num})

      return print(f"{yeni_isim} olarak guncellendi")
    
    elif tercih == 2:
      del rehber[isim]
      return print(f"{isim} rehberden silindi")
  
def kisi_sil():
  global rehber
  isim = input("Lutfen silmek istediginiz kisinin ismini girin: ")
  if isim not in rehber:
    return "Tekrar deneyin!!!"
  rehber.pop(isim)
  return  print(f"{isim} rehberden silindi")

def kisi_arama():
  global rehber
  isim = input("Lutfen aramak istediginiz kisiyi giriniz: ")
  if isim not in rehber:
    return "Bu kisi rehberde kayitli degil!"

  x = rehber.get(isim)
  return  print(f"Isim: {isim}\nNumara: {x}")

while True:
  print("""
        -----REHBER-----
        (1) Kisi ekle
        (2) Kisi duzenle
        (3) Kisi sil
        (4) Kisi arama
        (5) Cikis
        """)
  number = int(input("Yapmak istediginiz islem numarasini giriniz: "))

  if number == 1:
    kisi_ekle()

  elif number == 2:
    kisi_duzenle()
  elif number == 3:
    kisi_sil()
  elif number == 4:
    kisi_arama()  
  elif number == 5:
    print("Rehber kapatildi!")
    break
  else:
    print("Tekrar deneyin!")  

