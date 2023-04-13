liste=[ ]
def displaymenu():
    print('Telefon Rehberi')
    print('1-Yeni kisi ekleme')
    print('2-Kisi Duzenleme')
    print('3-Kisi Silme')
    print('4-Kisi Arama')
    print('5-Cikis')
    print()  
    
    
#Bu fonksiyon, kullanıcıdan bir kişi adı ve telefon numarası alarak telefon rehberine ekler.
def kisi_ekle(liste):
  while True:
    print('~~Yeni Kayit Ekle~~')
    name=input('Ad  Giriniz:').title()
    surname=input('Soyad Giriniz :').title()
    telno=input('Telefon Numarasini Giriniz:')
    print()
    print(f'Yeni Kayit:{name} {surname} {telno}','\n')
    if emin_misin():
      print('Kayit Ediliyor')
      kayit=dict(ad=name,soyad=surname,tel=telno)
      liste.append(kayit)
    if devam_mi():
      continue
    else:
      break


def kisi_duzenleme(liste):
  while True:
    for k in liste:
      print('Ad:{} Soyad:{} Telefonnumara {}'.format(k['ad'],k['soyad'],k['tel'] ))
    isim=input ('Duzenlemek  Istediginiz Kisinin Adini Giriniz:').title() 
    secim=int(input ('Soyadini guncellemek icin 1,Telefon numarasini guncellemek icin 2 ye basiniz:')) 
    for i in liste:
      if isim ==i['ad'] and secim==1:
        i['soyad']=input('Guncellemek istediginiz soyadi giriniz:').title()
        print('Ad {} Soyad {} Telefon numarasi {}'.format(i['ad'],i['soyad'],i['tel']))
        print('Soyad Guncellendi')
                
      elif isim ==i['ad'] and secim==2:
        i['tel']=input('Guncellemek istediginiz telefon numarasini giriniz:')
        print('Ad {} Soyad {} Telefon numarasi {}'.format(i['ad'],i['soyad'],i['tel']))
        print('Telefon numarasi guncellendi') 
        break  
    if devam_mi():
      continue
    else :
        break  
      
def kisi_arama(liste):
    while True:
        print('~~Kisi Arama~~')
        isim=input ('Aradiginiz Kisinin Adi Giriniz:').title()
        
        for i in liste:
          if isim== i['ad'] or isim==i['soyad']:
            print('Ad:{}  Soyad:{}  Telnumara:{}'.format(i['ad'],i['soyad'],i['tel'] ))
            break
        else:
          print('{} Bu adda kayit bulunamadi'.format(isim))    
          break
        print()      
        if devam_mi():
            continue
        else:
            break

def kisi_silme(liste):
    while True:
        print('~~Kisi Silme~~') 
        for k in liste:
            print('Ad:{} Soyad:{} Telefonnumara {}'.format(k['ad'],k['soyad'],k['tel'] ))
        isim=input('Silmek Istediginiz Kisinin Adini Giriniz:').title() 
        soyisim=input('Silmek Istediginiz Kisinin Soyadini Giriniz:').title()
        for i in liste:
          if isim== i['ad'] or isim==i['soyad']:
              if emin_misin():
                liste.remove(i)
                print('Silme islemi Basariyla Gerceklestirildi.')
                break
        else: 
          print('{} adli kayit yok'.format(isim))
        
        if devam_mi():
            continue
        else:
            break
        
def devam_mi():
  while True:
    devam=input('Devam etmek istiyor musunuz?(E\H)').upper()
    if devam=='E':
      return True
    else:
      return False
    

def emin_misin():
  while True:
    secenek=input ('Eminmisiniz(E/H):').upper()
    if secenek=='E':
      return True
    else:
      return False
    
while True:
    displaymenu()
    secim=int(input('Yapmak istediginiz islemin numarasini giriniz:'))
    if secim==1:
      kisi_ekle(liste)
    elif secim==2:
      kisi_duzenleme(liste)
    elif secim==3:
      kisi_silme(liste)
    elif secim==4:
      kisi_arama(liste)
    elif secim==5:
      print('~~Cikis yapiliyor~~')
      break    
